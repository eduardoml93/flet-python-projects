import flet as ft

def build_interface(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()  # Limpa a página atual
            page.add(ft.Text(f"Hello, {name}"))
            page.add(ft.ElevatedButton("Voltar", on_click=lambda e: rebuild_interface(page)))  # Botão de voltar
            page.update()

    def rebuild_interface(page: ft.Page):  # Função para reconstruir a interface inicial
        page.clean()
        build_interface(page)  # Reconstrói a interface inicial
        page.add(ft.Text("VOLTEI"))  # Mensagem adicional

    txt_name = ft.TextField(label="Seu name")
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))
    page.add(ft.Text("This is a simple app to say hello to you"))

ft.app(build_interface)



