# "Выбор без выбора" в Прологе: два варианта, но "Надо ещё подумать..." убегает
# от курсора при наведении, так что реально кликабелен только "Покупаю!".
# Возвращает "buy" или "think" (если игрок всё же как-то умудрится попасть по второй).

screen fake_choice_screen():
    modal True

    default dodge_x = 0
    default dodge_y = 0

    textbutton "Покупаю!":
        background "#14191eb4"
        hover_background "#28323cdc"
        padding (30, 15)
        text_font "fonts/TschicholdBold.ttf"
        text_size 32
        text_color "#ffffff"
        text_hover_color "#cceeff"
        text_align 0.5
        xalign 0.5
        yalign 0.42
        action Return("buy")

    textbutton "Надо ещё подумать...":
        background "#14191eb4"
        hover_background "#28323cdc"
        padding (30, 15)
        text_font "fonts/TschicholdBold.ttf"
        text_size 32
        text_color "#ffffff"
        text_hover_color "#cceeff"
        text_align 0.5
        xpos (760 + dodge_x)
        ypos (620 + dodge_y)
        hovered [
            SetScreenVariable("dodge_x", renpy.random.randint(-280, 280)),
            SetScreenVariable("dodge_y", renpy.random.randint(-140, 140)),
        ]
        action Return("think")
