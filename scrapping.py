import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import csv

# Configuração do cabeçalho para simular um navegador
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6562.74 Safari/537.36'
}

def main(produto, cidade):
    if not produto:
        messagebox.showerror("Erro", "Por favor, insira o nome do produto.")
        return
    
    product = produto.replace(" ", "-")
    cit = cidade.replace(" ", "-") if cidade else ""
    
    if cit:
        url = f'https://lista.mercadolivre.com.br/{cit}/{product}_Frete_Full'
    else:
        url = f'https://lista.mercadolivre.com.br/{product}_Frete_Full'

   
    filename = 'consulta_produto.csv'
   
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Descrição', 'Preço', 'Link', 'Avaliações'])   
        
        page = 1
        
        while True:
            final_url = f'{url}_Desde_{page}_NoIndex_True'
            response = requests.get(final_url, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', class_='poly-card__content')

            if response.status_code != 200:
                messagebox.showinfo("Páginas Acabaram", "As paginas acabaram! não há mais resultados")
                break
           
            for item in items:
                description = item.find('h2', class_='poly-box poly-component__title')
                price = item.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
                link = item.find('a')['href'] if item.find('a') else None
                reviews = item.find('span', class_='poly-reviews__rating')
                
                description_text = description.text if description else "Descrição não encontrada"
                price_text = price.text if price else "Preço não encontrado"
                link_text = link if link else "Link não encontrado"
                reviews_text = reviews.text if reviews else "Avaliações não encontradas"
                
                writer.writerow([description_text, price_text, link_text, reviews_text])
           
            page += 50

def create_scrapping():
    
    root = tk.Tk()
    root.title(" ")
    root.geometry("400x300")
    root.resizable(False, False)
    
    titulo = tk.Label(root, text="Consulta de Produtos no Mercado Livre", font=("Arial", 14, "bold"))
    titulo.pack(pady=10)
    
    produto_label = tk.Label(root, text="Nome do Produto:", font=("Arial", 10))
    produto_label.pack(pady=(10, 0))
    produto_entry = tk.Entry(root, width=40)
    produto_entry.pack(pady=(0, 10))
    
    cidade_label = tk.Label(root, text="Cidade (Opcional):", font=("Arial", 10))
    cidade_label.pack(pady=(10, 0))
    cidade_entry = tk.Entry(root, width=40)
    cidade_entry.pack(pady=(0, 10))
   
    iniciar_button = tk.Button(root, text="Iniciar Consulta", font=("Arial", 12), bg="green", fg="black",
                               command=lambda: main(produto_entry.get(), cidade_entry.get()))
    iniciar_button.pack(pady=20)
    
    root.mainloop()
if __name__ == "__main__":
    create_scrapping()
