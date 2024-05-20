# # # import requests
# # # from datetime import datetime

# # # def convert_currency(base_currency, amount, target_currency):
# # #     date_today = datetime.today().strftime('%Y-%m-%d')
# # #     print(date_today,base_currency)
# # #     url = f'https://api.exchangerate-api.com/{date_today}?base={base_currency}'
# # #     response = requests.get(url)
    
# # #     if response.status_code == 200:
# # #         data = response.json()
# # #         if target_currency in data['rates']:
# # #             rate = data['rates'][target_currency]
# # #             converted_amount = amount * rate
# # #             return converted_amount
# # #         else:
# # #             return f'Ошибка: Некорректный код целевой валюты'
# # #     else:
# # #         return f'Ошибка: Не удалось получить данные от сервера'

# # # base_currency = input('Введите изначальную валюту: ')
# # # amount = float(input('Введите количество валюты: '))
# # # target_currency = input('Введите валюту, в которую нужно перевести: ')

# # # result = convert_currency(base_currency, amount, target_currency)
# # # print(f'Результат конвертации: {result}')



# # import requests
# # from datetime import datetime

# # def convert_currency(base_currency, amount, target_currency):
# #     date_today = datetime.today().strftime('%Y-%m-%d')
# # #    url = f'https://open.er-api.com/{date_today}?base={base_currency}'
# #      url = f'https://cbr.ru'
# #     response = requests.get(url)
    
# #     if response.status_code == 200:
# #         data = response.json()
# #         if target_currency in data['rates']:
# #             rate = data['rates'][target_currency]
# #             converted_amount = amount * rate
# #             return converted_amount
# #         else:
# #             return f'Ошибка: Некорректный код целевой валюты'
# #     else:
# #         return f'Ошибка: Не удалось получить данные от сервера'

# # base_currency = input('Введите изначальную валюту: ')
# # amount = float(input('Введите количество валюты: '))
# # target_currency = input('Введите валюту, в которую нужно перевести: ')

# # result = convert_currency(base_currency, amount, target_currency)
# # print(f'Результат конвертации: {result}')



# import requests
# from datetime import datetime

# def convert_currency(base_currency, amount, target_currency, api_key):
#     date_today = datetime.today().strftime('%Y-%m-%d')
#     url = f'https://api.twelvedata.com/forex?symbol={base_currency}/{target_currency}&apikey={api_key}'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         if 'close' in data:
#             rate = data['close']
#             converted_amount = amount * rate
#             return converted_amount
#         else:
#             return f'Ошибка: Некорректный код целевой валюты'
#     else:
#         return f'Ошибка: Не удалось получить данные от сервера'

# api_key = 'b9e54f631f2448259723d96659ed9c02'
# base_currency = input('Введите изначальную валюту: ').upper()
# amount = float(input('Введите количество валюты: '))
# target_currency = input('Введите валюту, в которую нужно перевести: ').upper()

# result = convert_currency(base_currency, amount, target_currency, api_key)
# print(f'Результат конвертации: {result}')


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
            return f'Ошибка: Некорректный код целевой валюты'
    else:
        return 'Ошибка: Не удалось получить данные от сервера'

api_key = 'b9e54f631f2448259723d96659ed9c02'
base_currency = input('Введите изначальную валюту: ').upper()
amount = float(input('Введите количество валюты для конвертации: '))
target_currency = input('Введите код целевой валюты: ').upper()

result = convert_currency(base_currency, amount, target_currency, api_key)
if isinstance(result, float):
    print(f'{amount} {base_currency} равно {result} {target_currency}')
else:
    print(result)