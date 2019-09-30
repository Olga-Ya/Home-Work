# Получить курс нескольких валют
#  за текущую дату
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    currency = soup.find('body').text
    return currency

def  main():
    url ="https://www.nbrb.by/API/ExRates/Rates?periodicity=0"
    print(get_data(get_html(url)))

if  __name__=='__main__':
    main()