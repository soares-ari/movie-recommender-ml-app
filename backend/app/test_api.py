import requests

url = "http://127.0.0.1:8000/recommendations/25"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ API funcionando!")
    print("Recomendações para o usuário 25:")
    for rec in data["recommendations"]:
        print("-", rec["title"])
else:
    print("❌ Erro na API:", response.status_code)