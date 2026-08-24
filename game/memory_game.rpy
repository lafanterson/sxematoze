# Мини-игра "Память" на банковских картах - для сцены с "банкоматом"-мошенником в
# четвёртом акте (телефон вдруг сам открывает мини-игру вместо ответа на уведомление).
# Классическое "найди пару" из карточек-рубашек, три уровня подряд: 6, 8, 12 карт
# (3/4/6 пар). Карты стилизованы под банковские - фон-цвет "банка", золотой чип,
# простой геометрический "логотип платёжной системы" и маскированные цифры.
#
# В отличие от wire/fishing/snake/jenga - здесь всё чисто на действиях кнопок экрана
# (Function() на клик по карте, timer-action на паузы), без кастомного canvas-цикла
# с renpy.redraw()/event(). Это важно: срабатывание ЛЮБОГО action (клик по кнопке или
# таймер) само по себе - полноценное interaction-событие, которое обновляет весь
# экранный текст, поэтому не нужен трюк с периодическим restart_interaction(), которым
# пришлось чинить wire/fishing/snake/jenga. Единственный кастомный Displayable здесь -
# статичная иконка-логотип на лицевой стороне карты (примитивная фигура через canvas,
# т.к. в языке экранов своих кружков/ромбов нет).
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump memory_game_demo
#
# Использует общий декоративный дисплеймбл (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:
    import math

init python:

    # (фон, индекс формы логотипа, цвет логотипа, название банка, последние 4 цифры)
    MEMORY_CARD_DESIGNS = [
        ((58, 40, 140), 0, (255, 255, 255), "ЛУНАБАНК", "4471"),
        ((28, 108, 92), 1, (255, 255, 255), "СХЕМА PAY", "9028"),
        ((150, 42, 62), 2, (255, 255, 255), "ГОРИЗОНТ", "1153"),
        ((40, 70, 132), 3, (255, 255, 255), "ВОСТОК КРЕД", "6602"),
        ((122, 90, 22), 4, (255, 255, 255), "ЯНТАРЬ", "3390"),
        ((70, 30, 92), 5, (255, 255, 255), "МИРАЖ", "8817"),
    ]

    MEMORY_LEVELS = (6, 8, 12)


    class CardGlyphDisplayable(renpy.Displayable):
        """Статичная простая геометрическая фигура - "логотип платёжной системы"."""

        SHAPES = ["circle", "diamond", "triangle", "square", "star", "hex"]

        def __init__(self, shape_index, size=26, color=(255, 255, 255), **kwargs):
            super(CardGlyphDisplayable, self).__init__(**kwargs)
            self.shape = self.SHAPES[shape_index % len(self.SHAPES)]
            self.size = size
            self.color = color

        def render(self, width, height, st, at):
            s = self.size
            r = renpy.Render(s, s)
            canvas = r.canvas()
            cx = cy = s // 2
            rad = s // 2 - 2

            if self.shape == "circle":
                canvas.circle(self.color, (cx, cy), rad)
            elif self.shape == "diamond":
                canvas.polygon(self.color, [(cx, cy - rad), (cx + rad, cy), (cx, cy + rad), (cx - rad, cy)])
            elif self.shape == "triangle":
                canvas.polygon(self.color, [(cx, cy - rad), (cx + rad, cy + rad), (cx - rad, cy + rad)])
            elif self.shape == "square":
                canvas.rect(self.color, (cx - rad, cy - rad, rad * 2, rad * 2))
            elif self.shape == "star":
                pts = []
                for i in range(8):
                    ang = math.pi / 4 * i
                    rr = rad if i % 2 == 0 else rad * 0.42
                    pts.append((cx + math.cos(ang) * rr, cy + math.sin(ang) * rr))
                canvas.polygon(self.color, pts)
            elif self.shape == "hex":
                pts = [
                    (cx + math.cos(math.pi / 6 + i * math.pi / 3) * rad, cy + math.sin(math.pi / 6 + i * math.pi / 3) * rad)
                    for i in range(6)
                ]
                canvas.polygon(self.color, pts)

            return r


    class MemoryCard(object):
        def __init__(self, design_id):
            self.design_id = design_id
            self.revealed = False
            self.matched = False


    class MemoryGame(object):
        def __init__(self, level_sizes=MEMORY_LEVELS):
            self.level_sizes = level_sizes
            self.level_index = 0
            self.cards = []
            self.first = None
            self.second = None
            self.lock = False
            self.level_transition = False
            self.moves = 0
            self.mistakes = 0
            self.finished = False
            self._setup_level()

        def _setup_level(self):
            n = self.level_sizes[self.level_index]
            pairs = n // 2
            designs = list(range(len(MEMORY_CARD_DESIGNS)))
            renpy.random.shuffle(designs)
            chosen = designs[:pairs]
            deck = chosen * 2
            renpy.random.shuffle(deck)
            self.cards = [MemoryCard(d) for d in deck]
            self.first = None
            self.second = None
            self.lock = False

        def matched_pairs(self):
            return sum(1 for c in self.cards if c.matched) // 2

        def total_pairs(self):
            return len(self.cards) // 2

        def click_card(self, idx):
            if self.lock or self.finished or self.level_transition:
                return
            card = self.cards[idx]
            if card.matched or card.revealed:
                return

            card.revealed = True

            if self.first is None:
                self.first = idx
                renpy.play("audio/mouse_click_2.wav")
                return

            self.second = idx
            self.moves += 1
            a = self.cards[self.first]
            b = self.cards[self.second]

            if a.design_id == b.design_id:
                a.matched = True
                b.matched = True
                self.first = None
                self.second = None
                renpy.play("audio/true_answer.wav")
                if all(c.matched for c in self.cards):
                    self._advance_level()
            else:
                self.mistakes += 1
                self.lock = True
                renpy.play("audio/false_answer.wav")

        def unlock(self):
            if self.first is not None:
                self.cards[self.first].revealed = False
            if self.second is not None:
                self.cards[self.second].revealed = False
            self.first = None
            self.second = None
            self.lock = False

        def _advance_level(self):
            self.level_index += 1
            if self.level_index >= len(self.level_sizes):
                self.finished = True
            else:
                self.level_transition = True

        def start_next_level(self):
            self.level_transition = False
            self._setup_level()

        def result(self):
            return {"moves": self.moves, "mistakes": self.mistakes}


screen memory_card_face(design):
    $ bg, shape_idx, glyph_color, bank_name, last4 = design

    fixed:
        xysize (150, 96)

        add Solid(bg) xysize (150, 96)
        add Solid("#e8c96a") xysize (32, 22) xpos 10 ypos 10
        add CardGlyphDisplayable(shape_idx, 30, glyph_color) xpos 108 ypos 10

        text bank_name:
            font "fonts/TschicholdBold.ttf"
            size 15
            color "#ffffff"
            xpos 10
            ypos 44

        text "•••• [last4]":
            font "fonts/TschicholdBold.ttf"
            size 14
            color "#ffffffcc"
            xpos 10
            ypos 68


screen memory_card_back():
    fixed:
        xysize (150, 96)

        add Solid("#161b28") xysize (150, 96)
        add Solid("#232a3d") xysize (130, 76) xpos 10 ypos 10

        text "SXZ":
            font "fonts/TschicholdBold.ttf"
            size 26
            color "#39d6e055"
            xalign 0.5
            yalign 0.5


screen memory_card(game, idx):
    $ card = game.cards[idx]
    $ shown = card.revealed or card.matched
    $ clickable = (not shown) and (not game.lock) and (not game.level_transition)

    button:
        xysize (150, 96)
        background None
        action (Function(game.click_card, idx) if clickable else None)

        if shown:
            use memory_card_face(MEMORY_CARD_DESIGNS[card.design_id])
        else:
            use memory_card_back()

        if card.matched:
            add Solid("#4ee08a33") xysize (150, 96)


screen memory_game_screen():
    modal True

    default game = MemoryGame()

    default panel_w = 900
    default panel_h = 740

    if game.lock:
        timer 0.8 action Function(game.unlock)

    if game.level_transition:
        timer 1.2 action Function(game.start_next_level)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "НАЙДИ ПАРЫ КАРТ":
                font "fonts/TschicholdBold.ttf"
                size 40
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Клик по карте открывает её, найди все пары одинаковых":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5

            hbox:
                spacing 40
                xalign 0.5

                text "Уровень: [min(game.level_index + 1, len(game.level_sizes))]/[len(game.level_sizes)]" font "fonts/TschicholdBold.ttf" size 22 color "#e0e4ec"
                text "Пар: [game.matched_pairs()]/[game.total_pairs()]" font "fonts/TschicholdBold.ttf" size 22 color "#39d6e0"
                text "Ошибок: [game.mistakes]" font "fonts/TschicholdBold.ttf" size 22 color "#ff9a8c"

            if game.finished:
                text "Все уровни пройдены!":
                    font "fonts/TschicholdBold.ttf"
                    size 28
                    color "#4ee08a"
                    xalign 0.5
            elif game.level_transition:
                text "Уровень пройден!":
                    font "fonts/TschicholdBold.ttf"
                    size 28
                    color "#4ee08a"
                    xalign 0.5
            else:
                $ cols = 4 if len(game.cards) >= 8 else 3
                vbox:
                    spacing 16
                    xalign 0.5

                    for row_start in range(0, len(game.cards), cols):
                        hbox:
                            spacing 16
                            xalign 0.5

                            for idx in range(row_start, min(row_start + cols, len(game.cards))):
                                use memory_card(game, idx)

    if game.finished:
        timer 1.4 action Return(game.result())


label memory_game_demo:
    call screen memory_game_screen

    $ memory_result = _return
    "Все уровни пройдены. Ходов: [memory_result['moves']], ошибок: [memory_result['mistakes']]."
    return
