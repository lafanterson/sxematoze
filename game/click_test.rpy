# Диагностика: работают ли вообще клики по кнопкам экрана в этом проекте.
# Запуск из консоли (Shift+O): jump click_test

default click_test_count = 0

screen click_test_screen():
    frame:
        xalign 0.5
        yalign 0.5
        background "#1e2028"
        padding (40, 40)

        vbox:
            spacing 20
            xalign 0.5

            text "Нажатий: [click_test_count]" size 40 color "#ffffff" xalign 0.5

            button:
                xysize (300, 100)
                background Solid("#e6483c")
                hover_background Solid("#ff6a5c")
                xalign 0.5
                action [SetVariable("click_test_count", click_test_count + 1), Function(renpy.play, "audio/gav.wav", volume=0.7)]

                text "ЖМИ СЮДА" size 30 color "#ffffff" xalign 0.5 yalign 0.5

            textbutton "Закрыть":
                xalign 0.5
                action Return(True)


label click_test:
    $ click_test_count = 0
    call screen click_test_screen()
    "Тест окончен, нажатий было: [click_test_count]"
    return
