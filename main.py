# import requests

# def fetch_data(endpoint, filters={}):
#     url = f"https://rickandmortyapi.com/api/{endpoint}"
#     response = requests.get(url, params=filters)
    
#     return response.json() if response.status_code == 200 else None
    
#     characters = fetch_data("character", {'name': 'Rick'})
    
# if characters:
#     print(characters)
# else:
#     print('Failed to fetch data')

elementos = [3, 5, 7, 9]
for i in range(len(elementos)):
    print(f"O quadrado de {elementos[i]} é {elementos[i]**2}")
