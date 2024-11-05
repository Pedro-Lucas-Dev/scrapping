import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

# Configuração do cabeçalho para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6562.74 Safari/537.36'
}

def get_information(link):

    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', class_='ui-pdp-title').get_text() if soup.find('h1', class_='ui-pdp-title') else "Título não encontrado"
    sold = soup.find('span', class_='ui-pdp-subtitle').get_text() if soup.find('span', class_='ui-pdp-subtitle') else "Vendidos não encontrado"

    return title, sold

def process_links(filename, filename_output, progress_bar, total_links):

    with open(filename, 'r', newline='', encoding='utf-8') as file_in, \
         open(filename_output, 'w', newline='', encoding='utf-8') as file_out:
        
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)
        
        writer.writerow(['Link', 'Título', 'Vendidos'])

        for i, row in enumerate(reader, 1):
            link = row[0]
            title, sold = get_information(link)
            writer.writerow([link, title, sold])

            progress_bar['value'] = (i / total_links) * 100
            root.update_idletasks() 


        messagebox.showinfo("Processo Concluído", f"As informações foram salvas em {filename_output}")

def iniciar_processo():
    filename = 'links_produto.csv'         
    filename_output = 'informacoes_adicionais.csv'  

    with open(filename, 'r', encoding='utf-8') as f:
        total_links = sum(1 for _ in f) - 1 

    process_links(filename, filename_output, progress_bar, total_links)


root = tk.Tk()
root.title("Processador de Links")
root.geometry("300x250")
root.resizable(False, False)

titulo = tk.Label(root, text="Processador de Links CSV", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=250, mode='determinate')
progress_bar.pack(pady=20)

iniciar_button = tk.Button(root, text="Iniciar Extração", font=("Arial", 12), bg="green", fg="black", command=iniciar_processo)
iniciar_button.pack(pady=10)

root.mainloop()
