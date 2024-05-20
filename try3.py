# # import datetime
# # from openexchangerates import OpenExchangeRates

# # def main():
# #     c = OpenExchangeRates()

# #     initial_currency = input("Введите изначальную валюту: ")
# #     amount = float(input("Введите количество изначальной валюты: "))
# #     target_currency = input("Введите валюту, в которую нужно перевести: ")

# #     date = datetime.datetime.now()
    
# #     exchange_rate = c.get_rate(initial_currency, target_currency, date)
# #     converted_amount = c.convert(initial_currency, target_currency, amount, date)

# #     print(f"Курс обмена {initial_currency} к {target_currency} на {date}: {exchange_rate}")
# #     print(f"{amount} {initial_currency} равно {converted_amount} {target_currency}")

# # if __name__ == "__main__":
# #     main()

# import datetime
# from openexchangerates import OpenExchangeRates
# import requests

# def main():
#     c = OpenExchangeRates()

#     initial_currency = input("Введите изначальную валюту: ")
#     amount = float(input("Введите количество изначальной валюты: "))
#     target_currency = input("Введите валюту, в которую нужно перевести: ")

#     date = datetime.datetime.now()

#     try:
#         exchange_rate = c.get_rate(initial_currency, target_currency, date)
#         converted_amount = c.convert(initial_currency, target_currency, amount, date)

#         print(f"Курс обмена {initial_currency} к {target_currency} на {date}: {exchange_rate}")
#         print(f"{amount} {initial_currency} равно {converted_amount} {target_currency}")

#     except requests.exceptions.RequestException as e:
#         print("Произошла ошибка при запросе курса обмена:", e)

# if __name__ == "__main__":
#     main()

import datetime
from openexchangerates import OpenExchangeRates
import requests

def main():
    c = OpenExchangeRates()

    initial_currency = input("Введите изначальную валюту: ")
    amount = float(input("Введите количество изначальной валюты: "))
    target_currency = input("Введите валюту, в которую нужно перевести: ")

    date = datetime.datetime.now()

    try:
        exchange_rate = c.get_rate(initial_currency, target_currency, date)
        converted_amount = c.convert(initial_currency, target_currency, amount, date)

        print(f"Курс обмена {initial_currency} к {target_currency} на {date}: {exchange_rate}")
        print(f"{amount} {initial_currency} равно {converted_amount} {target_currency}")

    except requests.exceptions.RequestException as e:
        print("Произошла ошибка при запросе курса обмена:", e)

if __name__ == "__main__":
    main()