import flet
import requests
from flet import IconButton, Page, Row, TextField, Column, ElevatedButton

# Chave da API do OpenWeatherMap
API_KEY = 'a5676ce9dbe81f9ddad2125c4dedb9b6'  # Coloque sua chave da API do OpenWeatherMap aqui

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção se houver erro na requisição
        data = response.json()
        
        # Extrair informações relevantes
        weather_description = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        country = data['sys']['country']

        # Construir a string com as informações do clima
        weather_info = f'{weather_description}\n' \
                       f'Temperatura: {temp}°C\n' \
                       f'Umidade: {humidity}%\n' \
                       f'Velocidade do vento: {wind_speed} m/s\n' \
                       f'País: {country}'
        
        return weather_info
    except requests.exceptions.HTTPError as http_err:
        return f"Erro na requisição HTTP: {http_err}"
    except Exception as err:
        return f"Erro: {err}"

def main(page: Page):
    page.title = "Weather App do Dundun"
    page.vertical_alignment = "center"
    
    # Definindo o tamanho da janela
    page.window_width = 400
    page.window_height = 350

    txt_city = TextField(value="", width=200)
    txt_weather = TextField(value="", text_align="left", multiline=True, width=300, read_only=True)

    def update_weather(e):
        city = txt_city.value.strip()
        if city:
            weather = get_weather(city)
            txt_weather.value = weather
        else:
            txt_weather.value = "Digite o nome de uma cidade"
        page.update()

    def clear_weather(e):
        txt_city.value = ""
        txt_weather.value = ""
        page.update()

    def handle_enter(e):
        if e.key == "Enter":
            update_weather(None)

    page.add(
        Column(
            [
                txt_city,
                ElevatedButton(text="Buscar Clima", on_click=update_weather),
                txt_weather,
                Row([ElevatedButton(text="Limpar", on_click=clear_weather)])
            ],

        )
    )

flet.app(target=main)
