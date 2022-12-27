import requests

try:
    rates = requests.get("http://www.floatrates.com/daily/usd.json")
except requests.RequestException:
    print("Error")
    exit(1)

data = rates.json()
euro = data['eur']
rate = euro['rate']
dolar = eval(input("Dolar: "))
print(f"{dolar} Dollar = {dolar*rate} Euro")
