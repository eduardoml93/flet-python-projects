import flet
from deep_translator import GoogleTranslator
from flet import Page, TextField, ElevatedButton, Column

def translate_text(text, target_language):
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Erro na tradução: {str(e)}"

def main(page: Page):
    page.title = "Translator App"
    page.vertical_alignment = "center"
    
    # Definindo o tamanho da janela
    page.window_width = 400
    page.window_height = 300

    txt_input = TextField(value="", width=300)
    txt_output = TextField(value="", text_align="left", multiline=True, width=300, read_only=True)
    txt_target_language = TextField(value="pt", width=100)

    def translate_text_handler(e):
        text = txt_input.value.strip()
        target_language = txt_target_language.value.strip()
        
        if text and target_language:
            translation = translate_text(text, target_language)
            txt_output.value = translation
        else:
            txt_output.value = "Por favor, digite um texto e o código do idioma alvo."
        
        page.update()

    def clear_fields(e):
        txt_input.value = ""
        txt_output.value = ""
        txt_target_language.value = ""
        page.update()

    page.add(
        Column(
            [
                txt_input,
                txt_target_language,
                ElevatedButton(text="Traduzir", on_click=translate_text_handler),
                txt_output,
                ElevatedButton(text="Limpar", on_click=clear_fields)
            ],
            alignment="center"
        )
    )

flet.app(target=main)
