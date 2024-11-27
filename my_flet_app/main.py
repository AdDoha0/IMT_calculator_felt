
import flet as ft

def main(page: ft.Page):

    # настройки страницы
    page.window_width = 400
    page.window_height = 550
    page.theme_mode = "dark"



    def close_banner(e):
        page.banner.open = False
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

    # баннер с предупреждением об отсутствии заполненных полей
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER, color=ft.colors.AMBER, size=40),
        content=ft.Text("Упс, вы заполнили все поля?"),
        actions=[ft.TextButton('OK', on_click=close_banner)]
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
    button_calculated =  ft.ElevatedButton(text="Рассчитать IMT")

    # информация о IMT
    imt = ft.Text("Тут текст", size=30)
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
            imt,
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