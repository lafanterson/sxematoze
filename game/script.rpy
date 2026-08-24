# Определение персонажей игры.
define narrator = Character('...', color="#8b06ac")
define e = Character('Машa', color="#8b06ac")
define anti = Character('Антивирус', color="#480954")
define zlicev = Character('Борис Евгеньевич', color="#000000")
define fisherman = Character('Рыбак', color="#e3d8a1")
define waiter = Character('Официант', color="#054a3e")
define nn = Character('Незнакомец', color="#000000")

define gid = Character('Гид', color="#f9f9f9")
define secure = Character('Охранник', color="#890909", who_style="erika_who")
define armen = Character('Чебуречник', color="#020202", who_style="erika_who")
define instasamka = Character('Владелец бутика', color="#cf15bc", who_style="erika_who")
define temshik_1 = Character('Незнакомец', color="#230303", who_style="erika_who")
define temshik_2 = Character('Незнакомец', color="#041e25", who_style="erika_who")
define dns = Character('Мастер', color="#000000", who_style="erika_who")
define cofe = Character('Бариста', color="#ffffff", who_style="erika_who")
define qr = Character('Промоутер', color="#0b2d37", who_style="erika_who")
define kurator = Character('Куратор', color="#cf15bc", who_style="erika_who")
define bankomat = Character('Незнакомец', color="#041e25", who_style="erika_who")

define masha_pos = Position(xalign=0.8, yalign=0.5)
define small_left_pos = Position(xalign=0.3, yalign=0.8)

image anti_error_X = "anti_error_X.png"
image anti_error_hps = Transform("anti_error_hps.png", size=(config.screen_width, config.screen_height))
image anti_error_login = "anti_error_login.png"
image anti_error_sxema_toze = "anti_error_sxema_toze.png"
image anti_error_sxemoaoze = "anti_error_sxemoaoze.png"

# size задан явно для всех видео: если он не указан, Ren'Py подгоняет дисплеймбл под
# НАТИВНОЕ разрешение файла, а не под экран игры (1920x1080). Большинство новых видео -
# 3840x2160 (4K) - без size было видно только левый верхний угол кадра, растянутый на
# весь экран ("зум"). С явным size видео просто масштабируется под экран, независимо от
# того, в каком разрешении сняли исходник. ВАЖНО: не убирайте size= при правках ниже -
# это уже дважды терялось при редактировании блока и вызывало баг с зумом заново.
image fishing_video = Movie(play="video/fishing_scene.webm", loop=True, size=(config.screen_width, config.screen_height))
image pyramid_entry_video = Movie(play="video/pyramid_entry.webm", loop=True, size=(config.screen_width, config.screen_height))
image intro_laptop_video = Movie(play="video/intro_laptop.webm", loop=True, size=(config.screen_width, config.screen_height))
image alley_arrival_video = Movie(play="video/alley_arrival.webm", loop=True, size=(config.screen_width, config.screen_height))
image city_view_video = Movie(play="video/city_view.webm", loop=True, size=(config.screen_width, config.screen_height))
image lake_view_video = Movie(play="video/lake_view.webm", loop=True, size=(config.screen_width, config.screen_height))
image pier_view_video = Movie(play="video/pier_view.webm", loop=True, size=(config.screen_width, config.screen_height))
image pyramid_inside_video = Movie(play="video/pyramid_inside.webm", loop=True, size=(config.screen_width, config.screen_height))
image pier_near_the_city_video = Movie(play="video/pier_near_the_city.webm", loop=True, size=(config.screen_width, config.screen_height))
image curators_lair_video = Movie(play="video/curators_lair.webm", loop=True, size=(config.screen_width, config.screen_height))
image advertising_screen_video = Movie(play="video/advertising_screen.webm", loop=True, size=(config.screen_width, config.screen_height))
image cafe_view_video = Movie(play="video/cafe_view.webm", loop=True, size=(config.screen_width, config.screen_height))
image cheburechnaya_video = Movie(play="video/cheburechnaya.webm", loop=True, size=(config.screen_width, config.screen_height))
image night_park_video = Movie(play="video/night_park.webm", loop=True, size=(config.screen_width, config.screen_height))
image fork_three_video = Movie(play="video/fork_three.webm", loop=True, size=(config.screen_width, config.screen_height))
image forest_view_video = Movie(play="video/forest_view.webm", loop=True, size=(config.screen_width, config.screen_height))
image avoiding_charging_video = Movie(play="video/avoiding_charging.webm", loop=True, size=(config.screen_width, config.screen_height))
image night_pyramid_entry_video = Movie(play="video/night_pyramid_entry.webm", loop=True, size=(config.screen_width, config.screen_height))
image fork_two_video = Movie(play="video/fork_two.webm", loop=True, size=(config.screen_width, config.screen_height))
image sleeping_masha_video = Movie(play="video/sleeping_masha.webm", loop=True, size=(config.screen_width, config.screen_height))
image cafe_inside_video = Movie(play="video/cafe_inside.webm", loop=True, size=(config.screen_width, config.screen_height))
image mashas_room_video = Movie(play="video/mashas_room.webm", loop=True, size=(config.screen_width, config.screen_height))
image charging_video = Movie(play="video/charging.webm", loop=True, size=(config.screen_width, config.screen_height))
image storage_video = Movie(play="video/storage.webm", loop=True, size=(config.screen_width, config.screen_height))
image bankomat_video = Movie(play="video/bankomat.webm", loop=True, size=(config.screen_width, config.screen_height))
image cafe_scene_video = Movie(play="video/cafe_scene.webm", loop=True, size=(config.screen_width, config.screen_height))

# Та же проблема с разрешением, что и у видео выше (см. комментарий над блоком видео),
# только для картинок: anti_view_* сняты/нарисованы в 3840x2160 (4K), а "scene" по
# умолчанию показывает картинку в её натуральном пиксельном размере, а не под экран
# (1920x1080) - из-за этого она выглядела увеличенной вдвое и обрезанной. Явные
# объявления с Transform(size=...) переопределяют автоматически найденные по именам
# файлов картинки из images/ и масштабируют их под экран так же, как size= у Movie.
image anti_view_triangle = Transform("anti_view_triangle.png", size=(config.screen_width, config.screen_height))
image anti_view_galochka = Transform("anti_view_galochka.png", size=(config.screen_width, config.screen_height))
image anti_view_shock = Transform("anti_view_shock.png", size=(config.screen_width, config.screen_height))
image anti_view_arrow = Transform("anti_view_arrow.png", size=(config.screen_width, config.screen_height))
image anti_view_exc_mark = Transform("anti_view_exc_mark.png", size=(config.screen_width, config.screen_height))
image anti_view_angry_angry = Transform("anti_view_angry_angry.png", size=(config.screen_width, config.screen_height))
image anti_view_angry = Transform("anti_view_angry.png", size=(config.screen_width, config.screen_height))


default anti_warning_seen = False
default pyramida_fled = False
default act_four_snack = "чипсов"

transform move_from_left:
    xoffset -800
    linear 0.5 xoffset 0

transform move_from_right:
    xoffset 800
    linear 0.5 xoffset 0

transform fisherman_pos:
    xalign 0.8
    yalign 1.0

transform exit_right:
    on hide:
        linear 0.8 xoffset 800 alpha 0.0

transform exit_left:
    on hide:
        linear 0.8 xoffset -800 alpha 0.0

#label main_menu:
#    play music "audio/menu_theme.ogg" fadein 1.0
    
# Игра начинается здесь:
label start:
    jump intro

label intro:
    stop music
    play music "audio/intro.ogg"
    scene black
    
    play sound "audio/keyboard.wav"

    scene intro_laptop_video
    with Dissolve(.5)

    e "Если я просто куплю этот курс… все же наладится?"
    stop sound
    e "…Начни зарабатывать ради своих мечт?"
    e "Оно точно стоит того!"

    scene advertising_screen_video
    with fade

    # МИНИ-ЭПИЗОД: всплывающая реклама поверх курса. Три ложных кнопки показывают
    # окно "АНТИвирус" (первое появление концепции антивируса - позже станет псом Анти).
    call screen course_ads_screen()

    scene intro_laptop_video
    with Dissolve(.5)

    e "И всё же я долго работала, чтобы накопить такую сумму..."
    "От нервов я начинаю безжалостно кусать щёку изнутри."
    e "Ну всё, Маша, соберись..."

    # МИНИ-ЭПИЗОД: "выбор без выбора" - "Надо ещё подумать..." убегает от курсора.
    call screen fake_choice_screen()

    if _return == "buy":
        e "Покупаю! Сейчас только выведу деньги с депозита…"
        play sound "audio/notification.wav"
        e "О, быстро деньги пришли на карту."
    else:
        e "Надо ещё подумать..."
        e "..."
        e "Всё, подумала. Хочу много денег!"

    "Я чувствую, как мои руки слегка подрагивают от волнения."
    "Я часто делала что-то втайне от родителей, но настолько серьезное – впервые. Раздавать листовки вместо уроков не сравнится с покупкой такой дорогой вещи..."
    "Но это ведь только во благо, значит ничего запрещенного я не делаю. Тем более я уже взрослая и все понимаю!"

    window hide

    play sound "audio/keyboard.wav"

    e "Так, перейти по ссылке, записаться, оплатить…"

    window hide

    play sound "audio/mouse_click_2.wav"

    scene img3
    pause 1.0

    play sound "audio/notification.wav"
    e "Мне пришел QR-код на оплату."
    e "Странно, почему здесь какой-то Константин Михайлович С.?"
    e "Кто это, где девушка?.."
    e "Ладно, отправляю."

    pause 1.0

    "«Платеж поступил! Курс скоро будет у тебя.»"

    show sprite_masha_fun at Position(xalign=0.5, yalign=0.1)
    e "Отлично!"
    hide sprite_masha_fun

    scene black
    with Dissolve(.5)

    # Здесь по задумке художника - удлинённый фон от первого лица (комп + телефон снизу),
    # с анимацией ожидания: Маша облокачивается на руку, на стене часы, отсчитывающие время.
    "Я откидываюсь на спинку стула и разглядываю часы на стене. Минуты будто специально тянутся медленнее обычного."
    pause 2.0

    play sound "audio/notification.wav"
    "Проходит не больше пяти минут, когда я слышу звук нового сообщения."
    scene advertising_screen_video with fade
    e "Наконец-то!"

    scene img4
    with Dissolve(.5)
    "Схематоз? Впервые слышу об этом приложении..."
    "Наверное, это их собственная платформа."
    e "Курсы такие популярные, логично сделать общение удобным для всех участников."
    window hide
    play sound "audio/mouse_click_2.wav"

    e "Сразу установлю на компьютер, а потом и на телефон."
    "Приложение устанавливается очень быстро. Странно, учитывая, что наш вай-фай постоянно тормозит."

    scene img5
    with Dissolve(.5)
    play sound "audio/mouse_click_2.wav"
    e "..."
    stop music

    play music "audio/dark_theme.wav"
    e "Что-то не так?"

    "Я несколько раз нажимаю левую кнопку мыши - не работает. Потом пытаюсь поводить курсором и понимаю, что он не двигается, будто завис на месте."
    "Это потому, что компьютер старый? Или потому, что загрузка слишком нагружает процессор?"

    scene img3

    show sprite_masha_angry
    e "Ну почему ты не работаешь?!"
    play sound "audio/notification.wav"
    e "Антивирус пытается заблокировать работу приложения sxematoz.exe."

    play sound "audio/notification.wav" loop
    scene img6_1
    with dissolve
    pause 0.15

    scene img6_2
    with dissolve
    pause 0.15

    scene img6_3
    with dissolve
    pause 0.15

    scene img6_4
    with dissolve
    pause 0.15

    scene img6_5
    with dissolve
    pause 0.15

    scene img6_6
    with dissolve
    pause 0.15

    scene img6_7
    with dissolve
    pause 0.15

    scene img6_8
    with dissolve
    pause 0.15

    scene img6_9
    with dissolve
    pause 0.15
    stop sound
    e "Чего?!"

    scene img7_1
    with dissolve
    pause 0.2

    scene img7_2
    with dissolve
    pause 0.2

    scene img7_3
    with dissolve
    pause 0.2

    scene black
    "Пальцы на руках начинают стремительно неметь. Покалывание распространяется по всему телу, пока я пытаюсь удержать себя в сознании."
    "Несмотря на все попытки найти опору, я все равно на пару мгновений проваливаюсь в темноту."
    window hide
    stop music fadeout 3.0
    jump act_one

#попадание в схематоз
label act_one:
    scene black
    pause 5.0
    play music "audio/street_noise.wav"

    e "А... Что?"
    e "Что произошло? Где я?"
    
    "Пытаясь согнать темную пелену, я часто моргаю и жмурюсь. Когда зрение приходит в норму, неоновый свет бьет по глазам."
    stop music
    play music "audio/welcome_to_the_city.ogg"
    scene alley_arrival_video with fade
    pause 0.5
    e "Что это за место?.."

    show img_phone_alley with Dissolve(.5)
    pause 1.5
    "На автомате я достаю из кармана телефон. На экране высвечивается карта с поставленной меткой «Переулок»."

    play sound "audio/shesterenka.wav"
    pause 3
    stop sound

    hide img_phone_alley with dissolve
    pause 1.0

    show sprite_anti_kind at small_left_pos, move_from_left
    play sound "audio/gav.wav" volume 0.7
    pause 1.0
    "Механический щенок неуверенно тычется мне в ногу носом, а потом поднимает голову и виляет хвостом так, словно он вовсе не был роботом."
    "Как странно. Всё вокруг не похоже на мой город. А тут меня еще и робо-собака встречает."
    "Мне хочется ущипнуть себя за руку и проверить — не сон ли это."
    stop music

    play music "audio/puppy_heart.ogg"

    play sound "audio/gav.wav" volume 0.7 loop
    anti "Гав!"
    pause 1.0
    "Щенок явно пытается привлечь мое внимание."
    stop sound
    "Я сажусь на корточки, рассматривая странную дисплей-мордочку и уши-локаторы."
    hide sprite_anti_kind

    hide sprite_masha_scary
    show sprite_masha_neutral at masha_pos
    e "Ты кто такой?"
    hide sprite_masha_neutral

    "Я неуверенно хлопаю пса по голове ладонью и у того на экране появляется значок загрузки."

    scene img9
    with dissolve
    pause 2.0
    scene img10_1
    with Dissolve(.5)
    pause 2.0

    scene alley_arrival_video with dissolve
    show sprite_masha_neutral at masha_pos
    e "Так, ты пытаешься мне что-то сказать, да?"
    e "Ты… мой компьютер?"
    hide sprite_masha_neutral
    window hide

    scene img10_1 with dissolve
    pause 0.5
    play sound "audio/false_answer.wav"
    pause 1.0
    stop sound

    "Я не до конца понимаю, что он хочет сказать, но все равно вздрагиваю от звука, который издает робот."

    scene alley_arrival_video with fade
    show sprite_masha_neutral at masha_pos
    e "Ты попал сюда вместе со мной из-за того вируса?"
    hide sprite_masha_neutral

    scene img10_1 with dissolve
    pause 0.5
    play sound "audio/true_answer.wav"
    pause 1.0
    stop sound

    scene img9
    with dissolve
    pause 1.0
    scene img10_2
    with Dissolve(.5)
    pause 1.0

    scene alley_arrival_video with fade
    show sprite_masha_surprised at masha_pos
    e "Меч и щит… Ты защищаешь?"
    e "Поняла! Ты антивирус!"
    hide sprite_masha_surprised

    scene img10_2 with dissolve
    pause 0.5
    play sound "audio/true_answer.wav"
    pause 1.0
    stop sound

    scene alley_arrival_video with dissolve
    show sprite_masha_neutral at masha_pos
    e "Как же тебя зовут?"
    hide sprite_masha_neutral

    'Я присматриваюсь к его ошейнику, на котором висит подвеска с надписью "Анти".'

    show sprite_masha_fun at masha_pos
    e "А, так тебя зовут Анти? Я могла и догадаться. Приятно познакомиться."
    hide sprite_masha_fun
    stop music

    play music "audio/welcome_to_the_city.ogg"

    show sprite_masha_confused at masha_pos
    e "Наверное, я ударилась головой. Или все-таки сплю."
    hide sprite_masha_confused

    "Я решаю разбираться с проблемами по мере их поступления и не паниковать."
    "Сейчас нужно понять, что мне делать и куда идти."

    show sprite_masha_neutral at masha_pos
    e "Точно, здесь же работает мой телефон. На нем и посмотрю куда мне нужно."
    hide sprite_masha_neutral

    "Наконец-то мне удается его разблокировать — в этом мире он работает по-другому."
    "Почему-то карта города загружается не полностью."
    "Отображается только дорога до какого-то парка. Видимо, выбора у нас нет."
    "Я с осторожностью выглядываю из переулка, а потом медленно выхожу из тени, оглядывая улицу неизвестного города."

    play sound "audio/foot_step.wav"

    jump act_two

#действие2 - фишинг
label act_two:
    scene city_view_video with fade
    show sprite_masha_surprised at Position(xalign=0.8, yalign=0.1), move_from_right
    e "Какой огромный город!"
    hide sprite_masha_surprised

    scene alley_arrival_video with fade
    show sprite_anti_kind at Transform(zoom=0.8, xalign=0.5, yalign=0.7)
    "Я оглядываюсь назад, убеждаясь в том, что механический щенок следует за мной."
    play sound "audio/gav.wav" volume 0.7

    "Анти довольно машет хвостом и тявкает."
    hide sprite_anti_kind

    scene city_view_video with fade
    show sprite_masha_neutral at Position(xalign=0.8, yalign=0.1)
    e "Если я действительно оказалась в незнакомом месте, первым делом нужно найти кого-нибудь и разобраться, что происходит."
    e "Анти, давай попробуем поговорить с кем-то из прохожих."
    hide sprite_masha_neutral

    scene city_view_video
    "Я ускоряю шаг, вертя головой в разные стороны в поисках людей."
    "На улице было безлюдно. Лишь редкие машины с тонированными, словно замыленными стеклами проносятся мимо."
    "Чем дальше я иду, тем реже становятся здания вокруг."
    "Наконец мы с псом выходим к местному парку."

    scene black with fade
    pause 1.0

    scene night_park_video with fade
    "Я заметила чуть поодаль высокого мужчину..."

    scene img13 with dissolve
    pause 1.0

    show sprite_masha_fun at Position(xalign=0.8, yalign=0.1)
    e "Вот сейчас и спросим, где мы с тобой, Анти."
    hide sprite_masha_fun
    play sound "audio/gav.wav" volume 0.7
    anti "Гав!"

    "Мы быстрым шагом подошли к мужчине. Я смутилась, не зная, что именно спросить и как заговорить."
    "Мужчина, словно почувствовав моё волнение и нерешительность, резко повернулся к нам лицом."

    play music "audio/lawyer.wav"
    scene night_park_video with fade
    pause 1.0
    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0), move_from_left
    pause 1.5
    nn "Добрый вечер! Хотели о чем-то спросить?"
    hide sprite_zlicev_neutral

    "Он так странно выглядел… Но разговаривал вежливо, поэтому я не чувствовала себя напуганной."

    show sprite_masha_confused at Position(xalign=0.8, yalign=0.1)
    e "Здравствуйте, не могли бы Вы мне помочь?"
    hide sprite_masha_confused

    show sprite_zlicev_fun at Position(xalign=0.1, yalign=-3.0)
    nn "Могу! Ты попала к нужному человеку. Моя специальность — помогать людям."
    hide sprite_zlicev_fun

    "Мужчина, кажется довольный собой, протянул мне картонный прямоугольник."
    "Это была визитка."

    scene img14 with dissolve
    pause 1.0
    zlicev "Меня зовут Борис Евгеньевич Злицев. Я что-то вроде адвоката."

    "Я не совсем поняла, как связаны помощь незнакомцам на улице и адвокатское дело, но все равно неловко улыбнулась, чтобы не злить нового знакомого."

    scene night_park_video with fade
    pause 1.0
    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0), move_from_left
    pause 1.0
    zlicev "Ну что, юная леди, чем я могу помочь тебе и... твоему маленькому другу?"
    hide sprite_zlicev_neutral

    "Я невольно посмотрела на Анти, который странно притих, усевшись на землю рядом с моей ногой."
    show sprite_masha_neutral at masha_pos
    e "Можете подсказать, что это за город? И где тут ближайший полицейский участок?"
    hide sprite_masha_neutral

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "О, это просто! Вы находитесь в городе Схе..."
    zlicev "А! Да, что касается полицейского участка, то я могу показать Вам путь. Вам точно не стоит идти туда одной."
    hide sprite_zlicev_neutral

    show sprite_masha_fun at Position(xalign=0.8, yalign=0.1)
    e "О, это было бы просто замечательно!"
    hide sprite_masha_fun

    "Все мои мысли были заняты тем, как попасть в полицейский участок и желанием скорее вернуться домой."
    "Злицев стукнул тростью по земле, а потом махнул ладонью, приглашая идти за ним."

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "Как Вас зовут, юная леди? Не буду же я обращаться к Вам так и дальше."
    hide sprite_zlicev_neutral

    show sprite_masha_confused at masha_pos
    e "Меня зовут Маша."
    hide sprite_masha_confused

    "Борис Евгеньевич не вызывает чувства опасности."
    "Может, он и выглядит странно, но в этом городе абсолютно всё кажется таким."
    "Анти плетется рядом, все еще очень тихий."
    "Я хочу наклониться и потрепать его по голове, но еще больше мне хочется быстрее добраться до места назначения."
    scene black
    stop music fadeout 2.0
    pause 1.0

    play music "audio/city_park.wav"
    scene forest_view_video with fade
    pause 1.0
    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.0), move_from_right
    pause 1.0
    e "Борис Евгеньевич, куда дальше?"
    hide sprite_masha_neutral

    show sprite_zlicev_upset at Position(xalign=0.1, yalign=-3.0), move_from_left
    zlicev "Мария, у тебя с собой смартфон?"
    hide sprite_zlicev_upset

    show sprite_masha_neutral at masha_pos
    e "Вот. А зачем?"
    hide sprite_masha_neutral

    "Когда экран загорается, я опять вижу лишь небольшой кусочек карты города."
    "Ни приложений, ни рабочего стола — только карта."

    show img_phone_park with Dissolve(.5)
    pause 1.5
    hide img_phone_park with dissolve
    pause 0.5

    show sprite_masha_confused at masha_pos
    e "Анти, как думаешь, стоит сюда идти?"
    hide sprite_masha_confused

    scene forest_view_video
    "Анти вдруг срывается с места и убегает вперёд, вглубь парка."

    show sprite_masha_surprised at masha_pos
    e "Анти, ты куда?!"
    hide sprite_masha_surprised

    show sprite_zlicev_upset at Position(xalign=0.1, yalign=-3.0)
    zlicev "Знакомься с особенностями города."
    zlicev "Иногда, чтобы пройти куда-то или что-то сделать, нужно будет взаимодействовать с обстоятельствами через смартфон."
    hide sprite_zlicev_upset

    "Я быстро убираю телефон в карман и бегу за Анти."

    scene fork_three_video with fade
    show sprite_anti_kind at small_left_pos with dissolve
    pause 0.5
    "Анти ждет меня у развилки, крутясь на месте возле странного дерева."

    show sprite_masha_neutral at masha_pos, move_from_right
    e "Анти! Больше от меня не убегай…"
    hide sprite_masha_neutral
    hide sprite_anti_kind

    "Я снова достаю телефон. Вместо карты я вижу несколько кнопок со ссылками на сайты."
    "Не понимаю, как выбрать правильную..."
    "Я замечаю, что ссылки немного различаются."
    "Кажется, что-то такое нам показывали на классных часах в школе, когда рассказывали о мошеннических ссылках."
    jump first_first

label first_first:
    scene fork_three_video with fade
    window hide

    menu:
        "Выбрать левую дорогу: https://sxematoze.ru/maps":
            show sprite_anti_kind at small_left_pos, move_from_left
            play sound "audio/gav.wav" volume 0.7
            anti "Гав!"
            show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.0), move_from_right
            e "По-моему, нам сюда…"
            hide sprite_anti_kind
            hide sprite_masha_neutral
            jump second_second
        "Выбрать правую дорогу: https://sXematoze.ru/mAps":
            play sound "audio/false_answer.wav"
            scene anti_error_X with fade
            pause 1.0
            e 'Спасибо, Анти! Здесь ошибка — в адресе использованы заглавные буквы. Если адрес сайта отличается от привычного написания, стоит насторожиться и проверить его внимательнее.'
            scene fork_three_video with fade
            "Все вокруг резко темнеет."
            "Мне становится очень некомфортно."
            jump first_first

label second_second:
    play sound "audio/foot_step.wav"
    pause 1.0
    scene fork_three_video with fade
    pause 1.0
    show sprite_zlicev_upset at Position(xalign=0.1, yalign=-3.0), move_from_left
    "Теперь дороги три."
    "Я смотрю на Бориса Евгеньевича, но тот не собирается ничего подсказывать."
    "Анти же беспокойно вертится на месте, будто и сам не уверен."
    hide sprite_zlicev_upset
    scene fork_three_video with fade
    window hide
    pause 1.0
    menu:
        "Здесь снова развилка."
        "Выбрать левую дорогу: https://sxema.toze.ru/maps":
            play sound "audio/false_answer.wav"
            scene anti_error_sxema_toze with fade
            pause 1.0
            e 'Кажется, я поняла, что ты хочешь мне сказать. Здесь лишняя точка — "sxema.toze" вместо "sxematoze"! Точка разделила слово на две части.'
            jump first_first
        "Выбрать среднюю дорогу: hps://semaoze.ru/maps":
            play sound "audio/false_answer.wav"
            scene anti_error_hps with fade
            pause 1.0
            e 'Понятно, тут что-то не так: «hps» вместо «https» — пропущены буквы в начале ссылки! А ещё буквы пропущены в самом слове "sxematoze"!'
            jump first_first
        "Выбрать правую дорогу: https://sxematoze.ru/maps":
            show sprite_anti_kind at small_left_pos, move_from_left
            play sound "audio/gav.wav" volume 0.7
            anti "Гав!"
            "Кажется, городские высотки становятся заметно ближе."
            hide sprite_anti_kind
            jump third_third

label third_third:
    play sound "audio/foot_step.wav"
    pause 1.0
    scene fork_three_video with fade
    menu:
        "Выбрать левую дорогу: https://sxematoze1.ru/log.in":
            play sound "audio/false_answer.wav"
            scene anti_error_login with fade
            pause 1.0
            e 'Точно, Анти! Тут лишняя точка — «log.in» вместо «login»! И адрес ведет совсем не туда, куда нужно — домен написан с лишним символом 1.'
            scene lake_view_video with fade
            show sprite_masha_scary at Position(xalign=0.8, yalign=-1.0), move_from_right
            "Кажется, вокруг становится немного темнее."
            "По спине пробегает неприятный холодок."
            "Я оглядываюсь в поисках Анти или Бориса Евгеньевича, но они пропали, оставив меня совсем одну."
            show lake_view_video:
                blur 0.0
                zoom 1.0
                linear 4.0 blur 35.0 zoom 1.03
            show black:
                alpha 0.0
                linear 2.0 alpha 1.0
            pause 3.0
            hide sprite_masha_scary
            jump first_first
        "Выбрать среднюю дорогу: https://sxematoze.ru/maps":
            show sprite_anti_kind at small_left_pos, move_from_left
            play sound "audio/gav.wav" volume 0.7
            anti "Гав!"
            show sprite_masha_fun at Position(xalign=0.8, yalign=-1.0), move_from_right
            e "О, получилось! Мы вышли из парка!"
            hide sprite_masha_fun
            hide sprite_anti_kind
            stop music
            jump continue
        "Выбрать правую дорогу: https://sxemoaoze.rup/maps":
            play sound "audio/false_answer.wav"
            scene anti_error_sxemoaoze with fade
            pause 1.0
            e 'Всё, я поняла! Здесь домен написан неправильно — "sxemoaoze" вместо "sxematoze", и «rup» вместо «ru»!'
            scene lake_view_video with fade
            show sprite_masha_scary at Position(xalign=0.8, yalign=-1.0), move_from_right
            "Кажется, вокруг становится немного темнее."
            "По спине пробегает неприятный холодок."
            "Я оглядываюсь в поисках Анти или Бориса Евгеньевича, но они пропали, оставив меня совсем одну."
            show lake_view_video:
                blur 0.0
                zoom 1.0
                linear 4.0 blur 35.0 zoom 1.03
            show black:
                alpha 0.0
                linear 2.0 alpha 1.0
            pause 3.0
            hide sprite_masha_scary
            jump first_first
    
label continue:
    scene black with fade
    pause 1.0
    play sound "audio/foot_step.wav"
    play music "audio/lake.ogg"
    scene pier_view_video with fade
    pause 1.0
    "Не сдержав радости, я выбегаю вперед, выскакиваю на деревянный причал и глубоко вдыхаю речной воздух."
    "Моста, однако, нигде не видно. Лишь причал и табличка."

    show sprite_masha_surprised at Position(xalign=0.8, yalign=-1.0), move_from_right
    pause 1.0
    e "Борис Евгеньевич, куда дальше?"
    hide sprite_masha_surprised

    "Обернувшись, я вижу лишь Анти, который дружелюбно виляет хвостом и двигает ушами-локаторами."
    "Злицева нигде нет. Похоже, нас оставили одних."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.0)
    e "Анти, давай тогда самим разбираться."
    hide sprite_masha_neutral

    "Мы подходим ближе к причалу, рассматривая табличку."
    scene img21 with dissolve
    pause 1.5
    e "Только лодки нигде нет."
    e "Наверное, здесь все работает так же, как в парке. Нужно посмотреть в телефоне."

    scene pier_view_video with fade
    pause 1.0

    show img_phone_pier with dissolve
    pause 2.0
    e "Правильно, тут можно купить билет."

    show img_phone_pier_ticket with dissolve
    pause 1.0
    "Я нажимаю на кнопку «Купить билет?», и передо мной снова появляются несколько ссылок. Опять придется искать правильную."
    jump second_choice

label second_choice:
    scene pier_view_video with fade
    menu:
        "htp://bilet..sxmz..ru/raspisan1e/gorod_ Sxmz/gorod_Shema-Praviy/":
            play sound "audio/false_answer.wav"
            e "Точно, Анти! Тут «htp» вместо «https», двойные точки, и даже пробел появился прямо в адресе!"
            play sound "audio/radio_noise.wav"
            show sprite_masha_scary at Position(xalign=0.5, yalign=-1.0), move_from_right
            e "Ой!"
            play sound "audio/spam.wav" loop
            e "Какой-то странный сайт... Блин, столько рекламы выскакивает, что я уже ничего не вижу!"
            e "Анти, помоги! А то у меня телефон сейчас взорвётся."
            stop sound
            hide sprite_masha_scary
            jump second_choice
        "https://bilet.sxmz.ru/raspisanie/gorod_Sxmz/gorod_Shema-Praviy/":
            show sprite_masha_fun at Position(xalign=0.5, yalign=-1.0), move_from_right
            pause 1.0
            e "Отлично! Сейчас за нами приплывет лодочник!"
            hide sprite_masha_fun
            jump fisherman
        "https://bilit.схмз.com/raspisanie/gorod_SHEm4/gorod_Shema-Praviy/":
            play sound "audio/false_answer.wav"
            e "Поняла, Анти! Тут «схмз» русскими буквами вместо латинских «sxmz», а домен на самом деле другой!"
            e "Да и «bilit» вместо «bilet». А ещё в названии города цифра «4» подменяет букву «a»."
            play sound "audio/radio_noise.wav"
            show sprite_masha_scary at Position(xalign=0.5, yalign=-1.0), move_from_right
            e "Ой!"
            play sound "audio/spam.wav" loop
            e "Какой-то странный сайт... Блин, столько рекламы выскакивает, что я уже ничего не вижу!"
            e "Анти, помоги! А то у меня телефон сейчас взорвётся."
            stop sound
            hide sprite_masha_scary
            jump second_choice
        "https:///билет.схмз.ru/перевод/gorot_Shema/gorod_Shema-Praviy/":
            play sound "audio/false_answer.wav"
            e "Точно, Анти! Тут вообще всё написано русскими буквами — «билет» и «схмз»! И слэшей после «https» три вместо двух."
            play sound "audio/radio_noise.wav"
            show sprite_masha_scary at Position(xalign=0.5, yalign=-1.0), move_from_right
            e "Ой!"
            play sound "audio/spam.wav" loop
            e "Какой-то странный сайт... Блин, столько рекламы выскакивает, что я уже ничего не вижу!"
            e "Анти, помоги! А то у меня телефон сейчас взорвётся."
            stop sound
            hide sprite_masha_scary
            jump second_choice

label fisherman:
    scene black with fade
    pause 1.0
    scene pier_view_video with fade
    pause 1.0
    "Из-за камышей неспешно выплывает небольшая лодка, похожая больше на рыбацкую, чем на прогулочную."

    show sprite_masha_fun at Position(xalign=0.1, yalign=-0.3), move_from_left
    e "Здравствуйте!"
    hide sprite_masha_fun

    "Я машу рукой мужчине примерно того же возраста, что и мой дедушка."
    "Анти тихо тявкает, подпрыгивая на месте. Я тихо смеюсь, радуясь тому, что пёсик оказывается отличным спутником."

    # zoom=0.85, но позиция задана пикселями (xpos/ypos + нулевой anchor), а не
    # xalign/yalign - иначе при уменьшении спрайт съезжает: xalign/yalign пересчитывают
    # позицию относительно РАЗМЕРА спрайта, который меняется вместе с zoom. Числа - это
    # прежняя позиция (xalign=0.8, yalign=-0.6 при родном размере спрайта 900x900 на
    # экране 1920x1080), переведённая в абсолютные пиксели, чтобы не зависеть от zoom.
    show sprite_fisherman_neutral at Transform(zoom=0.70, xpos=890, ypos=180, xanchor=0.0, yanchor=0.0), move_from_right
    pause 1.5
    fisherman "Здравствуй, девчушка. Это тебе нужно помочь перебраться?"
    fisherman "Только учти — я не перевозчик, я рыбак! Обращайся ко мне только как Дедушка-Рыбак!"
    hide sprite_fisherman_neutral

    "Я останавливаюсь у края причала. Анти рядом настороженно смотрит то на лодку, то на старика."

    show sprite_anti_scary at Position(xalign=0.5, yalign=0.8), move_from_left
    pause 2.0
    "Вдруг на его дисплее вспыхивает тревожный значок."
    scene anti_view_triangle with fade
    pause 2.0
    scene pier_view_video with fade

    show sprite_masha_neutral at Position(xalign=0.1, yalign=-0.3)
    e "Ты опять что-то чувствуешь?"
    hide sprite_masha_neutral

    show sprite_anti_kind at Position(xalign=0.5, yalign=0.8)
    "Значок сменяется другим — словно прищурился."
    hide sprite_anti_kind

    "Я перевожу взгляд на старика. Тот не торопит меня, только молча кивает в сторону лодки."

    show sprite_fisherman_neutral at Transform(zoom=0.70, xpos=890, ypos=180, xanchor=0.0, yanchor=0.0)
    fisherman "Если хочешь попасть дальше, пешком не пройдёшь. Там путь перекрыт."
    hide sprite_fisherman_neutral

    "Я оглядываюсь. Впереди и правда видно, что дорога обрывается."

    show sprite_anti_kind at Position(xalign=0.5, yalign=0.8)
    "Анти делает несколько шагов к воде, будто осторожно сканируя лодку."
    anti "..."
    hide sprite_anti_kind
    "На экране загорается зелёный значок."
    scene anti_view_galochka with fade
    pause 2.0
    scene pier_view_video with fade

    show sprite_masha_surprised at Position(xalign=0.1, yalign=-0.3)
    e "То есть… можно?"
    hide sprite_masha_surprised

    show sprite_anti_kind at Position(xalign=0.5, yalign=0.8)
    play sound "audio/gav.wav" volume 0.7
    anti "Гав!"
    hide sprite_anti_kind

    "Старик спокойно ждет."

    show sprite_fisherman_neutral at Transform(zoom=0.70, xpos=890, ypos=180, xanchor=0.0, yanchor=0.0)
    fisherman "Я не прошу верить мне. Просто садись, если хочешь узнать, что будет дальше."
    hide sprite_fisherman_neutral

    "Я колеблюсь, потом снова смотрю на Анти."

    show sprite_anti_kind at Position(xalign=0.5, yalign=0.8)
    "На экране появляется стрелка вперёд."
    hide sprite_anti_kind

    "Я понимаю: он не уверен, но другого пути нет."

    show sprite_masha_neutral at Position(xalign=0.1, yalign=-0.3)
    e "Ладно… Только без сюрпризов."
    hide sprite_masha_neutral

    show sprite_fisherman_fun at Transform(zoom=0.70, xpos=890, ypos=180, xanchor=0.0, yanchor=0.0)
    fisherman "Сюрпризы бывают разные."
    hide sprite_fisherman_fun

    "Кажется, я уже начинаю привыкать к местным странностям, поэтому не возражаю. Наоборот, киваю несколько раз, подхватывая Анти на руки."

    show sprite_masha_confused at Position(xalign=0.1, yalign=-0.3)
    e "Пёс поедет на коленках. Так же можно? Не будете ругаться?"
    hide sprite_masha_confused

    show sprite_fisherman_fun at Transform(zoom=0.70, xpos=890, ypos=180, xanchor=0.0, yanchor=0.0)
    fisherman "Полезайте, ребятишки, отвезу уж."
    hide sprite_fisherman_fun

    "Мы забираемся в лодку, и старик отчаливает в сторону светящегося неоном незнакомого города."

    scene fishing_video with fade
    pause 1.0

    fisherman "Сильно не выглядывайте из лодки. У нас тут разные рыбы бывают. Может выпрыгнуть и цапнуть."

    "Я бросаю взгляд на мутную воду."
    "Мне кажется, что под водой плавает не рыба, а что-то похожее на буквы и цифры — словно те самые ссылки, из которых мне совсем недавно пришлось выбирать. Интересно."

    e "Не будем, Дедушка-Рыбак."

    e "В воде так много этих щук. У вас здесь только такая рыба водится?"

    play sound "audio/water_in_a_bucket.wav"
    "После моих слов что-то громко ударяется о дно лодки, будто услышав меня. Становится немного не по себе."

    fisherman "Раньше обманщук здесь вообще не было, а потом кто-то выпустил парочку и вот те нате — через год уже экологическая катастрофа. Тьфу!"
    fisherman "Обычная рыба осталась, но её совсем немного. Вот я и плаваю тут днями напролёт, вылавливаю эту гадость. Это не так легко, как ты, наверное, думаешь."
    fisherman "Обманщуки могут притворяться другими рыбами — так они охотятся. Как будто белые и пушистые, а потом заплывают другой рыбе за спину — и всё, капут."
    fisherman "Чего нос повесила? Давай уж тогда лучше бери удочку и за дело. Слезами-то ты рыбам точно не поможешь."

    "Да, быстро дедуля за выгоду ухватился."
    "Только удочку я держала в руках всего пару раз, и то совсем мелкая и с папиной помощью."
    "Ну, я вообще-то и не против, правда рыбок мне было жалко."

    e "Дедуля, а я —"

    fisherman "Дедушка-рыбак."

    e "..."
    e "...Дедушка-рыбак, а я рыбачить не умею."

    fisherman "Ничего, и не таких учили. Хватай удочку."

    "Не сказать, что мне прямо-таки не хватало этого навыка по жизни, но..."
    "Из последних событий я уже успела вынести для себя пару важных уроков, и один из них — лучше быть готовой ко всему."
    "В смысле прямо {i}ко всему{/i}."

    play sound "audio/water_in_a_bucket.wav"
    pause 1.0

    "К нашему общему удивлению, у меня очень быстро клюет. Я даже немного теряюсь."
    e "Клюёт!"

    menu:
        "Резко дёрнуть удочку на себя!":
            pause 1.0
            play sound "audio/false_answer.wav"
            e "Ай, сорвалась!"
            play sound "audio/dog_skulezh.wav"
            fisherman "Не дёргай сразу — спугнёшь. Дай ей заглотить, потом тяни."
            "Я снова забрасываю удочку."
            play sound "audio/water_in_a_bucket.wav"
            pause 1.0
            "Поплавок дёргается."
            jump fisherman_catch

        "Подождать и потянуть плавно.":
            jump fisherman_catch

label fisherman_catch:
    # МИНИ-ИГРА: вытягивание рыбы в духе Gold Miner - раскачивающаяся удочка, заброс
    # крючка, вытягивание рыбы; обманщуки визуально отличаются царапиной-ссылкой на
    # боку и тянутся тяжелее. См. game/fishing_game.rpy.
    fisherman "Ну вот, чувствуешь? Теперь сама лови, пока клюёт."

    call screen fishing_game_screen(duration=60.0)

    $ fishing_real = _return["real"]
    $ fishing_fake = _return["fake"]

    e "Уф, готово!"

    if fishing_real + fishing_fake == 0:
        "За всё время мне так никого и не удалось вытащить."
        fisherman "Бывает и так. Клёв сегодня привередливый."
    else:
        "Я успеваю вытащить не одну рыбину."

        if fishing_fake > 0:
            "Среди улова попадаются серебристые рыбины с царапиной на боку, похожей на обрывок какого-то адреса сайта."
            e "Ой! Так это..."
            fisherman "Верно, обманщуки. Глаз у тебя острый — выглядят почти как обычный карп, а внутри одно жало."
            fisherman "Вот и всё их оружие — притворяться своими. Эту породу у нас фейкарпом кличут."
            "Я бросаю фейкарпов в отдельное ведро, подальше от воды, и вытираю руки о куртку."
        else:
            fisherman "Ну-ка, покажи улов."
            "Я присматриваюсь к рыбинам - вроде все самые обычные, серебристые, без подвоха."
            fisherman "Повезло тебе, обманщука сегодня стороной обошла. Не всегда так гладко бывает."

        e "Тяжело, наверное, отличать их, если они прикидываются обычными."

        fisherman "Присматриваешься — и видно. У тебя, кстати, тоже неплохо получилось, для первого раза."

    "Спустя какое-то время мы останавливаемся у набережной, переходящей в современный город."
    stop music fadeout 2.0

    scene black
    with Dissolve(.5)
    scene img22 with fade
    play music "audio/city_park.wav"
    pause 1.5
    show sprite_fisherman_neutral at Transform(zoom=1.3,xalign=1.0, yalign=0.6), move_from_right
    pause 1.5
    fisherman "Оплаты не надо. Вы очень хорошие ребятишки."
    hide sprite_fisherman_neutral

    "Мне становится забавно от того, что он имеет в виду и Анти. Тот довольно машет хвостом, а я тихо смеюсь, опуская его на землю."

    show sprite_fisherman_neutral at Transform(zoom=1.3,xalign=1.0, yalign=0.6), exit_right
    fisherman "Только учтите, если встретите моего брата, то будьте аккуратнее."
    fisherman "Он отказался от нашего семейного рыбацкого дела и теперь считает, что он пират."
    hide sprite_fisherman_neutral
    pause 0.5
    show sprite_masha_surprised at Position(xalign=0.1, yalign=-1.0), move_from_left
    e "Хорошо, спасибо вам. До свидания и хорошей рыбалки!"
    hide sprite_masha_surprised
    window hide
    jump act_three

label act_three:
    scene black
    with Dissolve(.5)
    pause 2.0
    scene img22 with fade
    show sprite_masha_neutral at masha_pos, move_from_right
    pause 2.0
    e "Круто, конечно, что нам удалось выбраться обратно в город, но по сути мы же просто вернулись туда, откуда начали..."
    hide sprite_masha_neutral

    "Я удручённо вздыхаю и опускаю взгляд в пол."
    "Мне до сих пор слабо верится в происходящее, однако голод, жажда и тоска ощущаются уже как-то слишком реально."
    "Если это сон, почему я не могу ничего изменить?"
    "Обычно я могла управлять своими снами почти как игрой. А этот сон будто сам управляет мной."

    show sprite_masha_sad at masha_pos
    e "Борис Евгеньевич обещал, что проводит нас до полицейского участка."
    e "Почему он нас бросил?.."
    hide sprite_masha_sad

    play sound "audio/dog_skulezh.wav"
    "Анти тычется лбом в мой кроссовок, привлекая внимание."
    "Когда я перевожу на него взгляд, пёсик крутится вокруг себя и бодро пятится назад, словно приглашая меня пойти за ним."

    show sprite_masha_neutral at masha_pos
    e "Хочешь отвести меня куда-то?"
    hide sprite_masha_neutral

    play sound "audio/gav.wav" volume 0.7
    show sprite_anti_kind at Position(xalign=0.3, yalign=0.7), move_from_left
    "Анти одобрительно тявкает, после чего делает пару маленьких шагов вперёд, оглядываясь на меня."

    show sprite_masha_fun at masha_pos
    e "Ладно, согласна, не будем киснуть. Надеюсь, у тебя есть какой-то план."
    hide sprite_masha_fun

    show sprite_anti_kind at Position(xalign=0.3, yalign=0.7)
    play sound "audio/gav.wav" volume 0.7
    anti "Гав!"
    hide sprite_anti_kind

    "Пес довольно гавкает. Я плетусь за ним, вытирая остатки слез рукавом."

    show sprite_masha_fun at Position(xalign=0.8, yalign=-0.3)
    e "Хорошо, пойдем-пойдем."
    hide sprite_masha_fun

    "Анти ведет меня по каменным дорожкам, пока те не сменяются на асфальтированные."

    scene black
    pause 1.0
    scene cafe_view_video
    with fade
    pause 1.0
    show sprite_masha_surprised at Position(xalign=0.8, yalign=-0.3), move_from_right
    pause 1.0
    e "Ты сюда меня привести хотел? Поесть?"
    hide sprite_masha_surprised
    "Я растроганно улыбаюсь роботу, когда тот активнее начинает вилять хвостом, словно утвердительно отвечая."
    show sprite_masha_fun at Position(xalign=0.8, yalign=-0.3)
    e "Спасибо, маленький дружок. Без тебя я бы совсем пропала."
    hide sprite_masha_fun

    "Мы заходим в кофейню. Я удивленно осматриваюсь, разглядывая необычный интерьер."
    stop music fadeout 3.0
    scene black with fade
    pause 1.0

    play music "audio/cafe.ogg"
    scene cafe_inside_video with fade
    pause 1.0
    "Анти уверенно отходит к дальнему столику у окна, а я следую за ним, ощущая растерянность."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.4), move_from_right
    e "Посетителей больше нет. Наверное, не очень популярное место."
    e "Нам же лучше."
    hide sprite_masha_neutral

    "Я усаживаюсь на диванчик и беру брошюру со стола. На ней было только фото кофейни и контактные данные без меню."
    "Взгляд невольно опускается. Мне снова становится грустно."
    "Я так скучаю по маминым рагу и борщу! Постоянно воротила нос, но сейчас бы отдала многое, чтобы поесть их снова."
    "И по маминым объятиям тоже скучаю. И даже по папиному ворчанию!"
    "Я чувствую, как на глаза накатывают слёзы. Пришлось шумно шмыгнуть носом и посмотреть вверх, чтобы успокоиться."

    play sound "audio/mechanical_sounds.wav"

    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3), move_from_left
    pause 0.5
    waiter "Добрый вечер. Как определитесь с заказом — поднимите руку, чтобы я увидела."
    hide sprite_waiter

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.4)
    "Я настолько погружена в свои мысли, что от неожиданности дёргаюсь."
    hide sprite_masha_scary

    show sprite_masha_confused at Position(xalign=0.8, yalign=-0.4)
    e "Извините… Я только что поняла, что у нас вообще нет денег."
    hide sprite_masha_confused
    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.4)
    e "Может мы сможем как-то договориться? Накормите чем-нибудь бесплатно? Или не бесплатно, я могу помыть полы!"
    hide sprite_masha_scary

    "Официантка молча указывает на швабру и ведро в углу."

    # МИНИ-ИГРА: мытьё полов "змейкой" - веди мокрую дорожку по грязным пятнам,
    # не наступая на собственный след. См. game/snake_game.rpy.
    show sprite_masha_cleaning at Position(xalign=0.25, yalign=0.40), move_from_left
    play sound "audio/washing_the_floor.wav" volume 0.05 loop

    call screen floor_cleaning_screen

    $ floor_result = _return
    stop sound

    if floor_result["completed"]:
        "Я обхожу мокрой тряпкой каждый уголок, пока пол не начинает блестеть."
    else:
        "Я успеваю отмыть только часть пола, прежде чем руки начинают гудеть от усталости."

    "Анти в это время гоняет по нему закатившуюся под диван монетку."
    hide sprite_masha_cleaning

    scene black with fade
    pause 1.0
    stop sound
    scene cafe_inside_video with fade
    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.4), move_from_right
    e "Я всё!"
    hide sprite_masha_neutral

    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3), move_from_left
    waiter "Оставайся. Но до открытия тебя тут быть не должно."
    hide sprite_waiter

    show sprite_masha_confused at Position(xalign=0.8, yalign=-0.4)
    e "Анти, а что нам потом делать?.."
    e "Ничего не понимаю…"
    e "Давай-ка уже до утра поспим, пока нас не выгнали."
    hide sprite_masha_confused

    scene black with fade
    pause 1.0
    scene sleeping_masha_video with fade
    pause 1.0
    "Я облокачиваюсь на декоративную подушку у спинки, пытаясь найти удобное положение для сна."
    "Анти забирается на диванчик рядом со мной и укладывается у меня под боком. Выключает свой экранчик и переходит в спящий режим."
    "Я широко зеваю, закрываю глаза и пытаюсь уснуть."

    scene cafe_inside_video with fade
    pause 0.5
    show img24:
        blur 0.0
        zoom 1.0
        linear 4.0 blur 35.0 zoom 1.03

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 5.0
    hide black with Dissolve(1.5)

    show img24:
        zoom 1.03
        blur 35.0
        linear 1.5 blur 0.0 zoom 1.0
    pause 1.5

    scene cafe_inside_video 
    play sound "audio/glitch.wav"
    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3), move_from_left
    waiter "Давай вставай! Уже люди заходят, а ты все спишь!"
    hide sprite_waiter

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.4), move_from_right
    e "А! Что? Куда?!"
    hide sprite_masha_scary

    "Официантка указывает в сторону моего кармана — будто намекая, что стоит проверить телефон."
    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3)
    waiter 'Можешь попробовать сходить в "Пирамиду".'
    hide sprite_waiter

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.4)
    e "Что за «Пирамида»?"
    hide sprite_masha_neutral

    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3)
    waiter "Ты не местная что ли?"
    waiter "Торговый центр «Пирамида». Славится тем, что там может разбогатеть кто угодно, главное – вовремя подписаться на идею."
    hide sprite_waiter

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.4)
    e "Понятно..."
    hide sprite_masha_neutral

    show sprite_waiter at Transform(zoom=0.9, xalign=0.2, yalign=0.3), exit_right
    waiter "...Шла бы ты отсюда."
    hide sprite_waiter

    "Официантка разворачивается на сто восемьдесят и катится в противоположном направлении. Я оглядываюсь на окно – на улице было уже совсем светло."

    show sprite_masha_sad at Position(xalign=0.8, yalign=-0.4)
    play sound "audio/dog_skulezh.wav"
    e "Мне страшно, я не понимаю, что делать…"
    hide sprite_masha_sad

    scene black with fade
    pause 1.0
    scene cafe_view_video with fade
    pause 2.0

    show img_phone_cafe_route with Dissolve(.5)
    pause 2.0
    "Маршрут до «Пирамиды» на телефоне я сама не могу найти."
    hide img_phone_cafe_route with Dissolve(0.5)
    pause 0.5

    "День прошёл, число сменилось - ничего не изменилось. Мы всё ещё без денег, голодные, и что самое главное — не имеем ни малейшего понятия, что нам делать дальше."
    "Я опускаю Анти на пол и присаживаюсь перед ним на корточки. В отражении на его дисплее я вижу своё лицо, чуть более уставшее, чем обычно."
    "Пока я вглядываюсь в дисплей растерянно виляющего хвостом Анти, мне приходит идея."

    show sprite_masha_neutral at masha_pos
    e "Анти, а у тебя, получается, есть встроенный навигатор?"
    hide sprite_masha_neutral

    "Я вспомнила, что именно Анти привёл нас к этой кофейне. Интересно, на что ещё способен этот робо-пёсик?"

    show sprite_masha_fun at masha_pos
    e "Тогда построй маршрут до этой «Пирамиды», попробуем с тобой, как там было... «Вовремя подписаться на идею»."
    play sound "audio/gav.wav" volume 0.7
    hide sprite_masha_fun

    # МИНИ-ИГРА: сборка правильной ссылки из падающих блоков по трём дорожкам
    # (протокол / домен / зона-и-путь). См. game/link_game.rpy.
    "Анти выводит на дисплее подсказку из блоков — нужно было собрать из них правильный адрес."
    jump act_three_route_menu

label act_three_route_menu:
    pause 0.5
    call screen link_builder_screen

    $ link_result = _return

    if link_result["solved"]:
        play sound "audio/true_answer.wav"
        "Собранная ссылка загорелась зелёным, и на дисплее Анти начала прорисовываться карта."
    else:
        play sound "audio/false_answer.wav"
        "Время почти вышло, но Анти сам дособирал последние кусочки адреса — на экране, пусть и с опозданием, проступает карта."

    "Следуя указаниям Анти, мы вскоре добрались до огромного торгового центра в форме пирамиды, окружённого высотными небоскрёбами."
    jump entry

label entry:
    play music "audio/pyramid.ogg"
    scene black
    with Dissolve(0.8)
    pause 1.0
    scene pyramid_entry_video
    with fade
    pause 1.0
    show sprite_masha_fun at Position(xalign=0.8, yalign=-1.2), move_from_right
    pause 1.0
    e "Вау! Какое красивое здание. И какое огромное."
    hide sprite_masha_fun at masha_pos

    scene black with Dissolve(0.8)
    play sound "audio/foot_step.wav"
    "Мы с Анти ускорили шаг, побыстрее приближаясь ко входу."

    scene pyramid_inside_video with fade
    pause 1.0
    "Внутри торговый центр оказался таким же впечатляющим, как и снаружи: высоченные потолки, бесконечные ряды магазинчиков, кафе и ресторанов."
    "Я растерялась, не зная, куда смотреть в первую очередь."
    "И не сразу заметила, что стою с открытым от восторга ртом."
    window hide
    pause 1.5
    "Взяв себя в руки, я оглядываюсь. В глаза сразу же бросается охранник."

    show sprite_masha_confused at Position(xalign=0.8, yalign=-1.2), move_from_right
    e "Здравствуйте, помогите, пожалуйста..."
    e "Я слышала, что здесь можно найти работу…"
    hide sprite_masha_confused

    show sprite_security_guard at Position(xalign=0.2, yalign=1.2), move_from_left
    pause 1.0
    "Устрашающе выглядящий мужчина окидывает нас с Анти нечитаемым взглядом и тяжело вздыхает."
    secure "Девочка, шла бы ты отсюда, пока не поз..."
    hide sprite_security_guard

    "Не успевает он договорить, как на меня, словно вороны налетает целая стайка потенциальных работодателей — некоторые даже пихают мне в руки визитки и сомнительные листовки."

    show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left, exit_right
    armen "Малая, пошли ко мне работать. Посуду помоешь — еду получишь. От меня посудомойщица ушла. Сказала, что будет продавать карты... Или покупать? Не помню."
    hide sprite_cheburek
    pause 1.0

    show sprite_technician at Position(xalign=0.2, yalign=1.2), move_from_left, exit_right
    dns "Можешь помочь мне разобрать технику на складе, обиженной точно не уйдёшь."
    hide sprite_technician
    pause 1.0

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2), move_from_left, exit_right
    temshik_1 "Да зачем тебе делать лишнюю работу? Вложи небольшой процент со своего будущего заработка в мой бизнес и привлеки как можно больше друзей."
    temshik_1 "Будешь получать деньги ничего не делая."
    hide sprite_temshik_1
    pause 1.0

    show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left, exit_right
    cofe "На твоем месте я бы им всем не доверял. Давай я помогу тебе. Вижу, что ты еще ребенок."
    cofe "Можешь сегодня поработать бариста в моем кафе."
    hide sprite_barista
    pause 1.0

    show sprite_masha_scary at masha_pos, move_from_right
    "У меня кружится голова от того, как много людей накидывается на меня с разными предложениями."
    "Но, признаться честно, быть востребованной на рынке труда очень даже приятно. Вот бы и в моём мире так было..."
    "Попробовала бы свои силы в каждом направлении!"
    hide sprite_masha_scary

    show sprite_anti_angry at small_left_pos, move_from_left
    play sound "audio/gav.wav" volume 0.7
    "На дисплее Анти вспыхивает значок «Запрещено»."
    hide sprite_anti_angry

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.2)
    e "Ладно, не паникуй. Я ещё не выбрала."
    hide sprite_masha_neutral

    "В этот момент рядом раздается вежливый голос."

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0), move_from_left
    zlicev "Вы что-то ищете?"
    hide sprite_zlicev_neutral

    show sprite_masha_surprised at Position(xalign=0.8, yalign=-1.2)
    "Я испуганно оборачиваюсь."
    hide sprite_masha_surprised

    "Передо мной стоит Злицев. В руках у него планшет — будто он здесь работает консультантом."

    show sprite_zlicev_fun at Position(xalign=0.1, yalign=-3.0)
    zlicev "Не хотел подслушивать, но у вас очень характерный вид. Новичок в «Пирамиде»?"
    hide sprite_zlicev_fun

    show sprite_masha_confused at Position(xalign=0.8, yalign=-1.2)
    e "Да."
    e "А вы… тут работаете?"
    hide sprite_masha_confused

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "Можно и так сказать. Я помогаю людям не тратить время на глупости."
    hide sprite_zlicev_neutral

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    anti "Гав!"
    hide sprite_anti_angry

    show sprite_zlicev_fun at Position(xalign=0.1, yalign=-3.0)
    zlicev "Какая смышленная машинка."
    hide sprite_zlicev_fun

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.2)
    e "Он просто осторожный."
    hide sprite_masha_neutral

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "Это полезно. Но иногда осторожность мешает заметить хороший шанс."
    zlicev "Уже выбрали что-нибудь?"
    hide sprite_zlicev_neutral

    show sprite_masha_confused at Position(xalign=0.8, yalign=-1.2)
    e "Ещё нет."
    hide sprite_masha_confused

    show sprite_zlicev_upset at Position(xalign=0.1, yalign=-3.0)
    zlicev "Тогда позвольте совет. Не берите первое, что кажется безопасным."
    zlicev "Безопасное здесь обычно либо скучное, либо слишком медленное."
    hide sprite_zlicev_upset

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.2)
    e "А что не скучное?"
    hide sprite_masha_neutral

    "Злицев делает вид, что оценивает варианты."

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "Если хотите просто переждать день — кафе."
    zlicev "Если хотите действительно заработать — лучше что-то поинтереснее."
    hide sprite_zlicev_neutral

    "Он указывает на объявление о технической подработке, а затем — на предложенние о «вложениях под процент»."

    show sprite_zlicev_fun at Position(xalign=0.1, yalign=-3.0)
    zlicev "Вот это, например, уже интереснее."
    hide sprite_zlicev_fun

    pause 1.0
    "На дисплее Анти начинают мигать восклицательные знаки."
    scene anti_view_exc_mark with fade
    pause 2.0

    scene pyramid_inside_video with fade

    show sprite_masha_confused at Position(xalign=0.8, yalign=-1.2)
    e "Ты чего? Он же просто предлагает варианты."
    hide sprite_masha_confused

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0)
    zlicev "Просто не все любят, когда им сразу выдают всю правду."
    hide sprite_zlicev_neutral

    "Он говорит это спокойно, почти с сочувствием."

    show sprite_zlicev_upset at Position(xalign=0.1, yalign=-3.0)
    zlicev "В таком месте, как «Пирамида», лучше не цепляться за слишком безобидные пути."
    zlicev "Пока думаешь, хорошие места разбирают другие."
    hide sprite_zlicev_upset

    show sprite_masha_confused at Position(xalign=0.8, yalign=-1.2)
    e "То есть вы советуете работу с техникой?"
    e "Я немного переживаю..."
    hide sprite_masha_confused

    show sprite_zlicev_neutral at Position(xalign=0.1, yalign=-3.0), exit_left
    zlicev "Я советую не бояться того, что выглядит чуть сложнее, чем хотелось бы."
    zlicev "Подумайте."
    zlicev "Но недолго."
    hide sprite_zlicev_neutral

    "Злицев слегка улыбается и входит в поток людей, быстро теряясь среди толпы."
    "У меня в голове столько мыслей, что я не знаю, как лучше поступить."

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    "На дисплее Анти снова вспыхивает значок «Опасно», а следом появляется сердитая мордочка."
    hide sprite_anti_angry
    scene anti_view_angry_angry
    pause 2.0
    scene pyramid_inside_video

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.2)
    e "Да поняла я…"
    e "Но он вроде нормально говорил."
    hide sprite_masha_neutral

    "Анти тихо недовольно гавкает."
    "Но техническая подработка теперь кажется мне немного привлекательнее..."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-1.2)
    e "Так, подожди, Анти!"
    e "Думаю, мы еще успеем везде поработать!"
    hide sprite_masha_neutral

    show sprite_anti_kind at small_left_pos
    "Пёсик смотрит на меня снизу вверх и, словно не понимая, склоняет голову набок."
    "Только сейчас я замечаю, что с тех пор, как мы вошли в «Пирамиду», Анти стал тише."
    hide sprite_anti_kind

    "Немного поразмыслив, я прихожу к выводу, что первым делом стоит пробовать то, что звучит наиболее безопасно — помыть посуду."
    "Пообещав остальным работодателям, что вернемся позже, мы с Анти отправляемся в чебуречную."

    scene black with fade
    play sound "audio/foot_step.wav"
    stop music
    jump work_cheburechnaya

label work_cheburechnaya:
    scene black
    pause 1.5
    "Лучше уж меня точно покормят едой, чем обещаниями о деньгах."
    e "Давайте я помогу вам убраться в чебуречной. Я согласна."
    
    play music "audio/cafe.ogg"
    scene cheburechnaya_video with fade
    pause 1.5

    show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left, exit_left
    armen "Помой всю посуду на кухне и я приготовлю тебе поесть."
    armen "Ну, и если хорошо справишься, то может ещё и монетку накину..."
    hide sprite_cheburek

    play sound "audio/stomach_rumbling.wav"
    "От разговоров о еде мой желудок решает громко напомнить, что со вчерашнего дня я не съела ни крошки..."

    show sprite_masha_neutral at masha_pos
    e "Хорошо, мы всё сделаем!"
    hide sprite_masha_neutral

    "Хм... Мы?"
    show sprite_anti_kind at small_left_pos, move_from_right
    play sound "audio/gav.wav" volume 0.7
    "Я смотрю на крутящегося возле моих ног пёсика."
    hide sprite_anti_kind

    show sprite_masha_fun at masha_pos
    e "Анти, а ты, случайно, не можешь как автобот во что-нибудь другое пересобраться?"
    e "В посудомойную машину, например?"
    hide sprite_masha_fun

    show sprite_anti_kind at small_left_pos
    anti "?"
    hide sprite_anti_kind

    show sprite_masha_neutral at masha_pos
    e "Да ну тебя."
    hide sprite_masha_neutral

    "Добродушный хозяин чебуречной провожает меня на кухню, и я, закатав рукава, принимаюсь мыть гору грязной посуды."

    scene black with fade
    play sound "audio/wash_up.wav"
    pause 5.0
    stop sound

    scene cheburechnaya_video with fade
    show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
    armen "Пока еда доходит, сверь-ка вот эти чеки с эталонным — где-то в цифрах наверняка подвох."
    hide sprite_cheburek

    "Он выкладывает передо мной один «эталонный» чек и пачку таких же на вид — и показывает, что сверять нужно построчно, а не по общей сумме: она подделывается вместе с чеком."

    # МИНИ-ИГРА: сравнение эталонного чека с проверяемым, найти изменённую строку.
    # См. game/receipt_game.rpy.
    call screen receipt_game_screen

    $ receipt_result = _return

    if receipt_result["correct"] == receipt_result["total"]:
        show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
        armen "Ни одной ошибки! Глаз-алмаз."
        hide sprite_cheburek
    elif receipt_result["correct"] >= receipt_result["total"] // 2:
        show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
        armen "Неплохо, хоть пару чеков и пропустила."
        hide sprite_cheburek
    else:
        show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
        armen "Ну, где-то не углядела — бывает. Присматриваться надо повнимательнее."
        hide sprite_cheburek

    "Закончив, я стираю рукавом выступивший на лбу пот."
    "М-да, почаще надо отрываться от компьютера..."
    "Руки немного устали, но зато я чувствую себя отдохнувшей."
    "Уборка меня расслабила: монотонные движения под дип-хаус, играющий в торговом центре, помогли избавиться от тревожных мыслей."

    show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
    pause 1.0
    armen "Молодчина, девчонка! Иди, садись."
    hide sprite_cheburek

    "От услышанной похвалы я расплываюсь в улыбке."
    "Этот мужчина напоминает мне моего дедушку, к которому меня раньше часто отправляли на лето."
    "Эх, вот бы сейчас в деревню, а не вот это вот всё..."
    "Дедулька указывает на один из столов, я в нетерпении чуть ли не запрыгиваю на диванчик, и вскоре он ставит передо мной..."

    scene black with fade
    pause 1.0

    scene img29 with dissolve
    pause 1.0
    "Горячий, маслянистый чебурек!"
    "Уверена, он ещё и хрустящий!"
    armen "И вот ещё, заслужила."

    scene cheburechnaya_video with fade
    "Дяденька протягивает мне сложенную вдвое купюру."

    show sprite_masha_fun at masha_pos, move_from_right
    e "Спасибо Вам огромное!"
    hide sprite_masha_fun

    show sprite_cheburek at Position(xalign=0.2, yalign=1.2), move_from_left
    armen "Не за что. Приятного аппетита."
    hide sprite_cheburek

    show sprite_masha_fun at Position(xalign=0.8, yalign=0.1)
    e "Фпафибо!"
    hide sprite_masha_fun
    "Говорю я, уже набивая рот сочным чебуреком."
    "..."
    "Доев, я ещё какое-то время просто сижу и смотрю в потолок, осознавая, какое же всё-таки приятное чувство — сытость."
    "Вдруг что-то холодное тычется мне в лодыжку, вырывая из мыслей."
    "Заглядываю под стол и ожидаемо обнаруживаю там Анти."

    show sprite_masha_sad at masha_pos
    e "Блин, дружок, а я даже и не знаю, чем тебя кормить..."
    hide sprite_masha_sad

    play sound "audio/gav.wav" volume 0.7
    pause 1.5

    show sprite_masha_sad at masha_pos
    e "Жалко, что я не могу понять, что ты там говоришь."
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Кстати, мне же предлагали разобрать какую-то технику на складе — вот там про тебя и спрошу. Идём."
    hide sprite_masha_neutral

    "Распрощавшись с владельцем чебуречной, мы с Анти отправляемся искать неназванный склад."

    scene black with fade
    play sound "audio/foot_step.wav"
    stop music
    jump work_sklad

label work_sklad:
    scene black
    pause 1.0
    stop music
    play sound "audio/foot_step.wav"
    "Благодаря подсказкам нескольких прохожих мы без труда находим нужный павильон."

    play music "audio/dark_theme.wav"
    scene storage_video with fade
    pause 1.0

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Здравствуйте?"
    hide sprite_masha_neutral

    show sprite_technician at Position(xalign=0.2, yalign=1.2), move_from_left
    dns "Привет. Помню тебя."
    hide sprite_technician

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8)
    e "Отлично! А что нужно делать?"
    hide sprite_masha_scary

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Перебери коробку в углу. Складывай плохие детали в одну коробку, хорошие в другую."
    hide sprite_technician

    "Я поворачиваюсь в сторону, куда показывает этот дядька."
    "И правда: в углу стоит куча коробок."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8)
    e "А заплатите сколько?"
    hide sprite_masha_neutral

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Достаточно."
    hide sprite_technician

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8)
    e "Это сколько?"
    hide sprite_masha_neutral

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Ещё один вопрос и «достаточно» превратится в «чуть меньше, чем достаточно»."
    hide sprite_technician

    "Я ещё раз смотрю на сдвинутые в угол коробки."
    "В целом разобрать одну такую за загадочное «достаточно» я готова."
    "За посуду дедуля дал мне сто рублей."
    "Наверное, здесь я получу примерно столько же."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8)
    e "Можно задать еще один вопрос?"
    e "Он не о деньгах, так что давайте без урезания зарплаты."
    hide sprite_masha_neutral

    "Мужчина продолжает молчать, сидя ко мне спиной."
    "Восприняв его молчание за согласие, я продолжаю говорить."

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8)
    e "Не знаете, что едят вот такие собаки?"
    hide sprite_masha_neutral

    "Мужчина разворачивается на стуле, окидывает тяжёлым взглядом сначала меня, затем Анти, жмущегося к моей ноге, и с усталым вздохом отвечает."

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Едят живые, а этот, считай, микроволновка с мозгами и на ножках."
    dns "Зарядных станций для таких по всему городу понатыкано."
    dns "А теперь работай."
    hide sprite_technician

    "Мне становится обидно слышать такое про Анти."
    "Никакая он не микроволновка!"
    "В нём, между прочим, эмпатии побольше, чем в некоторых людях."
    "Однако озвучивать это я не буду — от греха подальше."
    "Расстроенно поджав губы, я треплю пёсика по голове и принимаюсь разбирать детали по коробкам."

    # МИНИ-ИГРА: сортировка перепутанных деталей по болтам (см. game/bolt_sort_game.rpy)
    call screen bolt_sort_screen

    "Вот эта работа дается мне уже гораздо сложнее."
    "Мыть посуду под музыку — это одно, а копаться в кучке перепутанных деталек — совсем другое."

    scene storage_video with fade
    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Дя... Кхм."
    e "Уважаемый!"
    e "Я всё."
    hide sprite_masha_neutral

    "«Уважаемый» разворачивается на стуле и окидывает взглядом плоды моего труда."
    "Скупо улыбнувшись, он показывает мне большой палец."

    show sprite_technician at Position(xalign=0.2, yalign=1.2), move_from_left
    dns "Ещё одну разберёшь?"
    hide sprite_technician

    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8)
    e "Ну-у..."
    e "Могу, но у меня есть вопрос..."
    hide sprite_masha_neutral

    show sprite_masha_confused at Position(xalign=0.8, yalign=-0.8)
    e "..."
    hide sprite_masha_confused

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8)
    e "Зачем это нужно делать?"
    e "Вы плохие детали выкидывать будете?"
    hide sprite_masha_scary

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "А ты сама еще не поняла?"
    hide sprite_technician

    "Я оглядываюсь в поисках хоть какой-нибудь зацепки, но так ничего и не нахожу."
    "Что-то с этим техником явно не так..."

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8)
    e "А что тут нужно понять?"
    hide sprite_masha_scary

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Я думал, раз согласилась, значит разбираешься."
    dns "При ремонте мои ребята вытаскивают из техники оригинальные детали и заменяют их дешёвыми аналогами."
    dns "Вот на этом и зарабатываем. Большой бизнес."
    hide sprite_technician

    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8)
    e "..."
    hide sprite_masha_scary

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Ну что?"
    dns "Будешь вторую коробку разбирать?"
    hide sprite_technician

    menu:
        "Нет...":
            jump sklad_decline
        "Ладно, давайте...":
            jump sklad_agree
        "А заплатите сколько?":
            jump sklad_agree

label sklad_decline:
    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Нет..."
    hide sprite_masha_scary

    show sprite_technician at Position(xalign=0.2, yalign=1.2),move_from_left
    dns "Ну, не хочешь — как хочешь."
    hide sprite_technician

    "Мужчина долго копается в карманах, после чего, даже не взглянув в мою сторону, бросает мне монетку."
    "Я едва успеваю поймать её, а когда разжимаю ладонь, вижу..."

    pause 0.5

    show sprite_masha_surprised at Position(xalign=0.8, yalign=-0.8)
    e "Десять рублей?"
    hide sprite_masha_surprised

    show sprite_masha_angry at Position(xalign=0.8, yalign=-0.8)
    e "Вы издеваетесь?.."
    hide sprite_masha_angry

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Это я ещё добавил."
    hide sprite_technician

    show sprite_masha_angry at Position(xalign=0.8, yalign=-0.8)
    e "Да как вам не стыдно?! Я здесь минут сорок работала!"
    hide sprite_masha_angry

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    hide sprite_anti_angry

    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Я, между прочим, мог бесплатно поручить это дело роботам. Но не стал."
    dns "Решил создать пару рабочих мест для таких, как ты."
    dns "Так что десять рублей — это ещё неплохо."
    hide sprite_technician

    show sprite_masha_angry at Position(xalign=0.8, yalign=-0.8)
    e "Вы обманщик! Такая оплата — чистый грабёж!"
    hide sprite_masha_angry

    "Меня переполняет гнев."
    "Знай я, что за мою работу заплатят такие копейки, — ни за что бы не согласилась."
    "Любой труд должен оплачиваться достойно."

    show sprite_anti_kind at Position(xalign=0.55, yalign=1.0), move_from_right
    play sound "audio/dog_skulezh.wav"
    "Анти аккуратно прихватывает зубами край моей штанины и тянет меня в сторону."
    "Я понемногу прихожу в себя и понимаю, что спор с этим мужиком всё равно ни к чему не приведёт."
    hide sprite_anti_kind

    show sprite_masha_sad at Position(xalign=0.8, yalign=-0.8), exit_right
    e "Чтобы вам пусто было."
    hide sprite_masha_sad

    show sprite_technician at Position(xalign=0.2, yalign=1.2), exit_left
    dns "..."
    hide sprite_technician

    scene black with fade
    play sound "audio/foot_step.wav"
    stop music
    jump work_pyramida

label sklad_agree:
    play sound "audio/growl_short.wav" loop
    "Неожиданно для меня до этого тихий и спокойный Анти заходится истеричным лаем."
    "Техник испуганно вжимается в кресло, быстро переводя взгляд с меня на Анти и обратно."
    show sprite_technician at Position(xalign=0.2, yalign=1.2)
    dns "Девчонка, успокой свою собаку!"
    hide sprite_technician

    show sprite_anti_angry at Position(xalign=0.5, yalign=0.8), move_from_right
    pause 1.0
    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Анти!"
    e "Эй, Анти, а ну перестань! Фу!"
    hide sprite_masha_scary
    hide sprite_anti_angry

    "Пёс не успокаивается и продолжает вопить, даже когда я беру его на руки."

    show sprite_technician at Position(xalign=0.2, yalign=1.2), exit_left
    dns "Убирайтесь вон! Оба!"
    hide sprite_technician

    show sprite_masha_angry at Position(xalign=0.8, yalign=-0.8), exit_right
    e "Всё-всё, уходим!"
    hide sprite_masha_angry

    scene black with fade
    pause 1.0
    stop sound
    play sound "audio/foot_step.wav"
    "Когда я выбегаю из мастерской в фойе с Анти на руках, он наконец перестает лаять."

    scene pyramid_inside_video with fade
    pause 1.0
    "Я ставлю Анти на пол и присаживаюсь перед ним на корточки."

    show sprite_masha_sad at masha_pos, move_from_right
    e "Анти! Почему ты начал лаять?"
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Да, мужик этот странный какой-то, но он бы нам заплатил хотя бы!"
    e "Ты что, забыл, зачем мы сюда пришли?"
    hide sprite_masha_neutral

    "Анти склоняет голову набок, словно вообще не понимает, о чём я говорю."
    scene anti_view_angry with dissolve
    "На его дисплее начинает крутиться значок загрузки, а через пару секунд появляется какая-то новая иконка."

    $ anti_warning_seen = True

    scene img27 with fade
    show sprite_masha_surprised at masha_pos
    e "Так, это что-то новенькое..."
    hide sprite_masha_surprised

    show sprite_masha_neutral at masha_pos
    e "Вот бы к тебе приложили инструкцию."
    e "Ладно."
    e "Что бы там ни случилось, больше так меня не пугай."
    e "Договорились?"
    e "Идём работать дальше."
    hide sprite_masha_neutral

    show sprite_anti_sad at small_left_pos
    play sound "audio/dog_skulezh.wav"
    hide sprite_anti_sad

    stop music
    jump work_pyramida

label work_pyramida:
    scene pyramid_inside_video with fade
    pause 1.5
    play music "audio/pyramid.ogg"

    show sprite_masha_neutral at masha_pos
    e "Так, Анти, вон того дядьку видишь?"
    hide sprite_masha_neutral

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2), move_from_left
    temshik_1 "..."
    hide sprite_temshik_1

    show sprite_masha_neutral at masha_pos
    e "Он, кажется, затирал что-то про вклады. Пойдём спросим?"
    e "Только на этот раз будем внимательнее. Какой-никакой опыт у нас с тобой уже есть."
    hide sprite_masha_neutral

    show sprite_masha_neutral at masha_pos, move_from_right
    e "Здравствуйте, я..."
    hide sprite_masha_neutral

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2), move_from_left
    temshik_1 "О, девчонка, я тебя помню!"
    temshik_1 "Готова вложить процент с будущей зарплаты?"
    hide sprite_temshik_1

    show sprite_masha_scary at masha_pos
    e "Что-то я не очень понимаю, как это работает."
    e "Можете подробнее объяснить?"
    hide sprite_masha_scary

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2)
    temshik_1 "Смотри: ты вкладываешь небольшой процент со своего будущего дохода в мой бизнес и зовёшь друзей тоже вложиться."
    temshik_1 "Будешь получать деньги ничего не делая. Кайф, скажи?"
    temshik_1 "Получается, будешь получать процент с выплат своих друзей, а потом — и с выплат друзей твоих друзей!"
    hide sprite_temshik_1

    show sprite_masha_surprised at masha_pos
    e "Подождите..."
    e "Получается, все платят деньги, но при этом все их и получают?"
    e "Как такое может быть?"
    hide sprite_masha_surprised

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2)
    temshik_1 "А кто сказал, что получают все?"
    temshik_1 "Получают те, кто приводят много людей. Остальные — платят."
    hide sprite_temshik_1

    pause 0.5
    menu:
        "А у вас случайно не было родственника с фамилией «Мавроди»?":
            scene pyramid_inside_video with fade
            $ pyramida_fled = True
            show sprite_masha_fun at masha_pos
            e "А у вас случайно не было родственника с фамилией «Мавроди»?"
            hide sprite_masha_fun
            jump pyramida_fled_outcome
        "Ладно, я могу привести много людей. Только они будут в синей форме и с фуражкой, устроит?":
            scene pyramid_inside_video with fade
            $ pyramida_fled = True
            show sprite_masha_fun at masha_pos
            e "Ладно, я могу привести много людей. Только они будут в синей форме и с фуражкой, устроит?"
            hide sprite_masha_fun
            jump pyramida_fled_outcome
        "Попробуем.":
            scene pyramid_inside_video with fade
            $ pyramida_fled = False
            show sprite_masha_fun at masha_pos
            e "Попробуем."
            hide sprite_masha_fun
            "Мужчина расплывается в улыбке, а я начинаю прикидывать, кого можно позвать из своих новых знакомых."
            "Ну, дедуля из чебуречной — это раз..."
            "Интересно, а роботам можно вкладываться? Им вообще платят?"
            "Если да, то, может, и официантку получится уговорить..."
            "Хотя вряд ли мы уже друзья..."
            jump pyramida_agree_outcome
        "Ну... Деньги нам нужны, так что попробую, не понравится - уйду.":
            scene pyramid_inside_video with fade
            $ pyramida_fled = False
            show sprite_masha_neutral at masha_pos
            e "Ну... Деньги нам нужны. Попробую. Если не понравится — уйду."
            hide sprite_masha_neutral
            jump pyramida_agree_outcome

label pyramida_fled_outcome:
    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2), move_from_left
    temshik_1 "Ах ты мелкая!.."
    hide sprite_temshik_1

    show sprite_masha_fun at masha_pos, exit_right
    e "Анти, бежим!"
    hide sprite_masha_fun

    play sound "audio/gav.wav" volume 0.7
    scene black with fade
    play sound "audio/foot_step.wav"

    stop music
    play music "audio/cafe.ogg"
    scene img32 with fade

    show sprite_masha_confused at masha_pos, move_from_right
    e "Вроде бы оторвались."
    hide sprite_masha_confused

    'Я оглядываюсь по сторонам, но "Мавроди" нигде не видно.'
    "Если он вообще пытался нас догнать..."
    "Облегченно выдохнув, прислоняюсь спиной к ближайшей стене, чтобы немного отдышаться."

    show sprite_masha_fun at masha_pos
    e "М-да, Анти..."
    e "Ну и устроили мы сегодня переполох."
    hide sprite_masha_fun

    "Присев отдышаться за свободным столиком, я замечаю позабытую кем-то башню из деревянных брусков - самую обычную «Дженгу»."
    "От нечего делать я начинаю вытягивать бруски один за другим, наблюдая, как башня становится всё более шаткой."

    # МИНИ-ИГРА: Дженга - башня рано или поздно обязательно рухнет, сколько бы
    # брусков ни вытянуть аккуратно. Отсылка к тому, что финансовая пирамида тоже
    # неизбежно рушится. См. game/jenga_game.rpy.
    call screen jenga_game_screen

    $ jenga_result = _return

    show sprite_masha_surprised at masha_pos
    e "Ой!"
    hide sprite_masha_surprised

    "Башня с грохотом разваливается, бруски разлетаются по столу."
    "Вытянуть успела, если не ошибаюсь, [jenga_result['pulled']] штук, прежде чем всё рухнуло."

    show sprite_masha_neutral at masha_pos
    e "Рано или поздно она всё равно бы упала."
    e "...Прямо как та финансовая пирамида?"
    hide sprite_masha_neutral

    jump pyramida_reveal

label pyramida_agree_outcome:
    show sprite_anti_angry at Position(xalign=0.4, yalign=0.8), move_from_right
    play sound "audio/growl_short.wav"
    pause 1.0

    show sprite_masha_scary at masha_pos, move_from_right
    e "Анти, ты чего?"
    hide sprite_masha_scary

    hide sprite_anti_angry
    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2), move_from_left
    temshik_1 "Эй, успокой свою собаку! Как тебя вообще сюда с ней пустили?"
    hide sprite_temshik_1

    show sprite_anti_angry at Position(xalign=0.4, yalign=0.8)
    show sprite_masha_scary at masha_pos
    e "Он обычно так себя не ведёт! "
    e "Анти, фу! Нельзя!"
    hide sprite_masha_scary
    hide sprite_anti_angry

    "Я судорожно пытаюсь успокоить Анти, пока он, надрываясь, лает на испуганного мужчину."
    "Блин, если он сейчас убежит, мы все денежки провороним!"
    "Я подхватываю Анти на руки и начинаю пятиться назад."

    show sprite_masha_sad at masha_pos
    e "Сейчас он успокоится, и мы вернёмся, ладно?"
    e "Только не уходите, пожалуйста!"
    hide sprite_masha_sad

    show sprite_temshik_1 at Transform(zoom=0.9, xalign=0.2, yalign=1.2)
    temshik_1 "Может, выкинешь эту псину?"
    temshik_1 "Ты не видишь? Он бракованный какой-то!"
    hide sprite_temshik_1

    play sound "audio/growl_short.wav"

    show sprite_masha_angry at masha_pos
    e "Не говорите так! Он мой друг!"
    hide sprite_masha_angry

    "Мужчина крутит пальцем у виска и выразительно присвистывает."
    "Я тем временем пытаюсь закрыть Анти пасть и отхожу в сторону, чтобы убрать мужчину из его поля зрения."
    "Чтобы он не крутился, аккуратно обхватываю его мордочку руками и осматриваю — нет ли каких-нибудь внешних повреждений."

    show sprite_masha_sad at masha_pos
    show sprite_anti_angry at Position(xalign=0.4, yalign=0.8)
    e "Ну, вроде бы ничего не отвалилось..."
    e "Анти, что с тобой?"
    e "Я и в своем мире в технике ничего не понимаю, а ты так вообще какой-то... робо-пёс."
    hide sprite_anti_angry
    hide sprite_masha_sad
    jump pyramida_reveal

label pyramida_reveal:
    if pyramida_fled and not anti_warning_seen:
        jump pyramida_reveal_A
    elif pyramida_fled and anti_warning_seen:
        jump pyramida_reveal_B
    elif not pyramida_fled and not anti_warning_seen:
        jump pyramida_reveal_C
    else:
        jump pyramida_reveal_D

label pyramida_reveal_A:
    pause 0.5
    play sound "audio/notification.wav"
    pause 1.5

    show sprite_masha_neutral at masha_pos
    e "М?"
    hide sprite_masha_neutral

    "Анти странно пикает."
    scene anti_view_angry with fade
    "Когда я перевожу на него взгляд, на его дисплее появляется какой-то новый символ."

    scene img32
    show sprite_masha_surprised at masha_pos
    e "И что это должно значить?"
    hide sprite_masha_surprised

    "Немного пораскинув мозгами, я прихожу к неожиданно милому и забавному выводу."

    show sprite_masha_fun at masha_pos
    e "Ты что, так предупреждаешь меня?"
    e "Показываешь, что это был мошенник?"
    hide sprite_masha_fun

    play sound "audio/true_answer.wav"

    show sprite_masha_fun at masha_pos
    e "Спасибо, Анти, это очень ценно!"

    play sound "audio/notification.wav"
    pause 1.0
    "Я озадаченно посмотрела на Анти, однако, источником звука, похоже, был не он."
    "Я вдруг вспоминаю, что всё это время у меня в кармане лежит телефон."

    hide sprite_masha_fun
    show img16 with dissolve
    pause 1.5
    "На экране высвечивается уведомление. Странно..."
    "На этом кирпиче же вроде нет никаких приложений кроме карты?.."
    "Я бросаю вопросительный взгляд на Анти."
    "Он лишь молча виляет хвостом."
    "Я нажимаю на уведомление, чтобы его открыть."

    scene stat_159 with fade
    pause
    "Ничего себе..."

    scene img32 with fade
    show sprite_masha_neutral at masha_pos
    e "Это ты мне прислал?"
    hide sprite_masha_neutral

    play sound "audio/gav.wav" volume 0.7
    pause 1.5

    "..."
    "Нет, конечно, я и так понимаю, что тот тип — мошенник, но всё равно как-то не по себе."
    "Я ведь могла согласиться..."
    "И что тогда?"

    play sound "audio/notification.wav"
    "Вслед за первым уведомлением приходит и второе."

    scene stat_172_3 with fade
    pause

    scene img32 with fade
    show sprite_masha_neutral at masha_pos
    e "Так это всё-таки и правда была финансовая пирамида?"
    e "Я думала, сейчас на такое уже никто не ведётся..."
    hide sprite_masha_neutral
    "..."

    show sprite_masha_neutral at masha_pos
    e "Ты всё это время мог просто присылать мне уведомления?.."
    hide sprite_masha_neutral

    play sound "audio/false_answer.wav"
    pause 2.0

    "Я присаживаюсь перед Анти, ласково глажу его по голове, а потом принимаюсь обеими руками чесать за ушами."

    show sprite_masha_neutral at masha_pos
    e "Спасибо, Анти. Только ты в следующий раз заранее меня предупреждай."
    hide sprite_masha_neutral

    "Анти качает головой и по-механически урчит от удовольствия."
    "До сих пор не понимаю, как что-то металлическое и электронное вообще может чувствовать прикосновения."
    "Но Анти, кажется, нравится, так что неважно — микроволновка он на ножках или маленький терминатор."
    "Все равно буду чесать его и дальше."
    "..."
    "Выдав Анти порцию заслуженных поглаживаний, я встаю и осматриваюсь."

    stop music
    jump work_barista

label pyramida_reveal_B:
    pause 0.5
    play sound "audio/notification.wav"
    pause 1.5
    show sprite_masha_neutral at masha_pos with dissolve
    e "М?"
    hide sprite_masha_neutral

    "Анти странно пикает."
    scene anti_view_angry
    "Когда я перевожу на него взгляд, на его дисплее появляется какой-то новый символ."
    scene img32

    show sprite_masha_sad at masha_pos
    e "Я всё ещё не понимаю."
    e "Анти, ты можешь текстом показывать? Я эти пиктограммы не понимаю!"
    hide sprite_masha_sad

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    hide sprite_anti_angry

    show sprite_masha_scary at masha_pos, exit_right
    e "Ой!"
    hide sprite_masha_scary

    "Я вздрагиваю от неожиданности и падаю на пол."

    show sprite_masha_angry at masha_pos
    e "Анти! Предупреждать надо."
    hide sprite_masha_angry

    "Анти подходит ко мне, тычется носом в колено, а потом снова поднимает голову и начинает вилять хвостом, будто чего-то ждет."
    "Видимо, момента, когда я наконец догадаюсь..."

    show sprite_masha_sad at masha_pos
    e "..."
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Так, ладно."
    e "В прошлый раз ты показывал мне этот значок, когда мы столкнулись с мошенником..."
    e "И сейчас нам снова попался мошенник!"
    hide sprite_masha_neutral

    play sound "audio/true_answer.wav"
    "Анти вскакивает и начинает вприпрыжку носиться вокруг меня."
    "Уверена, если бы он умел говорить, то сейчас запел бы «Аллилуйя!»"

    show sprite_masha_fun at masha_pos
    e "Да? Ты умеешь распознавать не только вирусы, но и мошенников?"
    e "Какой ты молодец, Анти!"
    hide sprite_masha_fun

    "Анти останавливается передо мной и смотрит в глаза."
    scene img9 with fade
    "На его дисплее на несколько секунд появляется значок загрузки, а затем я слышу знакомый звук..."
    scene img32 with fade

    play sound "audio/notification.wav"
    pause 1.0
    "Источником звука был не Анти, значит..."
    "Я вспоминаю, что всё это время у меня в кармане лежал телефон."

    show img16 with dissolve
    pause 1.5
    "На экране высвечивается уведомление. Странно..."
    "На этом кирпиче же вроде нет никаких приложений кроме карты?.."
    "Я бросаю вопросительный взгляд на Анти."
    "Он лишь молча виляет хвостом."
    "Я нажимаю на уведомление, чтобы его открыть."

    scene stat_159 with fade
    pause
    "Ничего себе..."

    scene img32 with fade
    show sprite_masha_neutral at masha_pos
    e "Это ты мне прислал?"
    hide sprite_masha_neutral

    play sound "audio/gav.wav" volume 0.7

    "..."
    "Теперь, благодаря Анти, я знаю, что тот тип оказался мошенником."
    "Стало неприятно."
    "А если бы он не залаял?.. Что тогда?"

    play sound "audio/notification.wav"
    "Вслед за первым уведомлением приходит и второе."

    scene stat_172_3 with fade
    pause

    scene img32 with fade
    show sprite_masha_sad at masha_pos
    e "Так это всё-таки и правда была финансовая пирамида?"
    e "Я думала, сейчас на такое уже никто не ведётся..."
    hide sprite_masha_sad

    "..."

    show sprite_masha_neutral at masha_pos
    e "Ты всё это время мог просто присылать мне уведомления?.."
    play sound "audio/false_answer.wav"
    pause 2.0

    e "Не суть."
    e "Спасибо, Анти."
    e "Только в следующий раз предупреждай меня заранее, а то уедем мы с тобой в места не столь отдалённые..."
    hide sprite_masha_neutral

    "Анти тыкает меня головой в бок, и я ласково глажу его по спинке."
    "Поднимаюсь наконец с пола, отряхиваюсь и улыбаюсь своему маленькому другу."

    stop music
    jump work_barista

label pyramida_reveal_C:
    "Анти трясет головой, словно прося отпустить его."
    scene anti_view_angry with fade
    "На его дисплее появляется какой-то новый символ."
    scene img32 with fade

    $ anti_warning_seen = True

    show sprite_masha_sad at masha_pos
    e "И что это значит?"
    e "Анти, ты можешь текстом показывать? Я эти пиктограммы не понимаю!"
    hide sprite_masha_sad

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    pause 1.0
    hide sprite_anti_angry

    show sprite_masha_scary at masha_pos, exit_right
    e "Ой!"
    hide sprite_masha_scary

    "Я дёргаюсь от неожиданности, теряю равновесие и падаю."

    show sprite_masha_angry at masha_pos
    e "Анти! Предупреждать надо."
    hide sprite_masha_angry

    show sprite_anti_kind at small_left_pos
    anti "..."
    hide sprite_anti_kind

    "Анти подходит ко мне, тычется носом в колено, а потом снова поднимает голову и начинает вилять хвостом, будто чего-то ждет."
    "Видимо, момента, когда я наконец догадаюсь..."

    show sprite_masha_sad at masha_pos
    e "..."
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Так, ладно."
    e "Когда мы только встретились, ты сказал, что будешь меня защищать. Поэтому я и назвала тебя «Анти»."
    e "Ну, знаешь... что-то вроде... Антивируса?"
    hide sprite_masha_neutral

    play sound "audio/true_answer.wav"

    show sprite_masha_neutral at masha_pos
    e "Хорошо, но при чём тут этот мужчина?"
    hide sprite_masha_neutral

    "Анти склоняет голову набок и поджимает хвост, будто размышляя, как бы ещё мне подсказать."

    show sprite_masha_confused at masha_pos
    e "Блин, думай, Маша, думай!"
    hide sprite_masha_confused

    show sprite_masha_neutral at masha_pos
    e "Эм, он — вирус?.."
    hide sprite_masha_neutral

    play sound "audio/false_answer.wav"

    show sprite_masha_neutral at masha_pos
    e "Ну да, вирусы в одежде, наверное, не ходят..."
    e "..."
    e "Он мошенник, что ли?"
    hide sprite_masha_neutral

    show sprite_anti_kind at small_left_pos
    play sound "audio/true_answer.wav"
    "Анти вскакивает и принимается радостно носиться вокруг меня кругами."
    hide sprite_anti_kind

    show sprite_masha_fun at masha_pos
    e "Да? Ты умеешь и такое?"
    e "Какой ты молодец, Анти!"
    hide sprite_masha_fun

    scene img9 with fade
    "На его дисплее на несколько секунд появляется значок загрузки, а затем я слышу знакомый звук..."
    scene img32 with fade

    play sound "audio/notification.wav"
    pause 1.0
    "Источником звука был не Анти, значит..."
    "Я вспоминаю, что всё это время у меня в кармане лежал телефон."

    show img16 with dissolve
    pause 1.5
    "На экране высвечивается уведомление. Странно..."
    "На этом кирпиче же вроде нет никаких приложений кроме карты?.."
    "Я бросаю вопросительный взгляд на Анти."
    "Он лишь молча виляет хвостом."
    "Я нажимаю на уведомление, чтобы его открыть."

    scene stat_159 with fade
    pause
    "Ничего себе..."

    scene pyramid_inside_video with fade
    show sprite_masha_neutral at masha_pos, move_from_right
    e "Это ты мне прислал?"

    play sound "audio/gav.wav" volume 0.7
    pause 1.5

    "..."
    "Теперь, благодаря Анти, я знаю, что тот тип оказался мошенником."
    "Стало неприятно."
    "А если бы он не залаял?.. Что тогда?"
    hide sprite_masha_neutral

    play sound "audio/notification.wav"
    "Вслед за первым уведомлением приходит и второе."

    scene stat_172_3 with fade
    pause

    scene pyramid_inside_video with fade
    show sprite_masha_sad at masha_pos, move_from_right
    e "Так это всё-таки и правда была финансовая пирамида?"
    e "Я думала, сейчас на такое только моя бабушка могла бы повестись, а в итоге сама чуть не... Погоди..."
    hide sprite_masha_sad
    "..."

    show sprite_masha_neutral at masha_pos
    e "Ты всё это время мог просто присылать мне уведомления?.."

    play sound "audio/false_answer.wav"
    pause 2.0

    e "Не суть."
    e "Спасибо, Анти."
    e "Только в следующий раз предупреждай меня заранее, а то уедем мы с тобой в места не столь отдалённые..."
    hide sprite_masha_neutral

    "Анти тыкает меня головой в бок, и я ласково глажу его по спинке."
    "Поднимаюсь наконец с пола, отряхиваюсь и улыбаюсь своему маленькому другу."

    show sprite_masha_fun at masha_pos
    e "Ну что, помощник, пойдём дальше?"
    e "Только этого товарища-мошенника надо обойти как-нибудь."
    hide sprite_masha_fun

    stop music
    jump work_barista

label pyramida_reveal_D:
    "Анти трясет головой, словно прося отпустить его."
    "На его дисплее появляется какой-то новый символ."

    $ anti_warning_seen = True

    show sprite_masha_sad at masha_pos
    e "И что это значит?"
    e "Анти, ты можешь текстом показывать? Я эти пиктограммы не понимаю!"
    hide sprite_masha_sad

    show sprite_anti_angry at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    hide sprite_anti_angry

    show sprite_masha_scary at masha_pos, exit_right
    e "Ой!"
    hide sprite_masha_scary

    "Я дёргаюсь от неожиданности, теряю равновесие и падаю."

    show sprite_masha_angry at masha_pos
    e "Анти! Предупреждать надо."
    hide sprite_masha_angry

    show sprite_anti_kind at small_left_pos
    anti "..."
    hide sprite_anti_kind

    "Анти подходит ко мне, тычется носом в колено, а потом снова поднимает голову и начинает вилять хвостом, будто чего-то ждет."
    "Видимо, момента, когда я наконец догадаюсь..."

    show sprite_masha_sad at masha_pos
    e "..."
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Так, ладно."
    e "Когда мы только встретились, ты сказал, что будешь меня защищать."
    e "Поэтому я и назвала тебя «Анти»."
    e "Ну, знаешь... что-то вроде... Антивируса?"
    hide sprite_masha_neutral

    play sound "audio/true_answer.wav"

    show sprite_masha_neutral at masha_pos
    e "Хорошо, но при чём тут этот мужчина?"
    hide sprite_masha_neutral

    "Анти склоняет голову набок и поджимает хвост, будто размышляя, как бы ещё мне подсказать."

    show sprite_masha_confused at masha_pos
    e "Блин, думай, Маша, думай!"
    hide sprite_masha_confused

    show sprite_masha_neutral at masha_pos
    e "Эм, он — вирус?.."
    hide sprite_masha_neutral

    play sound "audio/false_answer.wav"

    show sprite_masha_neutral at masha_pos
    e "Ну да, вирусы в одежде, наверное, не ходят..."
    e "..."
    e "Он мошенник?"
    hide sprite_masha_neutral

    show sprite_anti_kind at small_left_pos
    play sound "audio/true_answer.wav"
    "Анти вскакивает и принимается радостно носиться вокруг меня кругами."
    hide sprite_anti_kind

    show sprite_masha_fun at masha_pos
    e "Да? Ты умеешь и такое?"
    e "Какой ты молодец, Анти!"
    hide sprite_masha_fun

    scene img9 with fade
    "На его дисплее на несколько секунд появляется значок загрузки, а затем я слышу знакомый звук..."
    scene img32

    play sound "audio/notification.wav"
    pause 1.0
    "Источником звука был не Анти, значит..."
    "Я вспоминаю, что всё это время у меня в кармане лежал телефон."

    show img16 with dissolve
    pause 1.5
    "На экране высвечивается уведомление. Странно..."
    "На этом кирпиче же вроде нет никаких приложений кроме карты?.."
    "Я бросаю вопросительный взгляд на Анти."
    "Он лишь молча виляет хвостом."
    "Я нажимаю на уведомление, чтобы его открыть."

    scene stat_159 with fade
    pause
    "Ничего себе..."

    scene pyramid_inside_video with fade
    show sprite_masha_neutral at masha_pos, move_from_right
    e "Это ты мне прислал?"
    play sound "audio/gav.wav" volume 0.7
    pause 1.5
    "..."
    "Теперь, благодаря Анти, я знаю, что тот тип оказался мошенником."
    "Стало неприятно."
    "А если бы он не залаял?.. Что тогда?"
    hide sprite_masha_neutral

    play sound "audio/notification.wav"
    "Вслед за первым уведомлением приходит и второе."

    scene stat_172_3 with fade
    pause

    scene pyramid_inside_video with fade
    show sprite_masha_sad at masha_pos, move_from_right
    e "Так это всё-таки и правда была финансовая пирамида?"
    e "Я думала, сейчас на такое только моя бабушка могла бы повестись, а в итоге сама чуть не... Погоди..."
    hide sprite_masha_sad
    "..."

    show sprite_masha_neutral at masha_pos
    e "Ты всё это время мог просто присылать мне уведомления?.."
    play sound "audio/false_answer.wav"
    pause 2.0

    e "Не суть."
    e "Спасибо, Анти."
    e "Только в следующий раз предупреждай меня заранее, а то уедем мы с тобой в места не столь отдалённые..."
    hide sprite_masha_neutral

    "Анти тыкает меня головой в бок, и я ласково глажу его по спинке."
    "Поднимаюсь наконец с пола, отряхиваюсь и улыбаюсь своему маленькому другу."

    show sprite_masha_fun at masha_pos
    e "Ну что, помощник, пойдём дальше?"
    e "Только этого товарища-мошенника надо обойти как-нибудь."
    hide sprite_masha_fun

    stop music
    jump work_barista

label work_barista:
    scene black with fade
    pause 1.0
    scene img_barista_cafe with fade
    pause 1.0
    play sound "audio/foot_step.wav"

    show sprite_masha_neutral at masha_pos, move_from_right
    e "Насколько я помню, нас с тобой звали поработать в кофейню."
    e "Это она и есть?"
    hide sprite_masha_neutral

    show sprite_anti_kind at small_left_pos
    play sound "audio/gav.wav" volume 0.7
    hide sprite_anti_kind

    show sprite_masha_fun at masha_pos
    e "Как всегда в точку, Анти."
    hide sprite_masha_fun

    "Работа обещает быть приятной — мне всегда хотелось попробовать себя в роли бариста, да и само заведение нравится мне с первого взгляда."
    "После нескольких часов, проведённых в павильонах, это место кажется мне настоящим оазисом."

    play music "audio/pyramid.ogg"
    show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left
    cofe "Добрый день, что для Вас?"
    hide sprite_barista

    show sprite_masha_fun at masha_pos
    e "Добрый! А я по поводу работы..."
    hide sprite_masha_fun

    show sprite_barista at Position(xalign=0.2, yalign=1.2)
    cofe "О, точно, помню Вас!"
    hide sprite_barista

    "Меня слегка передергивает."
    "Слишком уж многие сегодняшние неприятности начинались с этой фразы."
    "Но ему я почему-то доверяю."

    show sprite_barista at Position(xalign=0.2, yalign=1.2)
    cofe "..."
    hide sprite_barista

    show sprite_masha_surprised at masha_pos
    e "..."
    e "Нет-нет, ничего такого! Просто фраза... Долгая история."
    hide sprite_masha_surprised

    show sprite_barista at Position(xalign=0.2, yalign=1.2), exit_left
    cofe "..."
    cofe "Понял."
    cofe "Ладно, проходи за стойку. Как раз пробежимся по азам, пока гостей нет."
    hide sprite_barista
    pause 1.0
    stop music

    scene black with Dissolve(.5)
    pause 1.5
    scene img_barista_cafe with Dissolve(.5)
    play music "audio/cafe.ogg"
    pause 1.5

    "Я надеваю фартук и захожу за стойку."
    "Парень объясняет всё очень понятно и совсем не раздражается, даже когда я по нескольку раз переспрашиваю о сложных моментах."
    "Труднее всего оказывается научиться правильно взбивать молоко. Все остальное получается почти с первой попытки, и я несказанно этому радуюсь." 
    "Ведь это значит, что если..."
    "...Когда."
    "Когда я вернусь в свой мир, смогу попробовать устроиться на подработку в кафе."
    "Эта перспектива нравится мне куда больше, чем раздавать листовки на улице или расклеивать по дворам странные объявления."

    show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left
    cofe "Ты умница! Сейчас как раз подходит время, когда начинается вторая волна заказов."
    cofe "Будешь у меня на подхвате."
    hide sprite_barista

    show sprite_masha_neutral at masha_pos, move_from_right
    e "Хорошо!"
    hide sprite_masha_neutral

    "Мне немного страшно: вдруг не успею или где-нибудь ошибусь?"
    "Но отступать уже поздно, да и некрасиво это как-то."
    "Сделав глубокий вдох, я приступаю к работе."

    # МИНИ-ИГРА: свари 3 вида кофе, нажимая ингредиенты в правильном порядке (шпаргалка
    # с рецептами видна всё время). См. game/coffee_game.rpy.
    pause 0.5
    call screen coffee_game_screen

    $ coffee_result = _return

    scene img_barista_cafe with fade
    pause 0.5

    if coffee_result["mistakes"] == 0:
        play sound "audio/true_answer.wav"
        show sprite_masha_fun at masha_pos, move_from_right
        e "Готово, готово и ещё раз готово!"
        hide sprite_masha_fun
        show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left
        cofe "Ни одной ошибки. Быстро учишься."
        hide sprite_barista
    else:
        play sound "audio/true_answer.wav"
        show sprite_masha_fun at masha_pos, move_from_right
        e "Ух, вроде разобралась!"
        hide sprite_masha_fun
        show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left
        cofe "Пару раз перепутала порядок, но результат неплохой для первого дня."
        hide sprite_barista

    scene black with Dissolve(.5)
    pause 1.5
    scene img_barista_cafe with Dissolve(.5)
    play music "audio/cafe.ogg"
    pause 1.5
    
    "Руки перестают дрожать только ближе к середине смены, поэтому большинство ошибок я допускаю именно в первые часы."
    "В остальном всё проходит отлично."
    "К концу рабочего дня морально я чувствую себя даже лучше, чем когда только заходила в это кафе."
    "А вот физически выматываюсь так, что едва держусь на ногах."
    "Впрочем, вот кто действительно прекрасно провёл время — так это Анти."
    "Всю мою смену он мирно спит под стойкой, свернувшись калачиком."

    scene img_barista_cafe with fade
    show sprite_barista at Position(xalign=0.2, yalign=1.2), move_from_left
    cofe "Хорошо поработали."
    cofe "Позвал бы тебя на постоянную работу."
    cofe "Но тебе, насколько я понял, нужно было только на сегодня?"
    hide sprite_barista

    show sprite_masha_sad at masha_pos
    e "Надеюсь, что да."
    hide sprite_masha_sad

    "Мужчина смотрит на меня с грустью, будто пытаясь понять, что со мной произошло."
    "Но расспрашивать не начинает, и за это я ему очень благодарна."

    show sprite_barista at Position(xalign=0.2, yalign=1.2)
    cofe "Ладненько, но ты приходи, если что."
    cofe "Для тебя у меня работа всегда найдётся."
    cofe "Сейчас отдам тебе твою зарплату."
    hide sprite_barista

    "Точно, зарплата! Я настолько устала, что без этого напоминания наверняка ушла бы, так и не забрав ни копейки за свою работу."
    "Мужчина открывает кассу, берёт две купюры и протягивает мне, тепло улыбаясь."
    "Приняв деньги, я расправляю их и вижу..."

    show sprite_masha_surprised at masha_pos
    e "Ничего себе! Полторы тысячи?"
    hide sprite_masha_surprised

    show sprite_masha_fun at masha_pos
    e "Спасибо огромное!"
    hide sprite_masha_fun

    show sprite_barista at Position(xalign=0.2, yalign=1.2), exit_left
    cofe "Тебе спасибо. Бывай."
    hide sprite_barista

    "Я бужу Анти, мы прощаемся с владельцем кафе и направляемся к выходу из «Пирамиды»."
    stop music fadeout 3.0
    jump act_four

label act_four:
    scene black with Dissolve(0.8)
    pause 1.0
    play music "audio/welcome_to_the_city.ogg"
    scene night_pyramid_entry_video with Dissolve(0.8)
    pause 1.0

    show sprite_masha_sad at masha_pos, move_from_right
    e "Что ж..."
    hide sprite_masha_sad

    play sound "audio/gav.wav" volume 0.7

    show sprite_masha_sad at masha_pos
    e "И снова в точку, Анти. Ночевать нам всё ещё негде."
    hide sprite_masha_sad

    "Я засовываю руки в карманы худи и задумчиво вглядываюсь в здание торгового центра."

    show sprite_masha_sad at masha_pos
    e "Как думаешь, Анти, если мы снова заявимся в то кафе, где ночевали, — нас сразу выставят или дадут попробовать договориться?"
    hide sprite_masha_sad

    play sound "audio/dog_skulezh.wav"

    show sprite_masha_sad at masha_pos
    pause 1.0
    e "Вот и я так думаю."
    e "Что делать-то будем?"
    hide sprite_masha_sad

    "На дисплее Анти пару секунд крутится колечко загрузки, а затем тот начинает пятиться в сторону, неуверенно глядя на меня."
    "Направляется он в сторону входа в парк."

    show sprite_masha_sad at masha_pos
    e "Ты предлагаешь переночевать на скамейке в парке?"
    hide sprite_masha_sad

    "Анти на пару секунд замер, как будто не зная, нужно ли отвечать на этот вопрос."
    play sound "audio/true_answer.wav"

    show sprite_masha_sad at masha_pos
    e "Ладно. Только давай сначала тебя подзарядим, а то вырубишься у меня. Я даже не знаю, где у тебя индикатор зарядки..."
    hide sprite_masha_sad

    "Анти дёргает ушами и склоняет голову набок. Наверняка сам думает о том, где же у него расположен индикатор."

    show sprite_masha_neutral at masha_pos
    e "Забей, пойдём поищем эту зарядную станцию. Техник сказал, что они по всему городу понатыканы."
    hide sprite_masha_neutral

    scene black with fade
    pause 1.0
    play sound "audio/foot_step.wav"
    stop music

    play music "audio/city_park.wav"

    scene charging_video with fade
    "Станцию мы находим довольно быстро. Правда, находится она в какой-то подворотне."
    "Я подхожу ближе и, прочитав небольшую инструкцию на голограмме, кладу в приёмник купюру в сто рублей."
    "На панели станции загорается схема с разноцветными разъёмами - судя по всему, подключать нужно самой, и лучше не перепутать провода."

    # МИНИ-ИГРА: соединить провода одного цвета, чтобы правильно подключить Анти к
    # зарядке (см. game/wire_game.rpy)
    call wire_game_rounds from _call_wire_game_rounds_charging

    "Провода наконец сходятся куда нужно, и голограмма мигает зелёным - подключение прошло успешно."
    "Анти остается только забраться внутрь и ждать, принимая электрические ванны."
    "Меня же больше заинтересовал автомат со снэками. Я подхожу к нему, и передо мной встает самый сложный выбор за сегодняшний день..."
    pause 1.0

    menu:
        "Странные чипсы":
            $ act_four_snack = "чипсов"
        "Непонятный батончик":
            $ act_four_snack = "батончика"
        "Загадочная шоколадка":
            $ act_four_snack = "шоколадки"

    play sound "audio/coin.mp3"
    "Я покупаю себе пачку [act_four_snack] незнакомой мне марки и усаживаюсь прямо на асфальт, оперевшись спиной к стенке зарядной станции."

    show sprite_masha_neutral at masha_pos, move_from_right
    e "Весёлый сегодня день. В моём городе нет больших торговых центров, так что я впервые была в таком месте."
    hide sprite_masha_neutral

    show sprite_masha_sad at masha_pos
    e "Ну, хотя не совсем. Когда я была маленькой, мы с родителями иногда выезжали в торговый центр."
    hide sprite_masha_sad

    show sprite_masha_neutral at masha_pos
    e "Сейчас я знаю, что он достаточно стрёмный и маленький, но тогда он казался мне очень большим. Большим и красивым."
    hide sprite_masha_neutral

    play sound "audio/notification.wav"
    "Через некоторое время — примерно через десять минут — станция издает короткий писк, оповещая о конце цикла зарядки. Я немного вздрагиваю, выдернутая из потока своих мыслей."

    show sprite_masha_neutral at masha_pos
    e "Так быстро. У меня телефон дольше заряжается, хотя он значительно меньше тебя."
    hide sprite_masha_neutral

    "Я окидываю взглядом довольного Анти, размахивающего хвостом."

    show sprite_masha_fun at masha_pos
    e "Хотя у тебя и зарядочка-то куда крупнее по габаритам."
    hide sprite_masha_fun

    show sprite_masha_neutral at masha_pos
    e "Ладно, другого выбора нет, Анти. Пойдем в парк."
    e "А завтра с тобой что-нибудь придумаем."
    e "Пообещай, что будешь меня охранять, хорошо?"
    hide sprite_masha_neutral

    play sound "audio/gav.wav" volume 0.7

    # Картинка 38 - Маша и Анти уходят из подворотни (арт ожидается).
    scene black with fade
    pause 1.0

    "Пусть я и сказала Анти, что мы будем придумывать какой-то план уже завтра. В моей голове не прекращается ураган из разного рода мыслей."
    "Как долго это будет продолжаться? За что зацепиться? Кто такой этот загадочный Борис Евгеньевич? И самое главное — как мне вернуться домой?.."

    scene black with fade
    pause 1.0
    scene bankomat_video with fade
    pause 1.0
    "Я ласково треплю друга за ухом и сажусь на лавочку, с облегченным вздохом вытягивая ноги."
    
    pause 1.0
    show bankomat_video:
        blur 0.0
        zoom 1.0
    with Dissolve(.5)

    show bankomat_video:
        linear 4.0 blur 35.0 zoom 1.03
    pause 4

    play sound "audio/foot_step.wav"
    show bankomat_video:
        blur 35.0
        zoom 1.03
        linear 0.12 blur 0.0 zoom 1.0
    pause 0.3

    scene bankomat_video
    
    "Я только прикрываю глаза, как слышу странные звуки."
    stop sound
    
    show sprite_bankomat at Position(xalign=0.2, yalign=1.2), move_from_left
    bankomat "Девочка! Слушай, помоги пожалуйста!"
    hide sprite_bankomat
    
    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Что случилось? Вы в порядке?"
    hide sprite_masha_scary
    
    "Я подскакиваю со скамьи, а Анти так же перепугано начинает наворачивать круги вокруг лавочки."
    
    show sprite_bankomat at Position(xalign=0.2, yalign=1.2)
    bankomat "Тише-тише. Мне нужна твоя помощь."
    hide sprite_bankomat
    
    "Я чувствую легкое раздражение."
    "Мне просто хочется уже поспать, чтобы этот день наконец закончился."
    
    show sprite_bankomat at Position(xalign=0.2, yalign=1.2)
    bankomat "Я не могу перевести деньги со своей банковской карты."
    bankomat "Помоги мне. Там сто тысяч рублей."
    bankomat "Я готов заплатить тебе за помощь 40%% от этой суммы."
    bankomat "Это правда очень срочно. Прошу помоги!"
    hide sprite_bankomat
    
    "Я уже хочу отказаться, но телефон в кармане вибрирует. Мне приходит уведомление."
    
    pause 1.0
    show img16 with Dissolve(.5)
    pause 1.5
    "На экране горит текст: «Вам предоставляется возможность заработать. Создать карту ради срочной ситуации?». Ниже — две кнопки."

    play sound "audio/notification.wav"
    "Не успеваю нажать ни на одну из них, как экран сам съезжает в сторону, открывая какое-то мини-приложение."

    # МИНИ-ИГРА: memory на банковских картах, 3 уровня подряд (6/8/12 карт). См.
    # game/memory_game.rpy.
    call screen memory_game_screen

    $ memory_result = _return
    "Игра исчезает так же внезапно, как появилась, и на экране снова высвечивается тот же вопрос про карту."

    scene bankomat_video with fade
    menu:
        "Что делать?"
        "Согласиться.":
            jump bankomat_agree
        "Отказаться.":
            jump bankomat_refuse

label bankomat_agree:
    scene black
    pause 1.0
    scene bankomat_video
    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Хорошо, давайте."
    hide sprite_masha_neutral
    
    "Я тяжело вздыхаю и соглашаюсь, нажимая на соответствующий вариант."
    "В конце концов, нам с Анти нужны деньги."
    "Может, правда, получу свои сорок процентов."
    
    show sprite_bankomat at Position(xalign=0.2, yalign=1.2)
    bankomat "Готово, я тебе перевел. Мне нужно, чтобы ты отправила эту сумму по пяти другим номерам."
    hide sprite_bankomat
    
    "Теперь ситуация кажется странной и сомнительной, но я все равно делаю так, как мне сказали."
    play sound "audio/white_noise.mp3"
    scene bankomat_video
    show bankomat_video:
        blur 0.0
        zoom 1.0
        linear 4.0 blur 35.0 zoom 1.03

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 5.0
    stop music

    play music "audio/negative_ending.wav"
    play sound "audio/white_noise.mp3" loop
    scene black
    pause 0.5
    window hide

    show text "{size=80}ВЫ ПОПАЛИСЬ НА УЛОВКУ И СТАЛИ СОУЧАСТНИКОМ МОШЕННИКОВ!{/size}" at truecenter:
        alpha 0.0
        linear 1.5 alpha 1.0
    pause
    stop sound
    
    scene stat_187_2 with Dissolve(.5)
    pause
    scene black with fade
    pause 1.0

    play music "audio/glamour_networks.wav"
    scene curators_lair_video with fade
    pause 1.0
    kurator "Ха-ха, какая глупышка."
    kurator "Повезло выйти из «Пирамиды» целенькой, не встретившись с ее Заведующим."
    kurator "А тут на самую простую уловку попалась."
    kurator "А ты говорил, что она умнее, чем выглядит."

    zlicev "Возможно, я ошибался. Принял вежливость за ум."
    
    play sound "audio/female_laugh.wav"
    stop music

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 5.0

    show text "{size=50}{color=#ffffff}Продолжение следует...{/color}{/size}" at truecenter:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 4.0

    hide text
    pause 1.0
    return

label bankomat_refuse:
    scene black
    pause 1.0
    scene bankomat_video
    show sprite_masha_angry at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Нет, всё! Меня не интересует это, не хочу я заводить никакую карту!"
    hide sprite_masha_angry
    
    show sprite_bankomat at Position(xalign=0.2, yalign=1.2), move_from_left, exit_left
    bankomat "Ты чего?! Я же сказал, что мне срочно. Еще и предложил такую огромную сумму!"
    
    show sprite_masha_scary at Position(xalign=0.8, yalign=-0.8), exit_right
    "Незнакомец начинает агрессивно подходить ко мне ближе, а я оглядываюсь вокруг, думая, куда бежать."
    hide sprite_masha_scary
    
    play sound "audio/growl_short.wav" loop
    pause 1.5
    show sprite_anti_angry at Position(xalign=0.8, yalign=1.05), move_from_right
    pause 1.5
    "Мужчина пятится назад, напуганный внезапной агрессивностью робо-пса."
    "А Анти лишь громче рычит и медленно идет на незнакомца."
    pause 1.5
    hide sprite_bankomat
    stop sound

    "В итоге мужчина уходит, почти что убегает, когда понимает, что Анти настроен серьезно."
    "А я облегченно выдыхаю."
    hide sprite_anti_angry
    
    show sprite_masha_neutral at Position(xalign=0.8, yalign=-0.8), move_from_right
    e "Спасибо, Анти. Без тебя я не знаю, что случилось бы."
    hide sprite_masha_neutral
    
    scene bankomat_video with fade
    "Я поднимаю пса к себе на скамью и сама ложусь рядом, всё еще периодически вздрагивая."
    "Со временем я успокаиваюсь и незаметно засыпаю."
    scene bankomat_video
    show bankomat_video:
        blur 0.0
        zoom 1.0
        linear 4.0 blur 35.0 zoom 1.03

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 5.0
    stop music

    play music "audio/glamour_networks.wav"
    scene curators_lair_video with fade
    pause 1.0
    kurator "Удачливая девочка."
    kurator "Повезло выйти из «Пирамиды» целенькой, не встретившись с ее Заведующим."
    kurator "Так еще и пёс охраняет ее от моих агентов."
    kurator "Ты правильно сказал, что она не такая уж и глупая."
    zlicev "Нужно что-то с ней делать."
    kurator "Или как минимум с псом. Меня начинает это раздражать."
    zlicev "Услышал Вас."
    stop music fadeout 5.0
    
    scene curators_lair_video
    show curators_lair_video:
        blur 0.0
        zoom 1.0
        linear 4.0 blur 35.0 zoom 1.03

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 5.0

    show text "{size=70}{color=#c87eff}ВЫ НЕ ПОДДАЛИСЬ МОШЕННИКАМ!{/color}{/size}" at truecenter:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 3.0

    hide text
    pause 0.5

    show text "{size=50}{color=#ffffff}Продолжение следует...{/color}{/size}" at truecenter:
        alpha 0.0
        linear 2.0 alpha 1.0
    pause 4.0

    hide text
    pause 1.0
    return