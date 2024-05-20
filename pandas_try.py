import importlib
from datetime import datetime

def install_packages():
    try:
        importlib.import_module('openexchangerates')
    except ImportError:
        print("Библиотека 'openexchangerates' не найдена. Устанавливаю...")
        import os
        os.system('pip install openexchangerates')

def main():
    install_packages()
    # После успешной установки библиотеки, импортируем OpenExchangeRates и продолжаем ваш код
    from pandas import pd

def convert_currency(initial_currency, amount, target_currency):
    # Получаем текущую дату
    current_date = datetime.today().strftime('%d/%m/%Y')
    
    # Формируем URL для запроса к Центральному банку России
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={current_date}&date_req2={current_date}&VAL_NM_RQ={initial_currency}'
    
    # Загружаем данные с сайта ЦБ
    data = pd.read_xml(url)
    
    # Получаем курс валюты на текущую дату
    exchange_rate = data.iloc[-1]['Value']
    
    # Вычисляем количество целевой валюты
    target_amount = amount / exchange_rate

    return target_amount

# Пример использования функции
initial_currency = 'R01235'  # пример кода изначальной валюты
amount = 1000  # количество изначальной валюты
target_currency = 'R01239'  # пример кода валюты, в которую нужно перевести

target_amount = convert_currency(initial_currency, amount, target_currency)
print(f'Количество валюты {target_currency}, которое вы получите: {target_amount}')