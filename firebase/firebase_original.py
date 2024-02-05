import requests
import json


link = 'https://meuprojetofabrin-default-rtdb.firebaseio.com'



def add_produto():
    produtos = {'teclado': 150, 'mouse': 100, 'monitor': 500, 'gabinete': 300, 'placa de video': 2000, 'placa mae': 800, 'processador': 1000, 'memoria ram': 400, 'hd': 300, 'ssd': 500}
    requisicao = requests.post(f'{link}/vendas/.json', data=json.dumps(produtos))
    print(requisicao)
    print(requisicao.text)

def add_clientes():
    clientes = ['robertinho', 'fabricio', 'alon', 'gabriel, lucas']
    requisicao = requests.post(f'{link}/clientes/.json', data=json.dumps(clientes))
    print(requisicao)
    print(requisicao.text)
    
def new_produto():
    new_produto = {'notebook acer intel core i7': 4000}
    requisicao = requests.patch(f'{link}/produtos/-NptYe2kcqAIyMe25hhH/.json', data=json.dumps(new_produto))
    print(requisicao)
    print(requisicao.text)
    
def delete():
    delete_clientes = requests.delete(f'{link}/clientes/-NptbZlIyStk4sWVa_vW/3.json')

