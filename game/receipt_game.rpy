# Мини-игра "Сравни чеки" для сцены с Чебуречником, где Маша разбирает чеки.
# Эталонный чек ОДИН на всю игру: дата, список покупок, итог, ФИО кассира и печать
# справа снизу - показывает, как должен выглядеть настоящий чек. Проверяемые чеки
# меняются каждый раунд и либо содержат всё то же самое (настоящий), либо им не хватает
# ровно одной детали: печати, даты или имени кассира (тонкая подделка - всё остальное
# на месте), либо это вообще нет ни списка покупок, ни даты, ни кассира, ни печати -
# только нацарапанная от руки сумма (грубая подделка). Нажми "ЧЕК ВЕРЕН"/"ЧЕК НЕВЕРЕН".
# Всего 10 чеков, есть общий таймер на раунд.
#
# В отличие от wire/fishing/snake-игр здесь нет непрерывной анимации - только текст и
# кнопки, поэтому не нужен кастомный Displayable с покадровым canvas: обычный
# screen-таймер сам обновляет весь текст, так как срабатывание timer-action уже само по
# себе полноценное interaction-событие (в отличие от renpy.redraw() у Displayable).
# Печать - единственное, что рисуется через canvas (её нет смысла делать текстом).
#
# Как протестировать отдельно: с главного меню открыть консоль (Shift+O) и выполнить:
# jump receipt_game_demo
#
# Использует общий декоративный дисплеймбл (GradientPanelDisplayable) из wire_game.rpy -
# все .rpy файлы в game/ делят один общий Python/screen-неймспейс.

init python:

    RECEIPT_ITEM_POOL = [
        ("Чебурек мясной", 150),
        ("Чебурек с сыром", 140),
        ("Чебурек острый", 160),
        ("Самса с бараниной", 130),
        ("Хычин с картофелем", 120),
        ("Беляш", 90),
        ("Пирожок с капустой", 60),
        ("Лаваш с сыром", 110),
        ("Чай чёрный", 50),
        ("Кофе американо", 80),
        ("Кола 0.5", 70),
        ("Компот вишнёвый", 60),
        ("Айран", 55),
        ("Соус чесночный", 30),
        ("Кетчуп", 20),
    ]

    RECEIPT_CASHIER_NAMES = [
        "Иванова А.С.",
        "Петров Д.В.",
        "Сидоркина Е.Н.",
        "Кузнецов М.И.",
        "Романова О.П.",
        "Ткаченко В.А.",
        "Белова К.Р.",
        "Морозов С.Г.",
    ]

    RECEIPT_FRAUD_TYPES = ["stamp", "date", "name", "handwritten"]

    RECEIPT_FRAUD_DESCRIPTIONS = {
        "stamp": "На чеке нет печати.",
        "date": "На чеке нет даты.",
        "name": "На чеке нет имени кассира.",
        "handwritten": "Это просто сумма от руки, без даты, кассира, списка и печати.",
    }


    class StampDisplayable(renpy.Displayable):
        """Статичная круглая печать - рисуется один раз, без анимации."""

        def __init__(self, size=92, **kwargs):
            super(StampDisplayable, self).__init__(**kwargs)
            self.size = size

        def render(self, width, height, st, at):
            s = self.size
            r = renpy.Render(s, s)
            canvas = r.canvas()

            color = (150, 40, 40)
            cx = s // 2
            cy = s // 2
            canvas.circle(color, (cx, cy), s // 2 - 3, 3)
            canvas.circle(color, (cx, cy), s // 2 - 12, 2)

            label = Text("ОПЛАЧЕНО", color="#963030", size=13, font="fonts/TschicholdBold.ttf")
            label_render = renpy.render(label, s, s, st, at)
            lw, lh = label_render.get_size()
            r.blit(label_render, (cx - lw // 2, cy - lh // 2 - 9))

            sub = Text("ЧЕБУРЕЧНАЯ", color="#963030", size=10, font="fonts/TschicholdBold.ttf")
            sub_render = renpy.render(sub, s, s, st, at)
            sw, sh = sub_render.get_size()
            r.blit(sub_render, (cx - sw // 2, cy + lh // 2 - 5))

            return r


    class ReceiptItem(object):
        def __init__(self, name, price):
            self.name = name
            self.price = price


    class Receipt(object):
        def __init__(self, items, total, date, cashier, has_stamp):
            self.items = items          # None -> "нацарапанная от руки сумма"
            self.total = total
            self.date = date            # None -> нет даты
            self.cashier = cashier      # None -> нет имени кассира
            self.has_stamp = has_stamp


    class ReceiptRound(object):
        def __init__(self, check, fraud_type):
            self.check = check
            self.fraud_type = fraud_type
            self.is_fake = fraud_type is not None
            self.answered = False
            self.correct = False


    def _random_items():
        count = renpy.random.randint(4, 5)
        pool = list(RECEIPT_ITEM_POOL)
        renpy.random.shuffle(pool)
        chosen = pool[:count]
        return [ReceiptItem(name, price) for name, price in chosen]

    def _make_reference_receipt():
        items = _random_items()
        total = sum(item.price for item in items)
        cashier = renpy.random.choice(RECEIPT_CASHIER_NAMES)
        return Receipt(items, total, "04.08.2026", cashier, True)

    def _make_check_receipt(fraud_type):
        if fraud_type == "handwritten":
            total = renpy.random.choice([320, 410, 480, 560, 650, 720])
            return Receipt(None, total, None, None, False)

        items = _random_items()
        total = sum(item.price for item in items)
        cashier = renpy.random.choice(RECEIPT_CASHIER_NAMES)
        date = "%02d.08.2026" % renpy.random.randint(1, 28)
        has_stamp = True

        if fraud_type == "stamp":
            has_stamp = False
        elif fraud_type == "date":
            date = None
        elif fraud_type == "name":
            cashier = None

        return Receipt(items, total, date, cashier, has_stamp)

    def _build_fraud_plan(round_count):
        """Половина чеков настоящая, вторая половина - поддельная, по очереди
        распределённая между всеми видами подделки (каждый вид встретится хотя бы
        раз), порядок затем перемешивается."""
        fake_count = round_count // 2
        genuine_count = round_count - fake_count

        plan = [None] * genuine_count
        for i in range(fake_count):
            plan.append(RECEIPT_FRAUD_TYPES[i % len(RECEIPT_FRAUD_TYPES)])

        renpy.random.shuffle(plan)
        return plan


    class ReceiptGame(object):
        def __init__(self, duration=90.0, round_count=10):
            self.reference = _make_reference_receipt()

            plan = _build_fraud_plan(round_count)
            self.rounds = [ReceiptRound(_make_check_receipt(ft), ft) for ft in plan]

            self.current_index = 0
            self.score = 0
            self.duration = duration
            self.time_left = duration
            self.finished = False

        def current(self):
            if 0 <= self.current_index < len(self.rounds):
                return self.rounds[self.current_index]
            return None

        def tick_second(self):
            if self.finished:
                return
            self.time_left -= 1
            if self.time_left <= 0:
                self.time_left = 0
                self.finished = True

        def answer(self, guess_fake):
            if self.finished:
                return
            round = self.current()
            if round is None or round.answered:
                return

            round.answered = True
            round.correct = (guess_fake == round.is_fake)

            if round.correct:
                self.score += 100
                renpy.play("audio/true_answer.wav")
            else:
                renpy.play("audio/false_answer.wav")

        def advance_round(self):
            if self.finished:
                return
            self.current_index += 1
            if self.current_index >= len(self.rounds):
                self.finished = True

        def result(self):
            correct_count = sum(1 for r in self.rounds if r.answered and r.correct)
            return {
                "score": self.score,
                "correct": correct_count,
                "total": len(self.rounds),
            }


screen receipt_panel(title, receipt):
    $ panel_w = 380

    frame:
        xsize panel_w
        background "#f1ede0"
        padding (24, 20)

        vbox:
            spacing 6
            xsize (panel_w - 48)

            text title:
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#2a2a2a"
                xalign 0.5

            null height 4
            add Solid("#00000033") xysize (panel_w - 48, 1)
            null height 4

            if receipt.date:
                text "Дата: [receipt.date]":
                    font "fonts/TschicholdBold.ttf"
                    size 15
                    color "#4a4a4a"

            if receipt.items is not None:
                null height 2

                for i, item in enumerate(receipt.items):
                    text "[i + 1]. [item.name] — [item.price] руб.":
                        font "fonts/TschicholdBold.ttf"
                        size 16
                        color "#2a2a2a"

                null height 4
                add Solid("#00000033") xysize (panel_w - 48, 1)
                null height 4

                text "ИТОГО: [receipt.total] руб.":
                    font "fonts/TschicholdBold.ttf"
                    size 18
                    color "#2a2a2a"
            else:
                null height 10
                text "[receipt.total] руб.":
                    font "fonts/TschicholdBold.ttf"
                    size 22
                    italic True
                    color "#5a4a3a"
                    xalign 0.5
                null height 10

            null height 6

            fixed:
                xsize (panel_w - 48)
                ysize 92

                if receipt.cashier:
                    text "Кассир: [receipt.cashier]":
                        font "fonts/TschicholdBold.ttf"
                        size 14
                        color "#4a4a4a"
                        xalign 0.0
                        yalign 1.0

                if receipt.has_stamp:
                    add Transform(StampDisplayable(), rotate=-12) xalign 1.0 yalign 1.0


screen receipt_game_screen(duration=90.0, round_count=10):
    modal True

    default game = ReceiptGame(duration, round_count)

    default panel_w = 1180
    default panel_h = 860

    timer 1.0 repeat True action Function(game.tick_second)

    $ current = game.current()
    if current is not None and current.answered and not game.finished:
        timer 0.9 action Function(game.advance_round)

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (panel_w, panel_h)

        add GradientPanelDisplayable(panel_w, panel_h)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            text "СРАВНИ ЧЕКИ":
                font "fonts/TschicholdBold.ttf"
                size 42
                color "#ffffff"
                outlines [(4, "#0d3a45", 0, 0)]
                xalign 0.5

            text "Слева - образец. Справа - проверяемый. Всё ли на месте?":
                font "fonts/TschicholdBold.ttf"
                size 20
                color "#9aa0b4"
                xalign 0.5

            hbox:
                spacing 50
                xalign 0.5

                text "Чек: [min(game.current_index + 1, len(game.rounds))]/[len(game.rounds)]" font "fonts/TschicholdBold.ttf" size 24 color "#e0e4ec"
                text "Очки: [game.score]" font "fonts/TschicholdBold.ttf" size 24 color "#f2d43c"
                text "Время: [int(max(0, game.time_left))]" font "fonts/TschicholdBold.ttf" size 24 color "#ff9a8c"

            if current is not None and not game.finished:
                hbox:
                    spacing 40
                    xalign 0.5

                    use receipt_panel("ЭТАЛОННЫЙ ЧЕК", game.reference)
                    use receipt_panel("ПРОВЕРЯЕМЫЙ ЧЕК", current.check)

                if current.answered:
                    $ verdict = "Верно! " if current.correct else "Неверно! "
                    if current.is_fake:
                        $ verdict += "Чек поддельный: " + RECEIPT_FRAUD_DESCRIPTIONS[current.fraud_type]
                    else:
                        $ verdict += "Чек был подлинным."
                    text verdict:
                        font "fonts/TschicholdBold.ttf"
                        size 20
                        color ("#4ee08a" if current.correct else "#e6483c")
                        xalign 0.5
                else:
                    text " " size 20 xalign 0.5

                hbox:
                    spacing 40
                    xalign 0.5

                    textbutton "✓ ЧЕК ВЕРЕН":
                        sensitive not current.answered
                        background "#1f8a4c"
                        hover_background "#28b562"
                        insensitive_background "#1f8a4c88"
                        padding (30, 16)
                        text_font "fonts/TschicholdBold.ttf"
                        text_size 26
                        text_color "#ffffff"
                        action Function(game.answer, False)

                    textbutton "✗ ЧЕК НЕВЕРЕН":
                        sensitive not current.answered
                        background "#c23b2e"
                        hover_background "#e04b3c"
                        insensitive_background "#c23b2e88"
                        padding (30, 16)
                        text_font "fonts/TschicholdBold.ttf"
                        text_size 26
                        text_color "#ffffff"
                        action Function(game.answer, True)
            else:
                text ("Время вышло!" if game.time_left <= 0 else "Готово!"):
                    font "fonts/TschicholdBold.ttf"
                    size 30
                    color "#e0e4ec"
                    xalign 0.5

    if game.finished:
        timer 1.6 action Return(game.result())


label receipt_game_demo:
    call screen receipt_game_screen

    $ receipt_result = _return
    "Правильных ответов: [receipt_result['correct']] из [receipt_result['total']]. Очки: [receipt_result['score']]."
    return
