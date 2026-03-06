import requests

url = 'https://elcomercio.pe/robots.txt'
response = requests.get(url)

if response.status_code == 200:
  print("robots.txt encontrado")
else:
  print("robots.txt no encontrado")

# testing
