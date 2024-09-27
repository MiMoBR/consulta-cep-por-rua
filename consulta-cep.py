import requests

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    return response.json()

#ceps = ['01001000', '02020030', '03030040']

for cep in ceps:
    resultado = consulta_cep(cep)
    print(f"CEP: {cep} - Rua: {resultado['logradouro']}")
