import requests
from datetime import datetime

def convert_currency(base_currency, amount, target_currency, api_key):
    date_today = datetime.today().strftime('%Y-%m-%d')
    url = f'https://api.twelvedata.com/price?symbol={base_currency}/{target_currency}&apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'price' in data:
            rate = data['price']
            converted_amount = float(amount) * float(rate)
            return converted_amount
        else:
            return f'Ошибка: Некорректная целевая валюта'
    else:
        return 'Ошибка: Не удалось получить данные от сервера'

api_key = 'b9e54f631f2448259723d96659ed9c02'
base_currency = input('Введите изначальную валюту: ').upper()
amount = float(input('Введите количество валюты для конвертации: '))
target_currency = input('Введите целевую валюту: ').upper()

result = convert_currency(base_currency, amount, target_currency, api_key)
if isinstance(result, float):
    print(f'{amount} {base_currency} равно {result} {target_currency}')
else:
    print(result)
