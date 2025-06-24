import pandas as pd
import yaml
import os
from utils.email_sender import enviar_email_alerta
from utils.geoip import obter_pais_por_ip

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

paises_permitidos = config['paises_permitidos']


log_path = 'logs/log_suspeitos.csv'
if not os.path.exists(log_path):
    print("Nenhum log suspeito encontrado.")
    exit()

df = pd.read_csv(log_path)

if 'pais' not in df.columns or df['pais'].isnull().any():
    df['pais'] = df['ip_origem'].apply(obter_pais_por_ip)

os.makedirs("alerts", exist_ok=True)

alertas = []

for index, row in df.iterrows():
    if row['pais'] not in paises_permitidos:
        alertas.append({"ip": row['ip_origem'],
            "usuario": row['usuario_suspeito'],
            "pais": row['pais'],
            "tentativas": row['tentativas_usuario'],
            "mensagem": "Acesso de país não permitido"})

if alertas:
    alerta_txt_path = "alerts/alerta_ips.txt"
    with open(alerta_txt_path, "w") as f:
        for alerta in alertas:
            f.write(f"[!] {alerta['mensagem']} - IP: {alerta['ip']} - "
                f"Usuário: {alerta['usuario']} - País: {alerta['pais']} - "
                f"Tentativas: {alerta['tentativas']}\n")

    print(f"Alertas gerados em {alerta_txt_path}")

    
    corpo_email = "⚠️ Foram detectadas tentativas suspeitas de login:\n\n"
    for alerta in alertas:
        corpo_email += (f"- IP: {alerta['ip']} | Usuário: {alerta['usuario']} | "
            f"País: {alerta['pais']} | Tentativas: {alerta['tentativas']}\n")


    enviar_email_alerta(assunto="[ALERTA DE SEGURANÇA] Tentativas suspeitas detectadas",
        corpo=corpo_email,
        config_email=config['email_alertas'])

else:
    print("Nenhum alerta gerado.")
