# Мини-игра "Дженга" - одиночная, символическая. Вставляется в сцену, где Маша уходит
# от Тёмщика (пирамида-мошенника): пока переводит дух, от нечего делать тянет бруски из
# забытой кем-то башни. Смысл в том, что башня ГАРАНТИРОВАННО рухнет рано или поздно,
# сколько бы брусков ни вытянули аккуратно - отсылка к тому, что финансовая пирамида
# тоже неизбежно рушится. С каждым вытянутым бруском шанс обрушения растёт (чуть выше
# для брусков из нижних рядов), и даже если бы игрок каким-то чудом вытянул все
# доступные бруски без обрушения - башня всё равно падает принудительно, как только
# тянуть больше нечего. Верхние 2 ряда трогать нельзя (как в настоящей дженге).
#
# Как и bolt_sort_game.rpy/wire_game.rpy - обычный canvas-дисплеймбл с кликами.
# Постоянная перерисовка нужна только во время анимации обрушения; в остальное время
# редрав идёт только по клику (renpy.restart_interaction() обновляет HUD-текст).
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump jenga_game_demo
#
# Использует общий декоративный дисплеймбл (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:
    import pygame

init python:

    class JengaGame(object):
        def __init__(self, layers=12, width=420, layer_h=24, protected_layers=2):
            self.layers = layers
            self.width = width
            self.layer_h = layer_h
            self.height = layers * layer_h + 30
            self.protected_layers = protected_layers

            self.blocks = {}
            for l in range(layers):
                for s in range(3):
                    self.blocks[(l, s)] = True

            self.pulled = 0
            self.collapsed = False
            self.collapse_time = 0.0
            self.collapse_duration = 1.6
            self.finished = False
            self.fall_vectors = {}

        def is_pullable_layer(self, layer):
            return 0 <= layer < self.layers - self.protected_layers

        def _any_pullable_left(self):
            for (l, s), present in self.blocks.items():
                if present and self.is_pullable_layer(l):
                    return True
            return False

        def try_pull(self, layer, slot):
            if self.collapsed or self.finished:
                return
            if not self.blocks.get((layer, slot), False):
                return
            if not self.is_pullable_layer(layer):
                renpy.play("audio/false_answer.wav")
                return

            self.blocks[(layer, slot)] = False
            self.pulled += 1
            renpy.play("audio/mouse_click_2.wav")

            depth_bonus = (self.layers - self.protected_layers - 1 - layer) * 0.0015
            chance = min(0.9, 0.015 + self.pulled * 0.011 + depth_bonus)

            if renpy.random.random() < chance or not self._any_pullable_left():
                self._start_collapse()

        def _start_collapse(self):
            self.collapsed = True
            self.collapse_time = 0.0
            for pos, present in self.blocks.items():
                if present:
                    dx = renpy.random.uniform(-140, 140)
                    dy = renpy.random.uniform(220, 380)
                    self.fall_vectors[pos] = (dx, dy)
            renpy.play("audio/false_answer.wav")

        def update(self, dt):
            if self.collapsed and not self.finished:
                self.collapse_time += dt
                if self.collapse_time >= self.collapse_duration:
                    self.finished = True

        def result(self):
            return {"pulled": self.pulled}


    class JengaDisplayable(renpy.Displayable):
        """Рисует башню из брусков; клик по бруску снизу вытягивает его."""

        def __init__(self, game, **kwargs):
            super(JengaDisplayable, self).__init__(**kwargs)
            self.game = game
            self.last_st = None

        def _block_rect(self, layer, slot):
            g = self.game
            block_w = g.width // 3
            x = slot * block_w
            y = g.height - 16 - (layer + 1) * g.layer_h
            return x, y, block_w, g.layer_h

        def render(self, width, height, st, at):
            dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
            self.last_st = st
            self.game.update(dt)

            g = self.game
            r = renpy.Render(g.width, g.height)
            canvas = r.canvas()

            canvas.rect((24, 18, 14), (0, 0, g.width, g.height))
            canvas.rect((60, 40, 26), (0, g.height - 12, g.width, 12))

            outline = (18, 12, 8)
            removed_below = 0

            for layer in range(g.layers):
                lean = 0 if g.collapsed else int(removed_below * 1.4)
                shade = (168, 122, 74) if layer % 2 == 0 else (140, 100, 60)
                layer_removed = 0

                for slot in range(3):
                    present = g.blocks[(layer, slot)]
                    x, y, bw, bh = self._block_rect(layer, slot)

                    if not present:
                        layer_removed += 1
                        if not g.collapsed:
                            x += lean
                            canvas.rect((10, 8, 6), (x + 4, y + 4, bw - 12, bh - 6))
                        continue

                    if g.collapsed:
                        dx, dy = g.fall_vectors.get((layer, slot), (0, 0))
                        t = min(1.0, g.collapse_time / g.collapse_duration)
                        ease = t * t
                        fx = int(x + dx * ease)
                        fy = int(y + dy * ease)
                        canvas.rect(outline, (fx - 2, fy - 2, bw + 2, bh + 2))
                        canvas.rect(shade, (fx, fy, bw - 4, bh - 4))
                        continue

                    x += lean
                    pullable = g.is_pullable_layer(layer)
                    col = shade if pullable else (90, 70, 48)
                    canvas.rect(outline, (x + 2, y + 1, bw - 4, bh - 2))
                    canvas.rect(col, (x + 4, y + 3, bw - 8, bh - 6))

                removed_below += layer_removed

            if not g.finished:
                renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            g = self.game
            if g.collapsed or g.finished:
                return None

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for layer in range(g.layers):
                    for slot in range(3):
                        if not g.blocks[(layer, slot)]:
                            continue
                        bx, by, bw, bh = self._block_rect(layer, slot)
                        if bx <= x <= bx + bw and by <= y <= by + bh:
                            g.try_pull(layer, slot)
                            renpy.redraw(self, 0)
                            renpy.restart_interaction()
                            raise renpy.display.core.IgnoreEvent()

            return None


screen jenga_game_screen():
    modal True

    default game = JengaGame()
    default jenga_display = JengaDisplayable(game)

    default panel_w = game.width + 160
    default panel_h = game.height + 220

    # Пока башня обрушается, кликов больше нет (пуллы заблокированы), поэтому
    # restart_interaction() из event() не вызывается - без периодического пинка экран
    # никогда не заметит, что game.finished стало True, и "call screen" зависнет
    # навсегда. Тот же приём, что в fishing_game_screen/floor_cleaning_screen.
    timer 0.1 repeat True action Function(renpy.restart_interaction)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            text "ДЖЕНГА":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Клик по бруску — вытянуть. Верхние два ряда трогать нельзя.":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5

            text "Вытянуто: [game.pulled]":
                font "fonts/TschicholdBold.ttf"
                size 24
                color "#e0e4ec"
                xalign 0.5

            add jenga_display xalign 0.5

            if game.collapsed:
                text "БАШНЯ РУХНУЛА":
                    font "fonts/TschicholdBold.ttf"
                    size 30
                    color "#e6483c"
                    xalign 0.5
            else:
                text " " size 30 xalign 0.5

    if game.finished:
        timer 1.2 action Return(game.result())


label jenga_game_demo:
    call screen jenga_game_screen

    $ jenga_result = _return
    "Вытянуто блоков: [jenga_result['pulled']]. Башня рухнула — как и всегда."
    return
