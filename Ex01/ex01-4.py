import time
import flet as ft

def main(page: ft.Page):
    t = ft.Text()
    page.add(
       ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ])
) 
ft.app(target=main)