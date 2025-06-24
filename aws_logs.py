import json

def extrair_eventos_suspeitos(caminho_arquivo):
    eventos = []
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
        for evento in dados.get("Records", []):
            ip = evento.get("sourceIPAddress")
            usuario = evento.get("userIdentity", {}).get("userName", "desconhecido")
            datahora = evento.get("eventTime")
            acao = evento.get("eventName")
            sucesso = evento.get("errorCode") is None

            eventos.append({"timestamp": datahora,
                "ip": ip,
                "usuario": usuario,
                "acao": acao,
                "sucesso": sucesso})
    return eventos
