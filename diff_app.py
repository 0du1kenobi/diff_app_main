import flet as ft

def main(page):
    name = ft.Ref[ft.TextField]()
    num1 = ft.Ref[ft.TextField]()
    num2 = ft.Ref[ft.TextField]()
    results = ft.Ref[ft.Column]()
    table = ft.Ref[ft.DataTable]()
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
                ft.Text(f"{counter[0]}. {name.current.value} - [Diff: {diff}] [{percent}%]", selectable=True)
            )

            # Add the results to the table
            table.current.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(name.current.value)),
                        ft.DataCell(ft.Text(str(number1))),
                        ft.DataCell(ft.Text(str(number2))),
                        ft.DataCell(ft.Text(str(percent))),
                    ],
                ),
            )

            # Write the results to a file
            with open("output.txt", "a") as file:
                if counter[0] == 1:
                    file.write("___\n")
                file.write(f"{counter[0]}. {name.current.value} - [Diff: {diff}] [{percent}%]\n")

            name.current.value = ""
            num1.current.value = ""
            num2.current.value = ""
            page.update()
            name.current.focus()
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
        ft.Row(
            [
                ft.Column(
                    [
                        ft.TextField(ref=name, label="Name", autofocus=True),
                        ft.TextField(ref=num1, label="First Number"),
                        ft.TextField(ref=num2, label="Second Number"),
                        ft.ElevatedButton("Difference!", on_click=btn_click),
                        ft.Column(ref=results),
                    ],
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.DataTable(
                            ref=table,
                            columns=[
                                ft.DataColumn(ft.Text("Name")),
                                ft.DataColumn(ft.Text("Main")),
                                ft.DataColumn(ft.Text("Branch")),
                                ft.DataColumn(ft.Text("Diff-%"), numeric=True),
                            ],
                            rows=[],
                        ),
                    ],
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
        )
    )

ft.app(target=main)

