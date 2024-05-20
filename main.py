import importlib
import datetime

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
    from openexchangerates import OpenExchangeRates

    c = OpenExchangeRates()

    initial_currency = input("Введите изначальную валюту: ")
    amount = float(input("Введите количество изначальной валюты: "))
    target_currency = input("Введите валюту, в которую нужно перевести: ")

    date = datetime.datetime.now()
    
    exchange_rate = c.get_rate(initial_currency, target_currency, date)
    converted_amount = c.convert(initial_currency, target_currency, amount, date)

    print(f"Курс обмена {initial_currency} к {target_currency} на {date}: {exchange_rate}")
    print(f"{amount} {initial_currency} равно {converted_amount} {target_currency}")

if __name__ == "__main__":
    main()