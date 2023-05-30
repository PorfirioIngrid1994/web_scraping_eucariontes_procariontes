import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.todamateria.com.br/procariontes-e-eucariontes/")

if page.status_code == 200: #É um padrão
    ...
else: 
    print("HTTP error", page.status_code)

soup = BeautifulSoup(page.content, "html.parser")

procariontes = {}
eucariontes = {}

tabela = soup.find("table")  # Encontrar a tabela
linhas = tabela.find_all("tr")  # Encontrar as linhas da tabela

for linha in linhas[1:]:  # Segunda linha porque a primeira é cabeçalho
    celulas = linha.find_all("td")  # Encontrar todas as células da linha
    if len(celulas) == 2:  # Verifica se tem duas células
        procarionte = celulas[0].text.strip()  # Extrair o texto da célula procarionte e remover espaços em branco
        eucarionte = celulas[1].text.strip()  # Extrair o texto da célula eucarionte e remover espaços em branco
        procariontes[procarionte] = eucarionte  # Adicionar ao dicionário de células procariontes
        eucariontes[eucarionte] = procarionte  # Adicionar ao dicionário de células eucariontes
print(procariontes)
print(eucariontes)
