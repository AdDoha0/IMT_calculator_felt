
import flet as ft

def main(page: ft.Page):

    # настройки страницы
    page.window_width = 400
    page.window_height = 550
    page.theme_mode = "dark"



    def close_banner(e):
        page.banner.open = False
        page.update()



    # height_field weight_field gender_dropdown
    def calculate(e):
        if weight_field.value == "" or height_field.value == "" or gender_dropdown.value == "":
            page.banner.open = True
            page.update()
        else:
            weight_value = float(weight_field.value)
            height_value = float(height_field.value)

            # вычесляем IMT
            imt = weight_value / (height_value * height_value)
            imt = float(f"{imt:2f}")

            # отоброзить значение IMT
            imt_views.value = f"IMT - {imt}"


        # очистить поля
        weight_field.value = ""
        height_field.value = ""
        gender_dropdown.value = ""

        # обновить страницу
        page.update()

    # appbar приложения (самая верхняя часть)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Калькулятор IMT"),
        center_title=False,
        bgcolor="#1E1E2F",
        color="#CCCCCC"
        )



    page.banner = ft.Banner(
    bgcolor="#2A2A2F",  # Темно-синий фон
    leading=ft.Icon(ft.icons.WARNING_AMBER, color="#CCCCCC", size=40),  # Светло-серый значок
    content=ft.Text("Упс, вы заполнили все поля?", color="#CCCCCC"),  # Светло-серый текст
    actions=[
        ft.TextButton(
            'OK',
            on_click=close_banner,
            style=ft.ButtonStyle(
                color="#CCCCCC",  # Цвет текста кнопки
                bgcolor="#333333"  # Цвет фона кнопки
                )
            )
            ]
        )



    height_field = ft.TextField(label="Рост", hint_text="Введите свой рост")
    weight_field= ft.TextField(label="Вес", hint_text="Введите свой вес")
    gender_dropdown = ft.Dropdown(
        label="Пол",
        hint_text="Какой у вас пол?",
        options=[
            ft.dropdown.Option("Мужчина"),
            ft.dropdown.Option("Женщина"),
        ]
        )
    button_calculated =  ft.ElevatedButton(text="Рассчитать IMT", on_click=calculate)

    # информация о IMT
    imt_views = ft.Text("Проверим тебя?", size=30)
    details = ft.Text("Введите свои данные", size=20)

    # главное изоброжение, которе видим в первую очередь
    img_main = ft.Image(
        src="img/fat-body.png",
        width=100,
        height=100,
        fit=ft.ImageFit
        )

    info_app_res = ft.Column(
        controls=[
            imt_views,
            details,
        ]
        )

    img_res = ft.Image(
        src="img/fat-body.png",
        width=100,
        height=100,
        fit=ft.ImageFit
        )

    info = ft.Row(
        controls=[
            info_app_res,
            img_res,
        ]
        )


    # Макет страницы
    layout = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=info,
                padding=5,
                col={"sm":4, "md":4, "xl":4},
                alignment=ft.alignment.center,
                ),

            ft.Container(
                content=height_field,
                padding=5,
                bgcolor="#1E1E2F",
                col={"sm":12, "md":3, "xl":3},
                ),

            ft.Container(
                content=weight_field,
                padding=5,
                bgcolor="#1E1E2F",
                col={"sm":12, "md":3, "xl":3},
                ),

            ft.Container(
                content=gender_dropdown,
                padding=5,
                bgcolor="#1E1E2F",
                col={"sm":12, "md":3, "xl":3},
                ),

            ft.Container(
                content=button_calculated,
                padding=0,
                # bgcolor="#1E1E2F",
                col={"sm":12, "md":3, "xl":3},
                ),
            ]
        )

    page.add(layout)


ft.app(target=main)