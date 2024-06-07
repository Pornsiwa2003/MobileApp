import flet as ft
class MyButton(ft.ElevatedButton)
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text     
def main(page: ft.Page):

    page.add(MyButton(text="OK"), MyButton(text="Cancel"))

ft.app(target=main)
