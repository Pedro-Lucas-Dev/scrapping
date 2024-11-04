import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

product = input("Qual o nome do produto? ") 
product = product.replace(" " , "-")

cit = input("Qual a Cidade? ")
cit = cit.replace(" " , "-")

if cit:
    url = f'https://lista.mercadolivre.com.br/{cit}/{product}_Frete_Full'
else:
    url = f'https://lista.mercadolivre.com.br/{product}_Frete_Full'

page = 1

while True: 

    final_url = f'{url}_Desde_{page}_NoIndex_True'

    request = requests.get(final_url, headers=headers)

    soup = BeautifulSoup(request.content, 'html.parser')

    titles = soup.find_all('h2', class_='ui-search-item__title')

    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    cents = soup.find_all('span', class_='andes-money-amount__cents')

    links = soup.find_all('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')

    if not titles:
        print("Não há mais itens")
        break
    
    for title, price, cent, link in zip(titles, prices, cents, links):
        print(f'\033[mProduto: {title.get_text()}')
        print(f'\033[32mPreço: R${price.get_text()},{cent.get_text()}')
        print(f'\033[34mLink: {link.get("href")}\n')
    
    page += 50

