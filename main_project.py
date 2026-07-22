import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.window.width = 320
    page.window.height = 450

    result = ft.Text(value="0", size=45, color=ft.Colors.WHITE)

    def button_click(e):
        data = e.control.data
        current = result.value

        if data == "C":
            result.value = "0"
        elif data == "=":
            try:
                result.value = str(eval(current))
            except Exception:
                result.value = "Error"
        else:
            if current == "0":
                result.value = data
            else:
                result.value = current + data
        page.update()

    def btn(label):
        return ft.ElevatedButton(
            label,
            data = label,
            on_click = button_click,
            expand = True,
        )
    page.add(
        ft.Container(
            content = result,
            alignment = ft.Alignment.CENTER_RIGHT,
            padding = 20,
            bgcolor = ft.Colors.BLACK,
        ),
            ft.Row([btn("7"), btn("8"), btn("9"), btn("/")]),
            ft.Row([btn("4"), btn("5"), btn("6"), btn("*")]),
            ft.Row([btn("1"), btn("2"), btn("3"), btn("-")]),
            ft.Row([btn("C"), btn("0"), btn("="), btn("+")]),
    )
ft.run(main)