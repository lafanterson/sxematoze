# Мини-игра "Свари кофе" для сцены с Машей-бариста в кафе. Сначала на пару секунд
# показывается шпаргалка со всеми рецептами (иконки ингредиентов по порядку, каждая
# подписана), затем по клику прячется насовсем - дальше нужно варить по памяти. Напитки
# подряд (американо, латте, капучино с корицей, раф, мокка, айс латте), ингредиенты -
# подписанные иконки на полке снизу, тащить мышью в кружку по центру. Среди ингредиентов
# есть лишние (сахар всегда лишний; сироп/лёд лишние не для всех напитков) - их
# использование не по рецепту сразу засчитывается как ошибка. Кружка сбрасывается
# заново на каждый новый напиток.
#
# В отличие от receipt_game.rpy здесь снова нужен canvas: перетаскивание мышью и живая
# отрисовка кружки/иконок - тот же паттерн Displayable+event(), что в wire_game.rpy
# (MOUSEBUTTONDOWN подхватывает иконку, MOUSEMOTION тащит, MOUSEBUTTONUP роняет в
# кружку или отменяет, если мимо). Подписи под иконками рисуются через renpy.render()
# Text-дисплеймбла и r.blit() поверх canvas - тот же приём, что и печать в
# receipt_game.rpy (canvas сам текст не умеет). Экранный HUD-текст обновляется через
# renpy.restart_interaction() после отпускания мыши - постоянный поллинг-таймер тут не
# нужен, состояние меняется только по действию игрока, а не непрерывно.
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump coffee_game_demo
#
# Использует общий декоративный дисплеймбл (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:
    import pygame

init python:

    # Порядок шагов - открытые, общеизвестные рецепты кофеен (эспрессо всегда первым).
    COFFEE_RECIPES = [
        ("Американо", ["espresso", "water"]),
        ("Латте", ["espresso", "milk"]),
        ("Капучино с корицей", ["espresso", "foam", "cinnamon"]),
        ("Раф", ["espresso", "milk", "syrup"]),
        ("Мокка", ["espresso", "chocolate", "milk"]),
        ("Айс латте", ["espresso", "ice", "milk"]),
    ]

    COFFEE_INGREDIENT_INFO = {
        "espresso": ("Эспрессо", (74, 47, 31)),
        "water": ("Вода", (58, 124, 168)),
        "milk": ("Молоко", (232, 223, 200)),
        "foam": ("Молочная пена", (221, 208, 184)),
        "cinnamon": ("Корица", (168, 106, 42)),
        "chocolate": ("Шоколад", (66, 38, 22)),
        "syrup": ("Сироп", (214, 60, 120)),
        "ice": ("Лёд", (170, 220, 235)),
        "sugar": ("Сахар", (245, 245, 245)),
    }

    COFFEE_SHELF_ORDER = [
        "espresso", "water", "milk", "foam", "cinnamon", "chocolate", "syrup", "ice", "sugar",
    ]


    def _draw_ingredient_glyph(canvas, key, x, y, color):
        glyph = (255, 255, 255) if sum(color) < 380 else (40, 30, 20)

        if key == "espresso":
            canvas.rect(glyph, (x - 10, y - 6, 20, 14))
            canvas.line(glyph, (x - 10, y - 6), (x + 10, y - 6), 2)
        elif key == "water":
            canvas.polygon(glyph, [(x, y - 12), (x - 9, y + 8), (x + 9, y + 8)])
        elif key == "milk":
            canvas.rect(glyph, (x - 8, y - 10, 16, 20))
            canvas.polygon(glyph, [(x - 8, y - 10), (x, y - 16), (x + 8, y - 10)])
        elif key == "foam":
            canvas.circle(glyph, (x - 7, y + 2), 8)
            canvas.circle(glyph, (x + 3, y - 4), 9)
            canvas.circle(glyph, (x + 9, y + 4), 6)
        elif key == "cinnamon":
            canvas.rect(glyph, (x - 3, y - 12, 6, 24))
            canvas.line(glyph, (x - 6, y - 6), (x + 6, y - 2), 2)
            canvas.line(glyph, (x - 6, y + 4), (x + 6, y + 8), 2)
        elif key == "chocolate":
            canvas.rect(glyph, (x - 10, y - 10, 20, 20))
            canvas.line(color, (x - 10, y), (x + 10, y), 2)
            canvas.line(color, (x, y - 10), (x, y + 10), 2)
        elif key == "syrup":
            canvas.rect(glyph, (x - 6, y - 12, 12, 22))
            canvas.rect(glyph, (x - 3, y - 18, 6, 8))
        elif key == "ice":
            canvas.polygon(glyph, [(x, y - 12), (x + 12, y), (x, y + 12), (x - 12, y)])
        elif key == "sugar":
            canvas.rect(glyph, (x - 10, y - 8, 20, 16))
            canvas.circle(color, (x - 4, y - 2), 2)
            canvas.circle(color, (x + 3, y + 2), 2)
            canvas.circle(color, (x, y - 4), 2)


    def _draw_ingredient_icon(r, canvas, key, x, y, radius, st, at, with_label=True):
        """Кружок-иконка + подпись под ним (подпись рендерится отдельно и вклеивается
        через r.blit - canvas сам текст рисовать не умеет)."""
        x, y = int(x), int(y)
        name, color = COFFEE_INGREDIENT_INFO[key]
        outline = (15, 12, 10)

        canvas.circle(outline, (x, y), radius + 3)
        canvas.circle(color, (x, y), radius)
        _draw_ingredient_glyph(canvas, key, x, y, color)

        if with_label:
            label = Text(
                name, color="#e0e4ec", size=12, font="fonts/TschicholdBold.ttf",
                outlines=[(2, "#0d0f16", 0, 0)], text_align=0.5,
            )
            label_render = renpy.render(label, radius * 5, 24, st, at)
            lw, lh = label_render.get_size()
            r.blit(label_render, (x - lw // 2, y + radius + 5))


    class IngredientIconDisplayable(renpy.Displayable):
        """Статичная иконка ингредиента с подписью - используется и в шпаргалке, и на полке."""

        def __init__(self, key, radius=26, **kwargs):
            super(IngredientIconDisplayable, self).__init__(**kwargs)
            self.key = key
            self.radius = radius

        def render(self, width, height, st, at):
            w = self.radius * 5
            h = self.radius * 2 + 34
            r = renpy.Render(w, h)
            canvas = r.canvas()
            _draw_ingredient_icon(r, canvas, self.key, w // 2, self.radius + 4, self.radius, st, at)
            return r


    class CoffeeDrink(object):
        def __init__(self, name, recipe):
            self.name = name
            self.recipe = recipe
            self.progress = 0
            self.done = False
            self.mistakes = 0


    class CoffeeGame(object):
        def __init__(self, width=960, height=480):
            self.width = width
            self.height = height

            self.drinks = [CoffeeDrink(name, list(recipe)) for name, recipe in COFFEE_RECIPES]
            self.current_index = 0
            self.phase = "reveal"  # "reveal" -> "playing"
            self.finished = False

            self.feedback = None
            self.feedback_timer = 0.0
            self.total_mistakes = 0
            self.hint_visible = False

            self.cup_pos = (width * 0.5, height * 0.32)
            self.cup_radius = 50

            self.ingredients = []
            n = len(COFFEE_SHELF_ORDER)
            margin = 90
            usable = width - margin * 2
            step = usable / float(n - 1) if n > 1 else 0
            shelf_y = height - 84
            for i, key in enumerate(COFFEE_SHELF_ORDER):
                self.ingredients.append({"key": key, "x": margin + i * step, "y": shelf_y})

            self.dragging = None
            self.drag_pos = (0, 0)

        def current(self):
            if 0 <= self.current_index < len(self.drinks):
                return self.drinks[self.current_index]
            return None

        def dismiss_reveal(self):
            self.phase = "playing"

        def toggle_hint(self):
            if self.phase != "playing" or self.finished:
                return
            self.hint_visible = not self.hint_visible

        def start_drag(self, key, x, y):
            if self.phase != "playing" or self.finished:
                return
            drink = self.current()
            if drink is None or drink.done:
                return
            self.dragging = key
            self.drag_pos = (x, y)

        def update_drag(self, x, y):
            if self.dragging is not None:
                self.drag_pos = (x, y)

        def end_drag(self, x, y):
            if self.dragging is None:
                return
            key = self.dragging
            self.dragging = None

            dx = x - self.cup_pos[0]
            dy = y - self.cup_pos[1]
            if (dx * dx + dy * dy) ** 0.5 > self.cup_radius + 30:
                return

            drink = self.current()
            if drink is None or drink.done:
                return

            expected = drink.recipe[drink.progress]
            if key == expected:
                drink.progress += 1
                if drink.progress >= len(drink.recipe):
                    drink.done = True
                    self.feedback = "done"
                    self.feedback_timer = 1.3
                    renpy.play("audio/true_answer.wav")
                else:
                    self.feedback = None
                    renpy.play("audio/mouse_click_2.wav")
            else:
                drink.progress = 0
                drink.mistakes += 1
                self.total_mistakes += 1
                self.feedback = "mistake"
                self.feedback_timer = 1.0
                renpy.play("audio/false_answer.wav")

        def advance(self):
            if self.finished:
                return
            self.feedback = None
            self.hint_visible = False
            self.current_index += 1
            if self.current_index >= len(self.drinks):
                self.finished = True

        def update(self, dt):
            if self.feedback_timer > 0:
                self.feedback_timer = max(0.0, self.feedback_timer - dt)
                if self.feedback_timer == 0.0 and self.feedback != "done":
                    self.feedback = None

        def result(self):
            return {
                "completed": all(d.done for d in self.drinks),
                "mistakes": self.total_mistakes,
            }


    class CoffeeDisplayable(renpy.Displayable):
        """Полка с ингредиентами + кружка по центру; перетаскивание мышью."""

        def __init__(self, game, **kwargs):
            super(CoffeeDisplayable, self).__init__(**kwargs)
            self.game = game
            self.last_st = None

        def _draw_cup(self, canvas):
            cx, cy = int(self.game.cup_pos[0]), int(self.game.cup_pos[1])
            r_ = self.game.cup_radius
            outline = (15, 12, 10)

            body_w = r_ * 2
            body_h = int(r_ * 1.8)
            left = cx - body_w // 2
            top = cy - body_h // 2

            canvas.rect(outline, (left - 3, top - 3, body_w + 6, body_h + 6))
            canvas.rect((235, 230, 220), (left, top, body_w, body_h))

            drink = self.game.current()
            if drink is not None and drink.progress > 0:
                layer_h = body_h / float(len(drink.recipe))
                for i in range(drink.progress):
                    key = drink.recipe[i]
                    color = COFFEE_INGREDIENT_INFO[key][1]
                    y0 = int(top + body_h - (i + 1) * layer_h)
                    y1 = int(top + body_h - i * layer_h)
                    canvas.rect(color, (left, y0, body_w, y1 - y0 + 1))

            canvas.circle(outline, (cx + body_w // 2 + 14, cy), 18, 5)
            canvas.circle((40, 30, 26), (cx + body_w // 2 + 14, cy), 12)

        def render(self, width, height, st, at):
            dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
            self.last_st = st
            self.game.update(dt)

            w, h = self.game.width, self.game.height
            r = renpy.Render(w, h)
            canvas = r.canvas()

            canvas.rect((40, 30, 26), (0, 0, w, h))
            canvas.rect((30, 22, 18), (0, h - 130, w, 130))

            self._draw_cup(canvas)

            for ing in self.game.ingredients:
                if ing["key"] == self.game.dragging:
                    continue
                _draw_ingredient_icon(r, canvas, ing["key"], ing["x"], ing["y"], 28, st, at)

            if self.game.dragging is not None:
                dx, dy = self.game.drag_pos
                _draw_ingredient_icon(r, canvas, self.game.dragging, dx, dy, 32, st, at)

            if self.game.dragging is not None or self.game.feedback_timer > 0:
                renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            if self.game.phase != "playing" or self.game.finished:
                return None

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for ing in self.game.ingredients:
                    dx = x - ing["x"]
                    dy = y - ing["y"]
                    if (dx * dx + dy * dy) ** 0.5 <= 34:
                        self.game.start_drag(ing["key"], x, y)
                        renpy.redraw(self, 0)
                        raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.MOUSEMOTION and self.game.dragging is not None:
                self.game.update_drag(x, y)
                renpy.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 and self.game.dragging is not None:
                self.game.end_drag(x, y)
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.display.core.IgnoreEvent()

            return None


screen coffee_game_screen():
    modal True

    default game = CoffeeGame()
    default coffee_display = CoffeeDisplayable(game)

    default panel_w = 1120
    default panel_h = 900

    $ drink = game.current()
    if game.phase == "playing" and drink is not None and drink.done and not game.finished:
        timer 0.9 action Function(game.advance)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            text "СВАРИ КОФЕ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            if game.phase == "reveal":
                text "Запомни порядок - шпаргалка спрячется по клику":
                    font "fonts/TschicholdBold.ttf"
                    size 20
                    color "#9aa0b4"
                    xalign 0.5

                grid 3 2:
                    xalign 0.5
                    spacing 26

                    for name, recipe in COFFEE_RECIPES:
                        vbox:
                            spacing 4
                            xalign 0.5
                            xsize 320

                            text name:
                                font "fonts/TschicholdBold.ttf"
                                size 20
                                color "#39d6e0"
                                xalign 0.5

                            hbox:
                                spacing 6
                                xalign 0.5

                                for key in recipe:
                                    add IngredientIconDisplayable(key, 18)

                null height 6

                textbutton "Начать!":
                    xalign 0.5
                    background "#1f8a4c"
                    hover_background "#28b562"
                    padding (36, 16)
                    text_font "fonts/TschicholdBold.ttf"
                    text_size 26
                    text_color "#ffffff"
                    action Function(game.dismiss_reveal)

            else:
                text "Тащи ингредиенты мышью в кружку. Лишнее — мимо.":
                    font "fonts/TschicholdBold.ttf"
                    size 20
                    color "#9aa0b4"
                    xalign 0.5

                hbox:
                    spacing 50
                    xalign 0.5

                    text "Напиток: [min(game.current_index + 1, len(game.drinks))]/[len(game.drinks)]" font "fonts/TschicholdBold.ttf" size 24 color "#e0e4ec"
                    text "Ошибок: [game.total_mistakes]" font "fonts/TschicholdBold.ttf" size 24 color "#ff9a8c"

                if drink is not None and not game.finished:
                    text "Готовим: [drink.name]":
                        font "fonts/TschicholdBold.ttf"
                        size 22
                        color "#39d6e0"
                        xalign 0.5

                    textbutton (u"Скрыть подсказку" if game.hint_visible else u"💡 Подсказка"):
                        xalign 0.5
                        background "#2a3a52"
                        hover_background "#3a4f70"
                        padding (20, 8)
                        text_font "fonts/TschicholdBold.ttf"
                        text_size 16
                        text_color "#ffffff"
                        action Function(game.toggle_hint)

                    if game.hint_visible:
                        hbox:
                            spacing 6
                            xalign 0.5

                            for key in drink.recipe:
                                add IngredientIconDisplayable(key, 16)

                    if game.feedback == "mistake":
                        text "Не то! Начни этот напиток сначала.":
                            font "fonts/TschicholdBold.ttf"
                            size 18
                            color "#e6483c"
                            xalign 0.5
                    elif game.feedback == "done":
                        text "[drink.name] готов!":
                            font "fonts/TschicholdBold.ttf"
                            size 18
                            color "#4ee08a"
                            xalign 0.5
                    else:
                        text " " size 18 xalign 0.5

                    add coffee_display xalign 0.5
                else:
                    text "Все напитки готовы!":
                        font "fonts/TschicholdBold.ttf"
                        size 30
                        color "#e0e4ec"
                        xalign 0.5

    if game.finished:
        timer 1.4 action Return(game.result())


label coffee_game_demo:
    call screen coffee_game_screen

    $ coffee_result = _return
    "Готово! Ошибок за смену: [coffee_result['mistakes']]."
    return
