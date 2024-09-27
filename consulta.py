import requests

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url)
        # Verifica se a requisição foi bem-sucedida (status code 200)
        if response.status_code == 200:
            try:
                return response.json()  # Tenta converter para JSON
            except ValueError:
                print(f"Erro ao decodificar a resposta em JSON para o CEP {cep}")
                return None
        else:
            print(f"Erro na requisição para o CEP {cep}: Status Code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão para o CEP {cep}: {e}")
        return None

ceps = ['22011070', '22011080', '22011090']
for cep in ceps:
    resultado = consulta_cep(cep)
    if resultado:
        print(f"CEP: {cep} - Rua: {resultado.get('logradouro', 'Não encontrado')}")
    else:
        print(f"CEP: {cep} - Resultado não disponível")
