import flet as ft
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

def main(page: ft.Page):
    page.title = "Web Tables Viewer"
    page.window_width = 800
    page.window_height = 600
    page.scroll = "auto"

    def extract_tables_from_page(url):
        tables_data = []
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for table in soup.find_all('table'):
            table_html = str(table)
            table_io = StringIO(table_html)
            df = pd.read_html(table_io)[0]
            tables_data.append(df)
        
        return tables_data

    def display_dataframes(tables_data):
        page.controls.clear()
        for i, df in enumerate(tables_data):
            page.controls.append(ft.Text(f"Table {i+1} - {len(df)} rows:"))
            page.controls.append(ft.DataTable(
                columns=[ft.DataColumn(ft.Text(col)) for col in df.columns],
                rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]) for row in df.itertuples(index=False)]
            ))
        page.controls.append(ft.ElevatedButton("Voltar", on_click=lambda e: rebuild_interface(page)))
        page.update()

    def rebuild_interface(page: ft.Page):
        page.controls.clear()
        build_interface(page)
        page.update()

    def build_interface(page: ft.Page):
        txt_url = ft.TextField(label="Web Page URL", width=600)
        btn_extract = ft.ElevatedButton(text="Extract Tables and Display", on_click=lambda e: display_dataframes(extract_tables_from_page(txt_url.value)))
        txt_error = ft.Text(value="", color="red")

        page.add(txt_url, btn_extract, txt_error)
        page.update()

    build_interface(page)

ft.app(target=main)
