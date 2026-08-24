# Мини-игра "Собери ссылку" (падающие блоки по дорожкам) для сцены с Анти в торговом
# центре. Три дорожки - протокол / домен / зона-и-путь - активны по очереди: пока не
# поймаешь правильный блок в текущей, следующая не начинает падать. В активной дорожке
# по очереди падают то настоящие, то похожие поддельные блоки; единая клавиша (пробел
# или клик) ловит блок, если он сейчас в подсвеченной зоне внизу. Мимо - блок просто
# летит дальше и позже вернётся в цикле; поймал не тот - засчитывается ошибка, дорожка
# не блокируется.
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump link_game_demo
#
# Использует общие декоративные дисплеймблы (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:
    import pygame

init python:

    class LinkPiece(object):
        def __init__(self, label, correct):
            self.label = label
            self.correct = correct


    class LinkLane(object):
        """Одна дорожка: очередь блоков (зациклена, пока не поймают правильный)."""

        def __init__(self, title, correct_label, decoy_labels, lane_height, fall_duration=4.6):
            self.title = title
            self.correct_label = correct_label
            self.lane_height = lane_height
            self.fall_duration = fall_duration

            pieces = [LinkPiece(correct_label, True)]
            for d in decoy_labels:
                pieces.append(LinkPiece(d, False))
            renpy.random.shuffle(pieces)
            self.pieces = pieces
            self.next_index = 0

            self.falling = None
            self.falling_y = 0.0
            self.spawn_cooldown = renpy.random.uniform(0.2, 0.8)

            self.solved = False
            self.mistakes = 0
            self.flash = None
            self.flash_timer = 0.0

        def _spawn_next(self):
            if self.next_index >= len(self.pieces):
                self.next_index = 0
                renpy.random.shuffle(self.pieces)
            self.falling = self.pieces[self.next_index]
            self.next_index += 1
            self.falling_y = 0.0

        def update(self, dt):
            if self.solved:
                return

            if self.flash_timer > 0:
                self.flash_timer = max(0.0, self.flash_timer - dt)
                if self.flash_timer == 0.0:
                    self.flash = None

            if self.falling is None:
                self.spawn_cooldown -= dt
                if self.spawn_cooldown <= 0:
                    self._spawn_next()
                return

            self.falling_y += (self.lane_height / self.fall_duration) * dt
            if self.falling_y >= self.lane_height:
                self.falling = None
                self.spawn_cooldown = 0.4

        def try_catch(self):
            if self.solved or self.falling is None:
                return

            zone_lo = self.lane_height * 0.50
            zone_hi = self.lane_height * 0.92
            if not (zone_lo <= self.falling_y <= zone_hi):
                return

            if self.falling.correct:
                self.solved = True
                self.falling = None
                self.flash = "correct"
                self.flash_timer = 1.0
                renpy.play("audio/true_answer.wav")
            else:
                self.mistakes += 1
                self.falling = None
                self.spawn_cooldown = 0.4
                self.flash = "wrong"
                self.flash_timer = 0.5
                renpy.play("audio/false_answer.wav")


    class LinkBuilderGame(object):
        def __init__(self, duration=55.0, lane_height=420.0):
            self.lane_height = lane_height
            self.lanes = [
                LinkLane("Протокол", "https://", [
                    "http://", "https:/", "https:///", "https:\\\\", "htps://",
                ], lane_height),
                LinkLane("Домен", "sxematoze", [
                    "vk", "sxematoz-ru", "sxemotoze", "sxematoze1", "sxernatoze",
                ], lane_height),
                LinkLane("Зона и путь", ".ru/maps", [
                    ".com/maps", ".ru.maps", ".ru/map", ".ru/mars", ".ru.info/maps",
                ], lane_height),
            ]
            self.duration = duration
            self.time_left = duration
            self.active_index = 0
            self.finished = False

        def update(self, dt):
            if self.finished:
                return

            self.time_left -= dt
            if self.time_left <= 0:
                self.finished = True
                return

            active_lane = self.lanes[self.active_index]
            active_lane.update(dt)

            if active_lane.solved:
                self.active_index += 1
                if self.active_index >= len(self.lanes):
                    self.finished = True

        def try_catch(self):
            if self.finished:
                return
            self.lanes[self.active_index].try_catch()

        def total_mistakes(self):
            return sum(lane.mistakes for lane in self.lanes)

        def result(self):
            return {
                "solved": all(lane.solved for lane in self.lanes),
                "mistakes": self.total_mistakes(),
            }


    class LinkBuilderTicker(renpy.Displayable):
        """Невидимый "тикер": двигает падающие блоки и ловит нажатия клавиш дорожек."""

        def __init__(self, game, **kwargs):
            super(LinkBuilderTicker, self).__init__(**kwargs)
            self.game = game
            self.last_st = None

        def render(self, width, height, st, at):
            dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
            self.last_st = st
            self.game.update(dt)

            r = renpy.Render(1, 1)
            if not self.game.finished:
                renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self.game.try_catch()
                raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.game.try_catch()
                raise renpy.display.core.IgnoreEvent()

            return None


screen link_lane_display(index, lane, is_active):
    $ lane_w = 260
    $ lane_h = int(lane.lane_height)
    $ zone_lo = int(lane_h * 0.50)
    $ zone_hi = int(lane_h * 0.92)

    $ border_color = "#2b2e40"
    if lane.solved:
        $ border_color = "#4ee08a"
    elif is_active and lane.flash == "correct":
        $ border_color = "#4ee08a"
    elif is_active and lane.flash == "wrong":
        $ border_color = "#e6483c"
    elif is_active:
        $ border_color = "#39d6e0"

    $ title_color = "#5a6070"
    if lane.solved:
        $ title_color = "#4ee08a"
    elif is_active:
        $ title_color = "#9aa0b4"

    vbox:
        xsize lane_w
        spacing 10

        text lane.title:
            font "fonts/TschicholdBold.ttf"
            size 20
            color title_color
            xalign 0.5

        fixed:
            xsize lane_w
            ysize lane_h

            add Solid("#14191ee0") xysize (lane_w, lane_h)

            if is_active and not lane.solved:
                add Solid("#39d6e022") xysize (lane_w, zone_hi - zone_lo) ypos zone_lo

            add Solid(border_color) xysize (lane_w, 3)
            add Solid(border_color) xysize (lane_w, 3) ypos (lane_h - 3)
            add Solid(border_color) xysize (3, lane_h)
            add Solid(border_color) xysize (3, lane_h) xpos (lane_w - 3)

            if lane.solved:
                frame:
                    ypos (lane_h - 76)
                    xsize lane_w
                    background "#1f3a2bd0"
                    padding (10, 16)
                    text lane.correct_label:
                        font "fonts/TschicholdBold.ttf"
                        size 22
                        color "#a8f0c0"
                        xalign 0.5
            elif is_active and lane.falling:
                frame:
                    ypos int(lane.falling_y)
                    xsize lane_w
                    background "#232840f0"
                    padding (10, 14)
                    text lane.falling.label:
                        font "fonts/TschicholdBold.ttf"
                        size 22
                        color "#e0e4ec"
                        xalign 0.5
            elif not is_active:
                text "ожидание...":
                    xalign 0.5
                    yalign 0.5
                    font "fonts/TschicholdBold.ttf"
                    size 18
                    color "#3a3f4d"

        text ("Готово" if lane.solved else ("Сейчас" if is_active else "Далее")):
            font "fonts/TschicholdBold.ttf"
            size 18
            color title_color
            xalign 0.5


screen link_builder_screen(duration=55.0):
    modal True

    default game = LinkBuilderGame(duration)
    default ticker = LinkBuilderTicker(game)

    default panel_w = 1000
    default panel_h = 780

    # Как и в остальных мини-играх: анимация падения идёт через renpy.redraw() у
    # ticker, но HUD-текст и "if game.finished:" ниже - это язык экранов, он
    # пересчитывается только при restart_interaction.
    timer 0.03 repeat True action Function(renpy.restart_interaction)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)
        add ticker

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "СОБЕРИ ССЫЛКУ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Пробел или клик — поймай нужный блок в подсвеченной зоне":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5

            hbox:
                spacing 50
                xalign 0.5

                text "Время: [int(max(0, game.time_left))]" font "fonts/TschicholdBold.ttf" size 24 color "#f2d43c"
                text "Ошибок: [game.total_mistakes()]" font "fonts/TschicholdBold.ttf" size 24 color "#ff9a8c"

            hbox:
                spacing 30
                xalign 0.5

                for i, lane in enumerate(game.lanes):
                    use link_lane_display(i, lane, i == game.active_index)

    if game.finished:
        timer 1.3 action Return(game.result())


label link_game_demo:
    call screen link_builder_screen

    $ link_result = _return
    if link_result["solved"]:
        "Ссылка собрана верно! Ошибок: [link_result['mistakes']]."
    else:
        "Время вышло, собрать успели не всё."
    return
