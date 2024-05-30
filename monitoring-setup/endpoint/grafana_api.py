import requests
import json

# Configurações do Grafana
GRAFANA_URL = "http://192.168.0.200:3000"
GRAFANA_USER = "admin"
GRAFANA_PASSWORD = "grafana"

# URLs da API
LOGIN_URL = f"{GRAFANA_URL}/login"
DATASOURCES_URL = f"{GRAFANA_URL}/api/datasources"

# Função para fazer login no Grafana e obter cookies de autenticação
def grafana_login():
    session = requests.Session()
    login_payload = {
        "user": GRAFANA_USER,
        "password": GRAFANA_PASSWORD
    }
    response = session.post(LOGIN_URL, json=login_payload)
    if response.status_code == 200 and response.json().get('message') == 'Logged in':
        print("Login bem-sucedido.")
        return session
    else:
        print(f"Erro ao fazer login no Grafana: {response.status_code} - {response.json()}")
        return None

# Função para obter datasources do Grafana
def get_datasources(session):
    response = session.get(DATASOURCES_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter datasources: {response.status_code} - {response.text}")
        return None
    
session = grafana_login()
if session:
    datasources = get_datasources(session)
    if datasources:
        print(json.dumps(datasources, indent=2))
    else:
        print("Falha ao obter datasources.")
else:
    print("Falha ao fazer login no Grafana.")