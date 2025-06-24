import requests

def obter_pais_por_ip(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("country_name") or "Desconhecido"
        else:
            return "Desconhecido"
    except requests.RequestException:
        return "Desconhecido"

