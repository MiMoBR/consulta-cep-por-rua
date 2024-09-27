import requests

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    print(url)
    #response = requests.get(url)
    #return response.json()

ceps = ['022050020', '022010000', '022010010']

for cep in ceps:
    resultado = consulta_cep(cep)
    print(f"CEP: {cep} - Rua: {resultado['logradouro']}")