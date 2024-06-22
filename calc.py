import flet
from flet import IconButton, Page, Row, TextField, Column, ElevatedButton

def main(page: Page):
    page.title = "Dundun Simple Calculator"
    page.window_width = 400  # Ajustando o tamanho da janela
    page.window_height = 400  # Ajustando o tamanho da janela
    
    txt_display = TextField(value="0", text_align="center", width=200, read_only=True)

    current_value = []
    
    def update_display(value):
        if value:
            current_value.append(value)
            txt_display.value = ''.join(current_value)
        else:
            current_value.clear()
            txt_display.value = "0"
        page.update()

    def button_click(e):
        update_display(e.control.text)
    
    def clear_click(e):
        update_display(None)
        
    def calculate_result(e):
        try:
            result = eval(''.join(current_value))
            txt_display.value = str(result)
            current_value.clear()
            current_value.append(str(result))
        except Exception as ex:
            txt_display.value = "Error"
            current_value.clear()
        page.update()

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]
    
    rows = []
    for row in buttons:
        rows.append(Row([ElevatedButton(text=btn, on_click=calculate_result if btn == '=' else button_click) for btn in row], alignment="center"))
    
    page.add(
        Column(
            [
                Row([txt_display], alignment="center"),  # Colocando txt_display dentro de uma Row para centralizá-lo
                Row([ElevatedButton(text="Limpar", on_click=clear_click)], alignment="center"),
                *rows
            ],
            alignment="center"  # Centralizando verticalmente todos os elementos
        )
    )

flet.app(target=main, view=flet.WEB_BROWSER)

