import requests
from bs4 import BeautifulSoup

Codigos = ['XX123456789XX', 'XX123456789XX' ]#Modifique aqui
for Codigo in Codigos:
    try:
        #Requisição
        req= requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?', data={'objetos' : Codigo})
        #Tratamento da requisição e organização
        soup = BeautifulSoup (req.text, 'html.parser')
        #Encontra o ultimo evento de objeto
        Texto = soup.find(id="UltimoEvento").strong.text
        #Encontra a data
        Data = soup.find(id="UltimoEvento").text.split()[-1]
        print(f'Status: {Texto} - Data - {Data} Codigo do produto: {Codigo}')
    except Exception as e:
        print(e)