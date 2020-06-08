from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import time


def parse(url,path):
    req = urllib.request.urlopen(url)
    raw_html = req.read()
    html = BeautifulSoup(raw_html, 'html.parser')
    kurs = html.find_all('div', class_='currency-table__large-text')
    banki = html.find_all('div', class_='currency-table__rate__text')
    bank_pokupka = banki[1].get_text(strip=True)
    bank_prodazha = banki[2].get_text(strip=True)
    cb = kurs[0].get_text(strip=True)
    pokupka = kurs[1].get_text(strip=True)
    prodazha = kurs[2].get_text(strip=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{datetime.now().strftime("[%d.%m %H:%M]")} Доллар ЦБ:{cb} рублей   Покупка:{pokupka} в {bank_pokupka}   Продажа:{prodazha} в {bank_prodazha}\n')
    f.close()

url = 'https://www.banki.ru/products/currency/usd/'
path = 'kurs.txt'
while True:
    try:
        parse(url,path)
    except:
        print('Неудалось получить данные')
    time.sleep(7) #Ставим сколько надо
