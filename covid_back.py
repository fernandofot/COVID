import requests
import json

# Visualizar se a pagina esta funcionando
response_covid_default = requests.get("https://api.covid19api.com/")
print("Imprimindo o resultado")
print(response_covid_default)
print("==============================")

response_covid_summary = requests.get("https://api.covid19api.com/summary")
print("Imprimindo o resultado")
print(response_covid_summary.json())
print("==============================")

response_covid_countries = requests.get("https://api.covid19api.com/countries")

def covid_print(obj):
    text1 = json.dumps(obj, sort_keys=True, indent=4)
    print(text1)

covid_print((response_covid_summary.json()))


def covid_countries(obj):
    text2 = json.dumps(obj, sort_keys=True, indent=4)
    print(text2)

covid_countries(response_covid_countries.json())
