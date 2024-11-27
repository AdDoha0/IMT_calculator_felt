
import flet as ft

def main(page: ft.Page):
    page.title = "Список задач"
    page.window_width = 460
    page.window_height = 550


    def add_new_task(e):
        if new_task_form.value =="":
            print("Добавте задачу")
        else:
            page.add(ft.Checkbox(label=new_task_form.value))
            new_task_form.value = ""
            new_task_form.focus()
            new_task_form.update()

    new_task_form = ft.TextField(hint_text="Введите новую задачу", width=300)
    button_add = ft.ElevatedButton("Добавить", on_click=add_new_task)

    page.add(ft.Row(controls=[new_task_form, button_add]))


ft.app(target=main)