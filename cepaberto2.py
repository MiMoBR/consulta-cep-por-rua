#https://www.cepaberto.com/api_key

import requests
import time

resultados = {}
def get_logradouro(lista_ceps):

    url = "https://www.cepaberto.com/api/v3/cep?cep="
    headers = {"Authorization": "Token 3ab7dfd9663f43301359429f66a82fc0"}

    for cep in lista_ceps:
        try:
            response = requests.get(url + cep, headers=headers)
            response.raise_for_status()
            resultados = response.json()

            if 'logradouro' in resultados:
                print(f"CEP: {cep} Logradouro: {resultados['logradouro']}")
            else:
                print(f"Erro: Logradouro não encontrado para o CEP: {cep}")
            time.sleep(10)
        except requests.exceptions.RequestException as e:
            resultados = {"erro": str(e)}

    return resultados

lista_ceps = ['22795446','22795450','22795453','22795455','22795460','22795465','22795470','22795475','22795480','22795485','22795490','22795491','22795492','22795493','22795500','22795505','22795510','22795520','22795560','22795565','22795570','22795571','22795572','22795583','22795584','22795585','22795586','22795587','22795588','22795589','22795590','22795595','22795641','22795650','22795690','22795700','22795711','22795712','22795720','22795740','22795750','22795760','22795770','22795780','22795790','22795800','22795810','22795820','22795830','22795850','22795860','22795865','22795870','22795900','22795901','22985901']
logradouro = get_logradouro(lista_ceps)