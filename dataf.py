import flet as ft
import pandas as pd
import requests
from io import StringIO

def main(page: ft.Page):
    page.title = "CSV Data Viewer. Remebember to use ?raw=true in the URL!"
    page.window_width = 800
    page.window_height = 600
    page.scroll = "auto"

    def download_csv(e):
        url = txt_url.value
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = StringIO(response.text)
            df = pd.read_csv(data)
            display_dataframe(df)
        except Exception as ex:
            txt_error.value = f"Error: {ex}"
            page.update()

    def display_dataframe(df):
        page.controls.clear()
        page.controls.append(ft.Text(f"Data from CSV ({len(df)} rows):"))
        page.controls.append(ft.DataTable(
            columns=[ft.DataColumn(ft.Text(col)) for col in df.columns],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]) for row in df.itertuples(index=False)]
        ))
        page.update()

    txt_url = ft.TextField(label="CSV URL", width=600)
    btn_download = ft.ElevatedButton(text="Download and Display CSV", on_click=download_csv)
    txt_error = ft.Text(value="", color="red")

    page.add(txt_url, btn_download, txt_error)

ft.app(target=main)
