import flet as ft

def main(page):

    num1 = ft.Ref[ft.TextField]()
    num2 = ft.Ref[ft.TextField]()
    results = ft.Ref[ft.Column]()

    def btn_click(e):
        try:
            number1 = float(num1.current.value)
            number2 = float(num2.current.value)
            diff = round(number1 - number2, 2)
            percent = round((diff / number1) * 100, 2)
            results.current.controls.append(
                ft.Text(f"{number1} and {number2} - [Diff: {diff}] [{percent}%]", selectable=True)
            )
            num1.current.value = ""
            num2.current.value = ""
            page.update()
            num1.current.focus()
        except ValueError:
            results.current.controls.append(ft.Text("Invalid input. Please enter valid numbers."))
            page.update()

    page.add(
        ft.TextField(ref=num1, label="First Number", autofocus=True),
        ft.TextField(ref=num2, label="Second Number"),
        ft.ElevatedButton("Difference!", on_click=btn_click),
        ft.Column(ref=results),
    )

ft.app(target=main)
