import requests

helius_api_key = "XXXXX"  # Reemplaza con tu clave de API de Helius

def get_token_holders(token_mint_address):
    url = f"https://mainnet.helius-rpc.com/?api-key={helius_api_key}&tokenAddress={token_mint_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json().get('result', [])
            holders = []
            for holder in result:
                holders.append({
                    "address": holder['owner'],
                    "amount": holder['amount']
                })
            return holders
        else:
            print(f"Failed to fetch data: {response.text}")
            return []
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

if __name__ == "__main__":
    token_mint_address = input("Ingrese la dirección del token mint: ")

    holders = get_token_holders(token_mint_address)

    if holders:
        print(f"Las siguientes wallets tienen el token {token_mint_address}:")
        for holder in holders:
            print(f"Address: {holder['address']}, Amount: {holder['amount']}")
    else:
        print(f"Ninguna wallet encontrada con el token {token_mint_address}.")
