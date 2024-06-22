import requests
import flet as ft

# Substitua 'YOUR_API_KEY' pela sua chave de API obtida do ExchangeRate-API.com
API_KEY = '304d9063647ea34617562d17'

def get_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()
    conversion_rates = data['conversion_rates']
    rates = {
        'BRL': conversion_rates['BRL'],
        'EUR': conversion_rates['EUR'],
        'GBP': conversion_rates['GBP'],
        'JPY': conversion_rates['JPY'],
        'AUD': conversion_rates['AUD']
    }
    return rates

def main(page: ft.Page):
    # Configuração da página
    page.title = "Cotação do Dólar"
    page.window_height = 800
    page.window_width = 600
    
    def update_currency_rates(e):
        rates = get_exchange_rates()
        page.clean()
        
        # Símbolos das moedas
        currency_symbols = {'BRL': 'R$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'AUD': '$'}
        
        # Exibindo as taxas de câmbio com os símbolos corretos
        currencies = ['BRL', 'EUR', 'GBP', 'JPY', 'AUD']
        for currency in currencies:
            symbol = currency_symbols.get(currency, '')  # Obtém o símbolo da moeda
            rate = rates[currency]
            page.add(ft.Text(f"{currency}: {symbol}{rate:.2f}"))
    
    button = ft.ElevatedButton("Atualizar Taxa", on_click=update_currency_rates)
    page.add(button)

ft.app(main)
