# Мини-игра "Рыбалка" (в духе Gold Miner) для сцены с Дедушкой-Рыбаком.
# Удочка мерно раскачивается из стороны в сторону. Клик мышью (или пробел) фиксирует
# текущий угол и забрасывает крючок - он летит по прямой, пока не заденет рыбу или не
# долетит до дна, после чего тянется обратно к лодке. Обманщуки (фейкарпы) отмечены
# жёлтой "царапиной" на боку (обрывок ссылки) и тяжелее/дольше вытягиваются, чем
# обычная рыба - зато стоят больше очков.
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump fishing_game_demo
#
# Фон и арт рыб - настоящие иллюстрации дизайнеров (fish_game_view.png,
# good_fish_*.png/bad_fish_*.png в images/), не canvas-примитивы. Плавающие рыбы -
# небольшие карточки без рамки с "cover"-обрезанной иллюстрацией конкретной рыбы
# (картинки не прозрачные и разных пропорций/размеров, поэтому каждая рисуется через
# renpy.render()+Render.blit() с обрезкой по границе карточки, разворачивается по
# горизонтали в сторону движения); жёлтая метка-подсказка у обманщук - поверх
# картинки, в углу карточки. Результат поимки - только текстом (без всплывающей
# карточки с крупным планом).
#
# Использует общие декоративные дисплеймблы (GradientPanelDisplayable, GradientBarDisplayable)
# и стиль кнопки (wire_game_button) из wire_game.rpy - все .rpy файлы в game/ делят один
# общий Python/screen-неймспейс, повторный импорт стилей не нужен.

init python:
    import pygame
    import math

init python:

    # Арт от дизайнеров: обычные рыбы - good_fish_*, обманщуки - bad_fish_* (три и пять
    # штук соответственно, разного разрешения - для каждой сохранён исходный размер,
    # чтобы масштабировать без искажений). Фон - fish_game_view.png (5480x3072).
    FISH_GOOD_IMAGES = [
        ("good_fish_first.png", 1365, 768),
        ("good_fish_second.png", 1376, 768),
        ("good_fish_third.png", 1365, 768),
    ]
    FISH_BAD_IMAGES = [
        ("bad_fish_first.png", 1216, 876),
        ("bad_fish_second.png", 1216, 876),
        ("bad_fish_third.png", 1365, 768),
        ("bad_fish_fourth.png", 1264, 843),
        ("bad_fish_sixth.png", 1024, 1024),
    ]
    FISH_BG_IMAGE = "fish_game_view.png"
    FISH_BG_SRC_W = 5480
    FISH_BG_SRC_H = 3072

    def _cover_scale(path, src_w, src_h, target_w, target_h):
        """im.Scale до размера, покрывающего (target_w, target_h) с сохранением
        пропорций - результат крупнее цели по одной оси, лишнее обрезает контейнер
        (frame/fixed в Ren'Py клипует детей по своим границам по умолчанию)."""
        scale = max(target_w / float(src_w), target_h / float(src_h))
        return im.Scale(path, int(src_w * scale) + 1, int(src_h * scale) + 1)

    def _fish_card_render(path, src_w, src_h, card_w, card_h, flip, st, at):
        """Рендерит иллюстрацию рыбы, увеличенную "cover"-масштабом до card-размера
        (лишнее обрежется при вклейке в canvas ниже) и при необходимости отражённую
        по горизонтали - картинки по умолчанию смотрят влево, разворот нужен, когда
        рыба плывёт вправо."""
        scale = max(card_w / float(src_w), card_h / float(src_h))
        xzoom = -scale if flip else scale
        d = Transform(path, xzoom=xzoom, yzoom=scale)
        return renpy.render(d, 4096, 4096, st, at)


    class Fish(object):
        """Одна рыба: позиция, горизонтальное движение, обычная или "обманщука"."""

        def __init__(self, x, y, speed, is_fake, image_info, radius=30):
            self.x = x
            self.y = y
            self.speed = speed
            self.is_fake = is_fake
            self.image_name, self.image_w, self.image_h = image_info
            self.radius = radius
            self.caught = False


    class FishingGame(object):
        """Состояние раунда рыбалки: удочка, крючок, стайка рыб, счёт, таймер."""

        def __init__(self, width=1000, height=640, duration=24.0, fish_count=5, fake_ratio=0.45):
            self.width = width
            self.height = height
            self.water_top = 100
            self.margin = 60

            self.pivot = (width / 2.0, 26)

            self.angle = 0.0
            self.angle_dir = 1
            self.angle_min = -50.0
            self.angle_max = 50.0
            self.angle_speed = 65.0

            self.state = "aiming"  # aiming -> casting -> reeling -> aiming
            self.cast_angle = 0.0
            self.line_len = 0.0
            self.max_line_len = height - 50
            self.cast_speed = 560.0
            self.reel_speed = 420.0
            self.hook_radius = 16

            self.caught = None
            self.fake_ratio = fake_ratio

            self.fishes = [self._spawn_fish() for _i in range(fish_count)]
            if fish_count > 1:
                if not any(f.is_fake for f in self.fishes):
                    self.fishes[0] = self._spawn_fish(force_fake=True)
                elif all(f.is_fake for f in self.fishes):
                    self.fishes[0] = self._spawn_fish(force_fake=False)

            self.duration = duration
            self.time_left = duration

            self.score = 0
            self.real_caught = 0
            self.fake_caught = 0

            self.last_result = None
            self.result_timer = 0.0

            self.finished = False

        def _spawn_fish(self, force_fake=None):
            is_fake = force_fake if force_fake is not None else (renpy.random.random() < self.fake_ratio)
            pool = FISH_BAD_IMAGES if is_fake else FISH_GOOD_IMAGES
            image_info = pool[renpy.random.randint(0, len(pool) - 1)]
            y = renpy.random.randint(self.water_top + 30, self.height - 40)
            x = renpy.random.randint(self.margin, self.width - self.margin)
            speed = renpy.random.randint(50, 120)
            if renpy.random.random() < 0.5:
                speed = -speed
            return Fish(x, y, speed, is_fake, image_info)

        def hook_pos(self):
            angle = self.cast_angle if self.state in ("casting", "reeling") else self.angle
            rad = math.radians(angle)
            dx = math.sin(rad)
            dy = math.cos(rad)
            return (self.pivot[0] + dx * self.line_len, self.pivot[1] + dy * self.line_len)

        def try_cast(self):
            if self.finished or self.state != "aiming":
                return False
            self.state = "casting"
            self.cast_angle = self.angle
            self.line_len = 0.0
            renpy.play("audio/water_in_a_bucket.wav")
            return True

        def _register_catch(self, fish):
            if fish.is_fake:
                self.fake_caught += 1
                self.score += 20
                self.last_result = "Поймана обманщука! +20"
            else:
                self.real_caught += 1
                self.score += 10
                self.last_result = "Обычная рыба поймана! +10"
            self.result_timer = 1.6
            renpy.play("audio/true_answer.wav")

            self.fishes.remove(fish)
            self.fishes.append(self._spawn_fish())

        def update(self, dt):
            if self.finished:
                return

            self.time_left -= dt

            if self.result_timer > 0:
                self.result_timer = max(0.0, self.result_timer - dt)
                if self.result_timer == 0.0:
                    self.last_result = None

            for fish in self.fishes:
                if fish is self.caught:
                    continue
                fish.x += fish.speed * dt
                if fish.x < self.margin:
                    fish.x = self.margin
                    fish.speed = abs(fish.speed)
                elif fish.x > self.width - self.margin:
                    fish.x = self.width - self.margin
                    fish.speed = -abs(fish.speed)

            if self.state == "aiming":
                self.angle += self.angle_dir * self.angle_speed * dt
                if self.angle >= self.angle_max:
                    self.angle = self.angle_max
                    self.angle_dir = -1
                elif self.angle <= self.angle_min:
                    self.angle = self.angle_min
                    self.angle_dir = 1

                if self.time_left <= 0:
                    self.finished = True
                return

            if self.state == "casting":
                self.line_len += self.cast_speed * dt
                hx, hy = self.hook_pos()

                for fish in self.fishes:
                    if fish.caught:
                        continue
                    dist = ((fish.x - hx) ** 2 + (fish.y - hy) ** 2) ** 0.5
                    if dist <= fish.radius + self.hook_radius:
                        fish.caught = True
                        self.caught = fish
                        self.state = "reeling"
                        break

                if self.state == "casting" and self.line_len >= self.max_line_len:
                    self.line_len = self.max_line_len
                    self.state = "reeling"
                return

            if self.state == "reeling":
                speed = self.reel_speed
                if self.caught is not None:
                    speed *= 0.55 if self.caught.is_fake else 0.85
                self.line_len -= speed * dt

                if self.caught is not None:
                    hx, hy = self.hook_pos()
                    self.caught.x = hx
                    self.caught.y = hy

                if self.line_len <= 0:
                    self.line_len = 0.0
                    if self.caught is not None:
                        self._register_catch(self.caught)
                    else:
                        self.last_result = "Пусто..."
                        self.result_timer = 1.4
                    self.caught = None
                    self.state = "aiming"

                    if self.time_left <= 0:
                        self.finished = True
                return

        def result(self):
            return {
                "score": self.score,
                "real": self.real_caught,
                "fake": self.fake_caught,
            }


    class FishingGameDisplayable(renpy.Displayable):
        """Рисует воду, удочку с крючком и рыб; тикает игру каждый кадр через st."""

        def __init__(self, game, **kwargs):
            super(FishingGameDisplayable, self).__init__(**kwargs)
            self.game = game
            self.last_st = None
            self._bg_image = _cover_scale(FISH_BG_IMAGE, FISH_BG_SRC_W, FISH_BG_SRC_H, game.width, game.height)

        def _draw_background(self, r_parent, st, at):
            """fixed/frame в screen language НЕ обрезают детей по границам сами по себе
            (проверено по документации Ren'Py) - оверсайженный "cover"-фон там просто
            вылезал бы за пределы игрового поля. Render.blit() в родительский Render
            фиксированного размера, наоборот, обрезает гарантированно - тот же приём,
            что и для карточек рыб ниже."""
            w, h = self.game.width, self.game.height
            bg_render = renpy.render(self._bg_image, 8192, 8192, st, at)
            bw, bh = bg_render.get_size()
            offset_x = (w - bw) // 2
            offset_y = (h - bh) // 2

            bg = renpy.Render(w, h)
            bg.blit(bg_render, (offset_x, offset_y))
            r_parent.blit(bg, (0, 0))

        def _draw_fish(self, canvas, r_parent, fish, st, at):
            direction = 1 if fish.speed >= 0 else -1
            card_w, card_h = 78, 54
            cx, cy = int(fish.x), int(fish.y)
            left, top = cx - card_w // 2, cy - card_h // 2

            fish_render = _fish_card_render(
                fish.image_name, fish.image_w, fish.image_h, card_w, card_h,
                flip=(direction > 0), st=st, at=at,
            )
            fw, fh = fish_render.get_size()

            # Промежуточный Render строго card_w x card_h - вклейка в него обрежет
            # "cover"-увеличенную картинку по границам карточки, а уже его самого
            # вклеиваем в общий canvas на позицию рыбы.
            card = renpy.Render(card_w, card_h)
            card.blit(fish_render, ((card_w - fw) // 2, (card_h - fh) // 2))
            r_parent.blit(card, (left, top))

            if fish.is_fake:
                mark_x = left + card_w - 20
                for i in range(3):
                    mx = mark_x - i * 6
                    canvas.line((255, 235, 90), (mx, top + 6), (mx + 4, top + 12), 2)

        def render(self, width, height, st, at):
            dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
            self.last_st = st
            self.game.update(dt)

            w, h = self.game.width, self.game.height
            r = renpy.Render(w, h)

            # ВАЖНО: фон блитится ДО r.canvas() - похоже, Render фиксирует порядок
            # отрисовки canvas-поверхности в момент первого обращения к .canvas(), а не
            # по факту, когда на ней что-то рисуется. Если вызвать .canvas() раньше, а
            # фон вклеить позже, фон перекрывает уже зарегистрированную (но ещё пустую
            # на тот момент) canvas-поверхность целиком - так однажды пропала удочка.
            self._draw_background(r, st, at)
            canvas = r.canvas()

            pivot = self.game.pivot
            px, py = int(pivot[0]), int(pivot[1])

            if self.game.state == "aiming":
                rad = math.radians(self.game.angle)
                ex = pivot[0] + math.sin(rad) * 55
                ey = pivot[1] + math.cos(rad) * 55
                canvas.line((230, 200, 90), (px, py), (int(ex), int(ey)), 3)
            else:
                hx, hy = self.game.hook_pos()
                canvas.line((235, 235, 235), (px, py), (int(hx), int(hy)), 2)
                canvas.circle((235, 235, 235), (int(hx), int(hy)), self.game.hook_radius, 3)

            for fish in self.game.fishes:
                self._draw_fish(canvas, r, fish, st, at)

            canvas.circle((20, 20, 28), (px, py), 10)
            canvas.circle((230, 200, 90), (px, py), 10, 3)

            if not self.game.finished:
                renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            if x < 0 or y < 0 or x >= self.game.width or y >= self.game.height:
                return None

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.game.try_cast():
                    raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                if self.game.try_cast():
                    raise renpy.display.core.IgnoreEvent()

            return None


screen fishing_game_screen(width=1000, height=640, duration=24.0, fish_count=5, fake_ratio=0.45):
    modal True

    default game = FishingGame(width, height, duration, fish_count, fake_ratio)
    default fishing_display = FishingGameDisplayable(game)

    default panel_w = 1300
    default panel_h = 1040

    # Анимация удочки/рыб идёт через renpy.redraw() у fishing_display, но HUD-текст
    # и "if game.finished:" ниже - это язык экранов, он пересчитывается только при
    # restart_interaction. Без периодического пинка счёт/таймер выглядели бы
    # замороженными, а конец раунда никогда бы не наступал.
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

            text "ЛОВИ РЫБУ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Клик или пробел — забросить крючок в текущем направлении удочки":
                font "fonts/TschicholdBold.ttf"
                size 22
                color "#9aa0b4"
                xalign 0.5

            hbox:
                spacing 50
                xalign 0.5

                text "Очки: [game.score]" font "fonts/TschicholdBold.ttf" size 26 color "#e0e4ec"
                text "Обычных: [game.real_caught]" font "fonts/TschicholdBold.ttf" size 26 color "#9ad6ff"
                text "Обманщук: [game.fake_caught]" font "fonts/TschicholdBold.ttf" size 26 color "#ff9a8c"
                text "Время: [int(max(0, game.time_left))]" font "fonts/TschicholdBold.ttf" size 26 color "#f2d43c"

            if game.last_result:
                text "[game.last_result]":
                    font "fonts/TschicholdBold.ttf"
                    size 24
                    color "#f2d43c"
                    xalign 0.5
            else:
                text " " size 24 xalign 0.5

            add fishing_display xalign 0.5

    if game.finished:
        timer 1.5 action Return(game.result())


label fishing_game_demo:
    call screen fishing_game_screen

    $ fishing_result = _return
    "Раунд окончен. Очки: [fishing_result['score']], обычных рыб: [fishing_result['real']], обманщук: [fishing_result['fake']]."
    return
