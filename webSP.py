# necessário instalar o "requests" e o "beautifulsoap4"
import requests
from bs4 import BeautifulSoup

url = input('Onde pesquisar:')
resposta = requests.get(url)
# print(resposta.text)  # para ver o HTML puro do site
html = BeautifulSoup(resposta.text, 'html.parser')

# o nome das classes para o select podem variar de acordo com o site
for pergunta in html.select('.s-post-summary--content'):  # retornando a classe ...summary--content do css do site
    titulo = pergunta.select_one('.s-link')  # como saber que é só 1 titulo usamos o "_one"
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    # agora que separamos o titulo, vamos pegar o seu texto somento
    print(data.text, "/", titulo.text, "/ votos:", votos)

