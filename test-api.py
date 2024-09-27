import time
import requests
from requests.exceptions import ConnectionError

url = 'https://viacep.com.br/ws/22261140/json/'

for i in range(5):  # Retry up to 5 times
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
            break
    except ConnectionError:
        print(f"Connection failed. Retrying {i+1}/5...")
        time.sleep(2 ** i)  # Exponential backoff
else:
    print("Max retries reached. Please check the server status or network.")
