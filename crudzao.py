import flet as ft

# Estrutura de dados para armazenar as informações das pessoas
people_data = []

def main(page: ft.Page):
    # Função para adicionar uma nova pessoa ao cadastro
    def add_person(e):
        id_ = len(people_data) + 1
        name = txt_name.value
        email = txt_email.value
        cpf = txt_cpf.value
        people_data.append({"id": id_, "name": name, "email": email, "cpf": cpf})
        txt_name.value = ""  # Limpa os campos após adicionar
        txt_email.value = ""
        txt_cpf.value = ""
        page.update()

    # Função para exibir todas as pessoas cadastradas
    def view_people(e):
        content = ""
        for person in people_data:
            content += f"{person['id']}, {person['name']}, {person['email']}, {person['cpf']}\n"
        page.add(ft.Text(content))

    # Função para atualizar uma pessoa existente
    def update_person(e):
        id_ = int(txt_id.value)
        name = txt_name.value
        email = txt_email.value
        cpf = txt_cpf.value
        for i, person in enumerate(people_data):
            if person["id"] == id_:
                people_data[i] = {"id": id_, "name": name, "email": email, "cpf": cpf}
                break
        page.update()

    # Função para deletar uma pessoa pelo ID
    def delete_person(e):
        id_ = int(txt_id.value)
        for i, person in enumerate(people_data):
            if person["id"] == id_:
                del people_data[i]
                break
        page.update()

   # Funções para manipulação de arquivos CSV
    def export_to_csv(event):  # Adicione o parâmetro event aqui
        import csv
        with open('people.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "CPF"])
            for person in people_data:
                writer.writerow([person["id"], person["name"], person["email"], person["cpf"]])

    # Campos de entrada para adicionar uma nova pessoa
    txt_name = ft.TextField(label="Nome")
    txt_email = ft.TextField(label="Email")
    txt_cpf = ft.TextField(label="CPF")
    txt_id = ft.TextField(label="ID")

    # Botões para operações CRUD
    btn_add = ft.ElevatedButton("Adicionar Pessoa", on_click=add_person)
    btn_view = ft.ElevatedButton("Ver Pessoas", on_click=view_people)
    btn_update = ft.ElevatedButton("Atualizar Pessoa", on_click=update_person)
    btn_delete = ft.ElevatedButton("Deletar Pessoa", on_click=delete_person)
    btn_export = ft.ElevatedButton("Exportar para CSV", on_click=export_to_csv)  # Ajuste feito aqui

    # Adicionando elementos à página
    page.add(
        txt_name,
        txt_email,
        txt_cpf,
        txt_id,
        btn_add,
        btn_view,
        btn_update,
        btn_delete,
        btn_export
    )

# Executando o aplicativo
ft.app(main)
