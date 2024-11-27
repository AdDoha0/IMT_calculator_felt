
import flet as ft

def main(page: ft.Page):

    # настройки страницы
    page.window_width = 400
    page.window_height = 550



    def close_banner(e):
        page.banner.open = False
        page.update()

    # appbar приложения (самая верхняя часть)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Калькулятор IMT"),
        center_title=False,
        bgcolor=ft.colors.SURFACE
        )

ft.app(target=main)