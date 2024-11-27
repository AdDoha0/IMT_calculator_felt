
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

    # баннер с предупреждением об отсутствии заполненных полей
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER, color=ft.colors.AMBER, size=40),
        content=ft.Text("Упс, вы заполнили все поля?"),
        actions=[ft.TextButton('OK', on_click=close_banner)]
        )

ft.app(target=main)