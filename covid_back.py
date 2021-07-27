import requests
import json

# Visualizar se a pagina esta funcionando
response_covid_default = requests.get("https://api.covid19api.com/")
print(response_covid_default)

