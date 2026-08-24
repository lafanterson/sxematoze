# Мини-игра "Змейка" (мытьё пола) для сцены с официанткой в кофейне.
# Мокрая дорожка от швабры ползёт по сетке пола, "поедая" грязные пятна и удлиняясь.
# Управление: стрелки или WASD, менять направление можно только не на 180 градусов.
#
# Проигрыш - когда змейка врезается в СВОЁ ТЕКУЩЕЕ ТЕЛО (хвост) или в стену: раунд
# останавливается, на экране на секунду-полторы показывается "Попробуйте снова", после
# чего игра полностью перезапускается (свежая грязь, змейка, счётчик очищенного,
# таймер) - без ограничения по числу попыток. Уже вымытые клетки пола (floor_cleaned)
# - чисто декоративный слой, наступать на них можно свободно, коллизия проверяется
# только против текущего тела змейки.
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump floor_cleaning_demo
#
# Использует общие декоративные дисплеймблы (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:
    import pygame

init python:

    class SnakeGame(object):
        """Состояние раунда мытья пола: сетка, змейка-дорожка, грязные пятна, таймер."""

        def __init__(self, duration=50.0, dirt_count=12, cols=16, rows=11, cell_size=42, gap=3):
            self.cols = cols
            self.rows = rows
            self.cell_size = cell_size
            self.gap = gap
            self.width = cols * cell_size + (cols - 1) * gap
            self.height = rows * cell_size + (rows - 1) * gap

            self.dirt_count = dirt_count
            self.duration = duration

            self.base_tick_interval = 0.16
            self.min_tick_interval = 0.09

            self.fails = 0

            self._full_restart()

        def _free_cell(self):
            occupied = set(self.snake) | self.dirt
            free = [
                (r, c)
                for r in range(self.rows)
                for c in range(self.cols)
                if (r, c) not in occupied
            ]
            if not free:
                return None
            return free[renpy.random.randint(0, len(free) - 1)]

        def _full_restart(self):
            """Свежий старт раунда: новая грязь, змейка, счётчик, таймер. Не трогает
            self.fails - это счётчик за весь сеанс игры, а не за одну попытку."""
            start_row = self.rows // 2
            self.start_snake = [(start_row, 5), (start_row, 4), (start_row, 3)]
            self.snake = list(self.start_snake)
            self.direction = (0, 1)
            self.pending_dir = (0, 1)

            self.tick_interval = self.base_tick_interval
            self.tick_acc = 0.0

            self.dirt = set()
            for _i in range(self.dirt_count):
                spot = self._free_cell()
                if spot is not None:
                    self.dirt.add(spot)
            self.total_dirt = len(self.dirt)

            self.floor_cleaned = set(self.snake)

            self.time_left = self.duration
            self.cleaned_count = 0

            self.state = "playing"  # "playing" -> "failed" (пауза с сообщением) -> "playing"
            self.message = None
            self.message_timer = 0.0

            self.finished = False

        def queue_direction(self, new_dir):
            if self.finished or self.state == "failed":
                return
            opposite = (-self.direction[0], -self.direction[1])
            if new_dir != opposite:
                self.pending_dir = new_dir

        def _fail(self):
            self.fails += 1
            self.state = "failed"
            self.message = "Попробуйте снова"
            self.message_timer = 1.4
            renpy.play("audio/false_answer.wav")

        def _step(self):
            self.direction = self.pending_dir
            head_r, head_c = self.snake[0]
            dr, dc = self.direction
            new_head = (head_r + dr, head_c + dc)

            if not (0 <= new_head[0] < self.rows and 0 <= new_head[1] < self.cols):
                self._fail()
                return

            will_grow = new_head in self.dirt
            body_to_check = self.snake if will_grow else self.snake[:-1]

            if new_head in body_to_check:
                self._fail()
                return

            self.snake.insert(0, new_head)
            if will_grow:
                self.dirt.discard(new_head)
                self.cleaned_count += 1
                renpy.play("audio/water_in_a_bucket.wav")
            else:
                self.snake.pop()

            self.floor_cleaned.update(self.snake)

            self.tick_interval = max(
                self.min_tick_interval,
                self.base_tick_interval - self.cleaned_count * 0.004,
            )

            if self.cleaned_count >= self.total_dirt:
                self.finished = True

        def update(self, dt):
            if self.finished:
                return

            if self.state == "failed":
                self.message_timer -= dt
                if self.message_timer <= 0:
                    self._full_restart()
                return

            self.time_left -= dt
            if self.time_left <= 0:
                self.finished = True
                return

            self.tick_acc += dt
            guard = 0
            while self.tick_acc >= self.tick_interval and self.state == "playing" and not self.finished and guard < 5:
                self.tick_acc -= self.tick_interval
                self._step()
                guard += 1

        def result(self):
            return {
                "cleaned": self.cleaned_count,
                "total": self.total_dirt,
                "fails": self.fails,
                "completed": self.cleaned_count >= self.total_dirt,
            }


    class SnakeGameDisplayable(renpy.Displayable):
        """Рисует сетку пола, грязные пятна и мокрую дорожку-змейку; тикает игру через st."""

        def __init__(self, game, **kwargs):
            super(SnakeGameDisplayable, self).__init__(**kwargs)
            self.game = game
            self.last_st = None

        def render(self, width, height, st, at):
            dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
            self.last_st = st
            self.game.update(dt)

            w, h = self.game.width, self.game.height
            r = renpy.Render(w, h)
            canvas = r.canvas()

            cs = self.game.cell_size
            gap = self.game.gap
            step = cs + gap

            canvas.rect((26, 20, 16), (0, 0, w, h))

            for (row, col) in self.game.floor_cleaned:
                x = col * step
                y = row * step
                canvas.rect((58, 52, 40), (x, y, cs, cs))

            grid_color = (40, 36, 30)
            for col in range(self.game.cols + 1):
                x = 0 if col == 0 else (w if col == self.game.cols else col * step - gap // 2)
                canvas.line(grid_color, (x, 0), (x, h), 1)
            for row in range(self.game.rows + 1):
                y = 0 if row == 0 else (h if row == self.game.rows else row * step - gap // 2)
                canvas.line(grid_color, (0, y), (w, y), 1)

            for (row, col) in self.game.dirt:
                cx = col * step + cs // 2
                cy = row * step + cs // 2
                canvas.circle((94, 66, 40), (cx, cy), int(cs * 0.28))
                canvas.circle((124, 90, 54), (cx, cy), int(cs * 0.16))

            outline = (10, 14, 20)
            body_color = (58, 150, 214)
            head_color = (120, 210, 255)
            if self.game.state == "failed":
                body_color = (214, 90, 70)
                head_color = (255, 130, 100)
            for i, (row, col) in enumerate(self.game.snake):
                x = col * step
                y = row * step
                color = head_color if i == 0 else body_color
                canvas.rect(outline, (x - 1, y - 1, cs + 2, cs + 2))
                canvas.rect(color, (x + 2, y + 2, cs - 4, cs - 4))

            if self.game.finished:
                pass
            elif self.game.state == "failed":
                renpy.redraw(self, 0)
            else:
                wait = self.game.tick_interval - self.game.tick_acc
                renpy.redraw(self, max(0.0, wait))

            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                new_dir = None
                if ev.key in (pygame.K_UP, pygame.K_w):
                    new_dir = (-1, 0)
                elif ev.key in (pygame.K_DOWN, pygame.K_s):
                    new_dir = (1, 0)
                elif ev.key in (pygame.K_LEFT, pygame.K_a):
                    new_dir = (0, -1)
                elif ev.key in (pygame.K_RIGHT, pygame.K_d):
                    new_dir = (0, 1)

                if new_dir is not None:
                    self.game.queue_direction(new_dir)
                    raise renpy.display.core.IgnoreEvent()

            return None


screen floor_cleaning_screen(duration=50.0):
    modal True

    default game = SnakeGame(duration)
    default snake_display = SnakeGameDisplayable(game)

    default panel_w = 1000
    default panel_h = 860

    # Как и в fishing_game_screen: анимация дорожки идёт через renpy.redraw() у
    # snake_display, но HUD-текст и "if game.finished:" ниже - это язык экранов,
    # он пересчитывается только при restart_interaction.
    timer 0.1 repeat True action Function(renpy.restart_interaction)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "ВЫМОЙ ПОЛ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Стрелки или WASD — веди мокрую дорожку по грязным пятнам, не наступай на свой хвост":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5
                xsize 760
                text_align 0.5

            hbox:
                spacing 50
                xalign 0.5

                text "Грязи убрано: [game.cleaned_count]/[game.total_dirt]" font "fonts/TschicholdBold.ttf" size 24 color "#e0e4ec"
                text "Осечек: [game.fails]" font "fonts/TschicholdBold.ttf" size 24 color "#ff9a8c"
                text "Время: [int(max(0, game.time_left))]" font "fonts/TschicholdBold.ttf" size 24 color "#f2d43c"

            if game.message:
                text "[game.message]":
                    font "fonts/TschicholdBold.ttf"
                    size 26
                    color "#ff5a4a"
                    xalign 0.5
            else:
                text " " size 26 xalign 0.5

            add snake_display xalign 0.5

    if game.finished:
        timer 1.2 action Return(game.result())


label floor_cleaning_demo:
    call screen floor_cleaning_screen

    $ floor_result = _return
    if floor_result["completed"]:
        "Пол вымыт полностью! Осечек: [floor_result['fails']]."
    else:
        "Время вышло. Вымыто [floor_result['cleaned']] из [floor_result['total']] пятен, осечек: [floor_result['fails']]."
    return
