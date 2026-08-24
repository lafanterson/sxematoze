# Мини-игра "Гайки на болтах" (Ball/Nuts Sort Puzzle) - головоломка на сортировку по
# цвету. Кликни болт с гайками - верхняя однотонная группа "поднимается" (подсветка),
# кликни другой болт - группа переезжает туда, если он пуст или сверху там гайка того
# же цвета и есть место. Цель - развести гайки так, чтобы на каждом болте лежали гайки
# только одного цвета. Усложнённая раскладка: 6 цветов, вместимость 4, но всего 2
# ПУСТЫХ болта-буфера (классическая "трудная" конфигурация - меньше свободного места
# для манёвра). Головоломка генерируется от решённого состояния случайными обратимыми
# ходами, поэтому всегда решаема.
#
# Как и wire_game.rpy - обычный canvas-дисплеймбл с кликами (не drag), без непрерывной
# анимации: renpy.restart_interaction() после каждого клика обновляет HUD-текст.
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump bolt_sort_demo
#
# Использует общие декоративные дисплеймблы (GradientPanelDisplayable) и палитру
# wire_colors из wire_game.rpy - все .rpy файлы в game/ делят один общий
# Python/screen-неймспейс.

init python:
    import pygame
    import math

init python:

    BOLT_SORT_COLOR_KEYS = ["red", "blue", "green", "yellow", "purple", "orange"]

    class BoltSortGame(object):
        def __init__(self, colors=None, capacity=4, empty_count=2, shuffle_moves=400):
            self.colors = colors if colors is not None else list(BOLT_SORT_COLOR_KEYS)
            self.capacity = capacity
            self.empty_count = empty_count
            self.shuffle_moves = shuffle_moves

            self.selected = None
            self.moves = 0

            # Геометрия сетки болтов - считается один раз, используется и для отрисовки,
            # и для попадания кликом.
            self.cols = 4
            self.col_w = 150
            self.row_h = 280
            self.margin_x = 70
            self.margin_y = 40
            self.slot_h = capacity * 46 + 50

            self._reset_bolts()

            n = len(self.bolts)
            self.width = self.margin_x * 2 + self.cols * self.col_w
            rows = (n + self.cols - 1) // self.cols
            self.height = self.margin_y * 2 + rows * self.row_h

            self.positions = []
            for i in range(n):
                col = i % self.cols
                row = i // self.cols
                x = self.margin_x + col * self.col_w + self.col_w // 2
                y = self.margin_y + row * self.row_h
                self.positions.append((x, y))

        def _reset_bolts(self):
            self.bolts = []
            for c in self.colors:
                self.bolts.append([c] * self.capacity)
            for _i in range(self.empty_count):
                self.bolts.append([])

            # На случайном блуждании иногда (редко) возвращаемся обратно в решённое
            # состояние - на такой случай перемешиваем ещё раз.
            guard = 0
            self._shuffle(self.shuffle_moves)
            while self.is_solved() and guard < 10:
                self._shuffle(self.shuffle_moves)
                guard += 1

            self.selected = None
            self.moves = 0

        def _top_run(self, bolt):
            if not bolt:
                return None, 0
            color = bolt[-1]
            length = 0
            for c in reversed(bolt):
                if c == color:
                    length += 1
                else:
                    break
            return color, length

        def _can_move_raw(self, src_idx, dst_idx):
            if src_idx == dst_idx:
                return False
            src = self.bolts[src_idx]
            dst = self.bolts[dst_idx]
            if not src:
                return False
            if len(dst) >= self.capacity:
                return False
            color, _length = self._top_run(src)
            if dst and dst[-1] != color:
                return False
            return True

        def _move_raw(self, src_idx, dst_idx):
            src = self.bolts[src_idx]
            dst = self.bolts[dst_idx]
            color, length = self._top_run(src)
            free = self.capacity - len(dst)
            move_count = min(length, free)
            moving = src[-move_count:]
            del src[-move_count:]
            dst.extend(moving)

        def _shuffle(self, count):
            """Раскладка строится от решённого состояния случайными ОБРАТНЫМИ ходами:
            берём часть верхнего однотонного столбика (не обязательно весь) и переносим
            на любой болт, где есть место - БЕЗ требования совпадения цвета сверху (это
            правило только для игровых ходов, не для генерации).

            Важно: если бы генерация использовала те же правила, что и игровые ходы
            (перенос только на пустой/совпадающий по цвету болт), с решённого состояния
            каждый болт целиком одноцветный, поэтому "верхний столбик" - это всегда весь
            болт целиком, а значит такие ходы могут только переставлять целые болты
            местами и никогда не перемешивают цвета внутри болта - раскладка гарантированно
            остаётся псевдо-решённой. Обратный ход без проверки цвета получателя лишён
            этой проблемы и всё равно гарантированно обратим: если проигрывать сделанные
            ходы в точности в обратном порядке, verхний слой на приёмнике на момент
            "отмены" - это ровно те элементы, что мы туда положили, а верхний слой на
            источнике после их извлечения - либо пусто, либо тот же цвет (кусок того же
            столбика), так что настоящий игровой ход всегда может их отыграть назад."""
            n = len(self.bolts)
            done = 0
            tries = 0
            while done < count and tries < count * 30:
                tries += 1
                src = renpy.random.randint(0, n - 1)
                if not self.bolts[src]:
                    continue
                _color, length = self._top_run(self.bolts[src])
                k = renpy.random.randint(1, length)
                dst = renpy.random.randint(0, n - 1)
                if dst == src:
                    continue
                if len(self.bolts[dst]) + k > self.capacity:
                    continue
                moving = self.bolts[src][-k:]
                del self.bolts[src][-k:]
                self.bolts[dst].extend(moving)
                done += 1

        def is_solved(self):
            for bolt in self.bolts:
                if not bolt:
                    continue
                if len(bolt) != self.capacity:
                    return False
                if any(c != bolt[0] for c in bolt):
                    return False
            return True

        def select(self, idx):
            if self.is_solved():
                return

            if self.selected is None:
                if self.bolts[idx]:
                    self.selected = idx
                return

            if self.selected == idx:
                self.selected = None
                return

            if self._can_move_raw(self.selected, idx):
                self._move_raw(self.selected, idx)
                self.moves += 1
                if self.is_solved():
                    renpy.play("audio/true_answer.wav")
            else:
                renpy.play("audio/false_answer.wav")

            self.selected = None

        def reshuffle(self):
            self._reset_bolts()

        def result(self):
            return {"moves": self.moves, "solved": self.is_solved()}


    class BoltSortDisplayable(renpy.Displayable):
        """Рисует сетку болтов с гайками; обрабатывает клики (не drag)."""

        def __init__(self, game, **kwargs):
            super(BoltSortDisplayable, self).__init__(**kwargs)
            self.game = game

        def _draw_nut(self, canvas, color_key, cx, cy, w, h):
            color = wire_colors[color_key]
            outline = (15, 12, 10)
            r = w // 2 - 4
            half_h = h * 0.42

            pts_outer = []
            for k in range(6):
                ang = math.pi / 6 + k * math.pi / 3
                pts_outer.append((cx + math.cos(ang) * r, cy + math.sin(ang) * half_h))

            canvas.polygon(outline, pts_outer)
            pts_inner = [(cx + (px - cx) * 0.84, cy + (py - cy) * 0.84) for px, py in pts_outer]
            canvas.polygon(color, pts_inner)

            hole_r = int(h * 0.16) + 2
            canvas.circle(outline, (int(cx), int(cy)), hole_r)
            canvas.circle((205, 205, 210), (int(cx), int(cy)), hole_r - 3)

        def _draw_bolt(self, canvas, bolt, x, top_y, selected):
            pole_w = 16
            nut_h = 46
            nut_w = 104
            slot_h = self.game.slot_h
            base_y = top_y + slot_h - 14

            outline = (15, 12, 10)

            canvas.rect(outline, (x - pole_w // 2 - 2, top_y, pole_w + 4, slot_h - 6))
            canvas.rect((152, 152, 160), (x - pole_w // 2, top_y, pole_w, slot_h - 6))
            for yy in range(top_y + 8, base_y, 9):
                canvas.line((112, 112, 120), (x - pole_w // 2, yy), (x + pole_w // 2, yy), 1)

            canvas.rect(outline, (x - nut_w // 2 - 6, base_y + 4, nut_w + 12, 16))
            canvas.rect((90, 90, 96), (x - nut_w // 2 - 3, base_y + 6, nut_w + 6, 11))

            if selected:
                canvas.rect(
                    (250, 220, 80),
                    (x - nut_w // 2 - 8, top_y - 8, nut_w + 16, slot_h + 16),
                    3,
                )

            for i, color_key in enumerate(bolt):
                cy = base_y - i * nut_h - nut_h // 2
                self._draw_nut(canvas, color_key, x, cy, nut_w, nut_h)

        def render(self, width, height, st, at):
            w, h = self.game.width, self.game.height
            r = renpy.Render(w, h)
            canvas = r.canvas()

            canvas.rect((26, 20, 34), (0, 0, w, h))

            for i, bolt in enumerate(self.game.bolts):
                x, y = self.game.positions[i]
                self._draw_bolt(canvas, bolt, x, y, i == self.game.selected)

            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                nut_w = 104
                for i, (bx, by) in enumerate(self.game.positions):
                    if (bx - nut_w // 2 - 10) <= x <= (bx + nut_w // 2 + 10) and by - 10 <= y <= by + self.game.slot_h + 10:
                        self.game.select(i)
                        renpy.redraw(self, 0)
                        renpy.restart_interaction()
                        raise renpy.display.core.IgnoreEvent()

            return None


screen bolt_sort_screen():
    modal True

    default game = BoltSortGame()
    default bolt_display = BoltSortDisplayable(game)

    default panel_w = game.width + 100
    default panel_h = game.height + 260

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            text "РАЗБЕРИ ГАЙКИ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Клик по болту снимает верхнюю группу гаек, клик по другому - переносит её":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5

            hbox:
                spacing 40
                xalign 0.5

                text "Ходов: [game.moves]" font "fonts/TschicholdBold.ttf" size 24 color "#e0e4ec"

                if game.is_solved():
                    text "Решено!" font "fonts/TschicholdBold.ttf" size 24 color "#4ee08a"

            add bolt_display xalign 0.5

            use wire_game_button("Новая головоломка", [Function(game.reshuffle), Function(renpy.redraw, bolt_display, 0.0)])

    if game.is_solved():
        timer 1.0 action Return(game.result())


label bolt_sort_demo:
    call screen bolt_sort_screen

    $ bolt_result = _return
    "Решено за [bolt_result['moves']] ходов."
    return
