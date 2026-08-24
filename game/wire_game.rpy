# Мини-игра "Провода" (Flow Free-стиль) для сцены с техником на складе.
# Рабочая логика на простых цветных фигурах, без арта - чтобы проверить, что механика реализуема.
# Управление: зажми точку и веди мышью по соседним клеткам до второй точки того же цвета, отпусти.
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить: jump wire_game_demo

init python:
    import pygame

define wire_colors = {
    "red": (230, 72, 60),
    "purple": (155, 77, 224),
    "cyan": (57, 214, 224),
    "green": (62, 209, 90),
    "yellow": (242, 212, 60),
    "blue": (60, 124, 230),
    "orange": (242, 147, 60),
}

init python:

    def _hamiltonian_neighbors(pos, visited, size):
        r, c = pos
        result = []
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                result.append((nr, nc))
        return result

    def _generate_hamiltonian_path(size, step_budget=20000):
        """Ищет путь, проходящий через КАЖДУЮ клетку поля ровно один раз (рандомизированный
        бэктрекинг с правилом Варнсдорфа - сначала идём в клетки с наименьшим числом
        свободных соседей, иначе поиск слишком часто загоняет себя в тупик)."""
        total = size * size
        start = (renpy.random.randint(0, size - 1), renpy.random.randint(0, size - 1))
        visited = set([start])
        path = [start]
        budget = [step_budget]

        def extend():
            if len(path) == total:
                return True
            budget[0] -= 1
            if budget[0] <= 0:
                return False

            candidates = _hamiltonian_neighbors(path[-1], visited, size)
            scored = []
            for cand in candidates:
                free_count = len(_hamiltonian_neighbors(cand, visited, size))
                scored.append((free_count, renpy.random.random(), cand))
            scored.sort(key=lambda item: (item[0], item[1]))

            for _count, _rand, cand in scored:
                path.append(cand)
                visited.add(cand)
                if extend():
                    return True
                path.pop()
                visited.remove(cand)

            return False

        if extend():
            return path
        return None

    def _serpentine_path(size):
        """Змейка, гарантированно проходящая через все клетки - надёжный запасной вариант."""
        path = []
        for r in range(size):
            cols = range(size) if r % 2 == 0 else range(size - 1, -1, -1)
            for c in cols:
                path.append((r, c))
        return path

    def _partition_path(path, k, min_len):
        """Режет путь на k смежных кусков случайной длины (каждый не короче min_len) -
        куски становятся цветными проводами, вместе покрывающими весь путь целиком."""
        total = len(path)
        if k <= 0 or k * min_len > total:
            return None

        extra_total = total - k * min_len
        if k > 1:
            cuts = sorted(renpy.random.randint(0, extra_total) for _i in range(k - 1))
        else:
            cuts = []

        extras = []
        prev = 0
        for c in cuts:
            extras.append(c - prev)
            prev = c
        extras.append(extra_total - prev)

        segments = []
        idx = 0
        for e in extras:
            length = min_len + e
            segments.append(path[idx:idx + length])
            idx += length
        return segments

    def generate_wire_level(size=6, colors=None, min_len=2, max_tries=40):
        """Строит уровень от готового решения, покрывающего ВСЕ клетки поля (полный путь
        по сетке, нарезанный на цветные сегменты) - поэтому условие "все клетки заполнены"
        всегда достижимо игроком, а не только "провода соединены"."""
        if colors is None:
            colors = ["red", "blue", "green", "yellow", "purple"]

        num_colors = len(colors)

        for _try in range(max_tries):
            path = _generate_hamiltonian_path(size)
            if path is None:
                continue

            segments = _partition_path(path, num_colors, min_len)
            if segments is None:
                continue

            endpoints = {}
            for color, seg in zip(colors, segments):
                endpoints[color] = [seg[0], seg[-1]]
            return {"size": size, "endpoints": endpoints}

        # Гарантированно проходимый запасной вариант, если случайный поиск не удался.
        path = _serpentine_path(size)
        segments = _partition_path(path, num_colors, min_len)
        if segments is None:
            num_colors = max(2, (size * size) // max(min_len, 2))
            colors = colors[:num_colors]
            segments = _partition_path(path, num_colors, min_len)

        endpoints = {}
        for color, seg in zip(colors, segments):
            endpoints[color] = [seg[0], seg[-1]]
        return {"size": size, "endpoints": endpoints}

    class GradientPanelDisplayable(renpy.Displayable):
        """Тёмная панель со скошенной по диагонали рамкой цвет-в-цвет (голубой -> розовый),
        не зависящая от размера - без артефактов растяжения, в отличие от 9-slice рамки диалога."""

        def __init__(self, width, height, border=5, c1=(33, 212, 246), c2=(253, 100, 186),
                     fill=(10, 12, 26, 235), **kwargs):
            super(GradientPanelDisplayable, self).__init__(**kwargs)
            self.w = width
            self.h = height
            self.border = border
            self.c1 = c1
            self.c2 = c2
            self.fill = fill

        def _lerp(self, t):
            return tuple(int(self.c1[i] + (self.c2[i] - self.c1[i]) * t) for i in range(3))

        def render(self, width, height, st, at):
            r = renpy.Render(self.w, self.h)
            canvas = r.canvas()

            canvas.rect(self.fill, (0, 0, self.w, self.h))

            steps = max(self.w, self.h)
            b = self.border

            for i in range(steps):
                t = i / float(steps - 1) if steps > 1 else 0
                color = self._lerp(t)

                x = int(i * self.w / float(steps))
                x2 = int((i + 1) * self.w / float(steps)) + 1
                canvas.rect(color, (x, 0, x2 - x, b))
                canvas.rect(color, (x, self.h - b, x2 - x, b))

                y = int(i * self.h / float(steps))
                y2 = int((i + 1) * self.h / float(steps)) + 1
                canvas.rect(color, (0, y, b, y2 - y))
                canvas.rect(color, (self.w - b, y, b, y2 - y))

            return r

        def event(self, ev, x, y, st):
            return None


    class GradientBarDisplayable(renpy.Displayable):
        """Ровная горизонтальная градиентная полоска (голубой -> розовый) без резкого стыка цветов."""

        def __init__(self, width, height, c1=(33, 212, 246), c2=(253, 100, 186), **kwargs):
            super(GradientBarDisplayable, self).__init__(**kwargs)
            self.w = width
            self.h = height
            self.c1 = c1
            self.c2 = c2

        def render(self, width, height, st, at):
            r = renpy.Render(self.w, self.h)
            canvas = r.canvas()
            for i in range(self.w):
                t = i / float(self.w - 1) if self.w > 1 else 0
                color = tuple(int(self.c1[k] + (self.c2[k] - self.c1[k]) * t) for k in range(3))
                canvas.rect(color, (i, 0, 1, self.h))
            return r

        def event(self, ev, x, y, st):
            return None


    class WireGame(object):
        """Состояние одного уровня игры "Провода"."""

        def __init__(self, size, endpoints):
            self.size = size
            # endpoints: {"цвет": [(r1, c1), (r2, c2)], ...}
            self.endpoints = endpoints
            self.paths = dict((color, [pts[0]]) for color, pts in endpoints.items())
            self.active_color = None

        def _adjacent(self, a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1

        def cell_owner(self, pos, exclude=None):
            for color, path in self.paths.items():
                if color == exclude:
                    continue
                if pos in path:
                    return color
            return None

        def endpoint_color(self, pos):
            for color, pts in self.endpoints.items():
                if pos in pts:
                    return color
            return None

        def start_drag(self, pos):
            end_color = self.endpoint_color(pos)
            if end_color is None:
                return False

            path = self.paths[end_color]
            if pos in path:
                idx = path.index(pos)
                self.paths[end_color] = path[:idx + 1]
            else:
                # Тянуть можно с любой из двух точек цвета, не только с первой.
                self.paths[end_color] = [pos]
            self.active_color = end_color
            return True

        def drag_to(self, pos):
            if self.active_color is None:
                return

            path = self.paths[self.active_color]

            if pos in path:
                idx = path.index(pos)
                self.paths[self.active_color] = path[:idx + 1]
                return

            if not self._adjacent(path[-1], pos):
                return

            other_color = self.endpoint_color(pos)
            if other_color is not None and other_color != self.active_color:
                return

            if self.cell_owner(pos) is None:
                path.append(pos)

        def end_drag(self):
            self.active_color = None

        def reset(self):
            self.paths = dict((color, [pts[0]]) for color, pts in self.endpoints.items())
            self.active_color = None

        def is_color_done(self, color):
            path = self.paths[color]
            if len(path) < 2:
                return False
            a, b = self.endpoints[color]
            return (path[0] == a and path[-1] == b) or (path[0] == b and path[-1] == a)

        def all_cells_filled(self):
            filled = set()
            for path in self.paths.values():
                filled.update(path)
            return len(filled) == self.size * self.size

        def is_solved(self):
            return self.all_cells_filled() and all(self.is_color_done(c) for c in self.endpoints)

        def cell_color(self, pos):
            return self.cell_owner(pos)

        def is_endpoint(self, pos):
            return self.endpoint_color(pos) is not None


    class WireGameDisplayable(renpy.Displayable):
        """Кастомный дисплеймбл: рисует сетку и обрабатывает протяжку мышью."""

        def __init__(self, game, cell_size=108, gap=8, **kwargs):
            super(WireGameDisplayable, self).__init__(**kwargs)
            self.game = game
            self.cell_size = cell_size
            self.gap = gap
            self.dragging = False

        def _total(self):
            return self.game.size * self.cell_size + (self.game.size - 1) * self.gap

        def _center(self, pos):
            row, col = pos
            step = self.cell_size + self.gap
            return (col * step + self.cell_size // 2, row * step + self.cell_size // 2)

        def render(self, width, height, st, at):
            total = self._total()
            r = renpy.Render(total, total)
            canvas = r.canvas()

            canvas.rect((20, 22, 31), (0, 0, total, total))

            step = self.cell_size + self.gap
            grid_color = (43, 46, 64)
            for i in range(self.game.size + 1):
                pos = 0 if i == 0 else (total if i == self.game.size else i * step - self.gap // 2)
                canvas.line(grid_color, (pos, 0), (pos, total), 2)
                canvas.line(grid_color, (0, pos), (total, pos), 2)

            line_width = int(self.cell_size * 0.4)
            joint_radius = line_width // 2
            dot_radius = int(self.cell_size * 0.38)
            outline = (12, 14, 24)
            outline_w = 3

            # Линии-"трубы" протянутых проводов с тонкой тёмной окантовкой для чёткости.
            for color, path in self.game.paths.items():
                rgb = wire_colors[color]
                for i in range(len(path) - 1):
                    a = self._center(path[i])
                    b = self._center(path[i + 1])
                    canvas.line(outline, a, b, line_width + outline_w * 2)
                for pos in path:
                    canvas.circle(outline, self._center(pos), joint_radius + outline_w)

                for i in range(len(path) - 1):
                    a = self._center(path[i])
                    b = self._center(path[i + 1])
                    canvas.line(rgb, a, b, line_width)
                for pos in path:
                    canvas.circle(rgb, self._center(pos), joint_radius)

            # Точки-концы всегда видны поверх линий, даже пока провод не протянут.
            for color, pts in self.game.endpoints.items():
                rgb = wire_colors[color]
                for pos in pts:
                    canvas.circle(outline, self._center(pos), dot_radius + outline_w)
                    canvas.circle(rgb, self._center(pos), dot_radius)

            return r

        def event(self, ev, x, y, st):
            total = self._total()
            cell_total = self.cell_size + self.gap

            if x < 0 or y < 0 or x >= total or y >= total:
                if self.dragging and ev.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                    self.game.end_drag()
                    renpy.redraw(self, 0)
                    renpy.restart_interaction()
                return None

            col = int(x // cell_total)
            row = int(y // cell_total)
            pos = (row, col)

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.game.start_drag(pos):
                    self.dragging = True
                    renpy.redraw(self, 0)
                    raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.MOUSEMOTION and self.dragging:
                self.game.drag_to(pos)
                renpy.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 and self.dragging:
                self.dragging = False
                self.game.end_drag()
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.display.core.IgnoreEvent()

            return None


screen wire_game_screen(level, round_num=1, round_total=1):
    modal True

    default game = WireGame(level["size"], level["endpoints"])
    default wire_display = WireGameDisplayable(game)

    default panel_w = 1320
    default panel_h = 1060

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 22

            text "СОЕДИНИ ПРОВОДА ОДНОГО ЦВЕТА":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            if round_total > 1:
                text "Раунд [round_num] из [round_total]":
                    font "fonts/TschicholdBold.ttf"
                    size 22
                    color "#39d6e0"
                    xalign 0.5

            text "Зажми точку и веди мышью до второй точки того же цвета — нужно заполнить все клетки поля":
                font "fonts/TschicholdBold.ttf"
                size 24
                color "#9aa0b4"
                xalign 0.5

            add wire_display xalign 0.5

            hbox:
                spacing 40
                xalign 0.5

                use wire_game_button("Сброс", [Function(game.reset), Function(renpy.redraw, wire_display, 0.0)])

    if game.is_solved():
        timer 0.6 action Return(True)


screen wire_game_button(label, act):
    vbox:
        xsize 260
        spacing 0

        textbutton label:
            background "#14191ee0"
            hover_background "#232840f0"
            padding (26, 16)
            xsize 260
            text_font "fonts/TschicholdBold.ttf"
            text_size 28
            text_color "#e0e4ec"
            text_hover_color "#ffffff"
            text_xalign 0.5
            text_yalign 0.5
            action act

        add GradientBarDisplayable(260, 4)


label wire_game_rounds(total=3):
    $ wire_round_total = total
    $ wire_round = 1

label wire_game_round_loop:
    $ wire_level = generate_wire_level()
    call screen wire_game_screen(wire_level, wire_round, wire_round_total)
    $ wire_round += 1
    if wire_round <= wire_round_total:
        jump wire_game_round_loop
    return _return


label wire_game_demo:
    call wire_game_rounds from _call_wire_game_rounds_1

    if _return:
        "Решено! Все провода соединены правильно."
    return
