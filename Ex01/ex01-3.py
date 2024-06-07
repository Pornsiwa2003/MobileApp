import time
import flet as ft

def main(page: ft.Page):
    t = ft.Text()
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)
ft.app(target=main)