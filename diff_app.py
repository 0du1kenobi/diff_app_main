import flet as ft


def main(page):
    num1 = ft.Ref[ft.TextField]()
    num2 = ft.Ref[ft.TextField]()
    results = ft.Ref[ft.Column]()
    counter = [0]

    def btn_click(e):
        try:
            number1 = float(num1.current.value)
            number2 = float(num2.current.value)
            diff = round(number1 - number2, 2)
            percent = round((diff / number1) * 100, 2)

            counter[0] += 1  # Increasing the counter
            # Add a counter before the result text
            results.current.controls.append(
                ft.Text(f"{counter[0]}. {number1} and {number2} - [Diff: {diff}] [{percent}%]", selectable=True)
            )

            # Write the results to a file
            with open("output.txt", "a") as file:
                if counter[0] == 1:
                    file.write("___\n")
                file.write(f"{counter[0]}. {number1} and {number2} - [Diff: {diff}] [{percent}%]\n")

            num1.current.value = ""
            num2.current.value = ""
            page.update()
            num1.current.focus()
        except ValueError:
            counter[0] += 1  # Increasing the counter
            results.current.controls.append(ft.Text(f"{counter[0]}. Invalid input. Please enter valid numbers."))

            # Write the error to a file
            with open("output.txt", "a") as file:
                if counter[0] == 1:
                    file.write("___\n")
                file.write(f"{counter[0]}. Invalid input. Please enter valid numbers.\n")

            page.update()

    page.add(
        ft.TextField(ref=num1, label="First Number", autofocus=True),
        ft.TextField(ref=num2, label="Second Number"),
        ft.ElevatedButton("Difference!", on_click=btn_click),
        ft.Column(ref=results),
    )


ft.app(target=main)
