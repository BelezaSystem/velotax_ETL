from bs4 import BeautifulSoup
import pandas as pd

arquivo = r'C:\Users\Pc\Desktop\PROJECT CEP\Velotax _ Impostos Descomplicados.html'

# Supondo que o arquivo HTML esteja em 'arquivo.html'
with open(arquivo, 'r') as file:
    content = file.read()

# Criar um objeto BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

list_itens = soup.find_all(class_='ant-list-item ant-list-item-no-flex')

velotax = {}

# Extrair as informações de cada tag encontrada
for itens in list_itens:
    matriz = itens.find(class_='ant-collapse-header').get_text()
    tags_list_info = itens.find_all(class_='list-info')
    if 'Ativo' in tags_list_info:
        velotax[matriz] = {}
        for tag in tags_list_info:
            label = tag.find(class_='list-info-label').get_text()
            value = tag.find(class_='list-info-value').get_text()
            # Verificar se o texto é 'Ativo'


            velotax[matriz][label] = value

# df = pd.DataFrame.from_dict(velotax, orient='index')
# df.to_excel('velotax.xlsx', index=True)

print(velotax)
