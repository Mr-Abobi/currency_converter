import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

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
            return 'Ошибка: Некорректный код целевой валюты'
    else:
        return 'Ошибка: Не удалось получить данные от сервера'

def perform_conversion():
    base_currency = base_currency_entry.get().upper()
    amount = float(amount_entry.get())
    target_currency = target_currency_entry.get().upper()

    result = convert_currency(base_currency, amount, target_currency, api_key)

    if isinstance(result, float):
        messagebox.showinfo('Результат конвертации', f'{amount} {base_currency} равно {result} {target_currency}')
    else:
        messagebox.showerror('Ошибка', result)

api_key = 'b9e54f631f2448259723d96659ed9c02'

# Создание графического интерфейса
root = tk.Tk()
root.title('Конвертер валют')

base_currency_label = tk.Label(root, text='Изначальная валюта:')
base_currency_label.pack()
base_currency_entry = tk.Entry(root)
base_currency_entry.pack()

amount_label = tk.Label(root, text='Количество валюты для конвертации:')
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

target_currency_label = tk.Label(root, text='Целевая валюта:')
target_currency_label.pack()
target_currency_entry = tk.Entry(root)
target_currency_entry.pack()

convert_button = tk.Button(root, text='Конвертировать', command=perform_conversion)
convert_button.pack()

root.mainloop()