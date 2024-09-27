import requests

def get_logradouro(cep):
    """Fetches the logradouro (street name) for a given CEP using the CEP Aberto API.

    Args:
        cep (str): The CEP (ZIP code) to query.

    Returns:
        str: The logradouro (street name) associated with the CEP, or None if the request fails.
    """

    url = f"https://www.cepaberto.com/api/v2/cep/{cep}"  # Updated URL using v2
    headers = {"Authorization": "Token your_api_token"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for error status codes

        data = response.json()
        return data.get("logradouro")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching logradouro for CEP {cep}: {e}")
        return None

# Example usage
cep = "01001000"
logradouro = get_logradouro(cep)

if logradouro:
    print(f"Logradouro: {logradouro}")
else:
    print("Failed to fetch logradouro.")