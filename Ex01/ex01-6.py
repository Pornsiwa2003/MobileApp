import time
import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
ft.app(target=main)