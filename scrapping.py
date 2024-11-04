import requests
from bs4 import BeautifulSoup

headers = {
<<<<<<< HEAD
    "User-Agent": # "your user agent"

    
=======
    "User-Agent": # "YOUR USER AGENT"
>>>>>>> 3330a62f822e91af732ca0a0b1036a6e6413ea42
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
    
    for title, price, cent, link in zip(titles, prices, cents, links):
        print(f'\033[mProduto: {title.get_text()}')
        print(f'\033[32mPreço: R${price.get_text()},{cent.get_text()}')
        print(f'\033[34mLink: {link.get("href")}\n')

    if not request:
        print("Não há mais itens")
        break
    
    page += 50



    # response = requests.get(url)
    # if response.status_code != 200:
    #     print(f"Erro ao acessar a URL: {response.status_code}")
    #     return

    # soup = BeautifulSoup(response.text, 'html.parser')
    # ol_container = soup.find('ol', class_='ui-search-layout ui-search-layout--stack shops__layout')
    # items = ol_container.find_all('li', class_='ui-search-layout__item')
    
    # results = []
    # for item in items:

    #     price_container = item.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
    #     price = None
    #     if price_container:
    #         real = price_container.find('span', class_='andes-money-amount__fraction')
    #         cents = price_container.find('span', class_='andes-money-amount__cents')
    #         if real:
    #             price = f"R${real.text},{cents.text.zfill(2) if cents else '00'}"


    #     title = item.find('h2', class_='poly-box poly-component__title')
    #     title_text = title.text if title else None

    #     link = item.find('a', href=True)
    #     link_url = link['href'] if link else None

    #     rating = item.find('span', class_='poly-reviews__rating', attrs={'aria-hidden': 'true'})
    #     rating_value = rating.text if rating else 'não avaliado'

    #     results.append({
    #         'price': price,
    #         'title': title_text,
    #         'link': link_url,
    #         'rating_value': rating_value
    #     })

    
    # for result in results:
            
