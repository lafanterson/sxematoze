# Мини-эпизод в Прологе: поверх страницы с курсом всплывают 3 рекламных баннера-приманки.
# Клик по любому из них показывает предупреждение "АНТИвирус" (первое появление
# концепции антивируса - потом он станет псом Анти). Клик по самому курсу не нужен -
# курс не является "живой кнопкой", Маша просто читает его и продолжает сама.
# Стиль кнопок - тот же шрифт/рамка, что и у обычных игровых выборов (см. style choice_button
# в screens.rpy), но компактнее и ближе к центру экрана - имитация окон поверх монитора.

screen course_ads_screen():
    modal True

    default ad_popup = None

    if ad_popup:
        frame:
            xalign 0.5
            yalign 0.5
            background "#14191eb4"
            padding (36, 26)

            vbox:
                spacing 14
                xalign 0.5
                xsize 460

                text "АНТИвирус":
                    font "fonts/TschicholdBold.ttf"
                    size 30
                    color "#ff5c5c"
                    xalign 0.5

                text "Подозрительная реклама заблокирована. Не переходите по таким ссылкам.":
                    font "fonts/TschicholdBold.ttf"
                    size 20
                    color "#ffffff"
                    xalign 0.5
                    text_align 0.5
                    layout "subtitle"

                textbutton "Закрыть":
                    background "#14191eb4"
                    hover_background "#28323cdc"
                    padding (24, 10)
                    text_font "fonts/TschicholdBold.ttf"
                    text_size 22
                    text_color "#ffffff"
                    text_hover_color "#cceeff"
                    text_xalign 0.5
                    xalign 0.5
                    action SetScreenVariable("ad_popup", None)
    else:
        textbutton "Тебе уже есть 14 лет? Заработок от 5000 рублей.":
            background "#14191eb4"
            hover_background "#28323cdc"
            padding (18, 12)
            text_font "fonts/TschicholdBold.ttf"
            text_size 20
            text_color "#ffffff"
            text_hover_color "#cceeff"
            text_align 0.5
            xpos 600
            ypos 360
            xsize 360
            action [SetScreenVariable("ad_popup", 1), Function(renpy.play, "audio/notification.wav")]

        textbutton "Крипта снова в России, хочешь заработать? Тебе…":
            background "#14191eb4"
            hover_background "#28323cdc"
            padding (18, 12)
            text_font "fonts/TschicholdBold.ttf"
            text_size 20
            text_color "#ffffff"
            text_hover_color "#cceeff"
            text_align 0.5
            xpos 980
            ypos 470
            xsize 360
            action [SetScreenVariable("ad_popup", 2), Function(renpy.play, "audio/notification.wav")]

        textbutton "Что сейчас ощущается как биткоин в 2010? Успей купить…":
            background "#14191eb4"
            hover_background "#28323cdc"
            padding (18, 12)
            text_font "fonts/TschicholdBold.ttf"
            text_size 20
            text_color "#ffffff"
            text_hover_color "#cceeff"
            text_align 0.5
            xpos 700
            ypos 590
            xsize 360
            action [SetScreenVariable("ad_popup", 3), Function(renpy.play, "audio/notification.wav")]

        textbutton "Продолжить читать курс →":
            background "#14191eb4"
            hover_background "#28323cdc"
            padding (22, 12)
            text_font "fonts/TschicholdBold.ttf"
            text_size 24
            text_color "#ffffff"
            text_hover_color "#cceeff"
            text_align 0.5
            xalign 0.5
            yalign 0.9
            action Return(True)
