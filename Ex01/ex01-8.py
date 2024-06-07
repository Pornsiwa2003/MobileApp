import flet as ft

def main(page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    first_name.disabled = True
    last_name.disabled = True
    page.add(first_name, last_name)
ft.app(target=main)