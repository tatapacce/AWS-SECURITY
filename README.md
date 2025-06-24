# 🔐 AWS-SECURITY – Monitoramento de Acessos Suspeitos com Python

Este projeto simula um sistema de monitoramento e alerta de segurança, capaz de identificar **tentativas de acesso suspeitas** com base em logs de login, geolocalização de IPs e envio de notificações por e-mail.

💡 **Pronto para integrar com AWS CloudTrail  .

---

## 📌 Funcionalidades

-  Identificação de tentativas de login vindas de IPs suspeitos
-  Localização do IP via API pública (ipapi.co)
-  Validação contra uma lista de países permitidos
-  Envio automático de alertas por e-mail
-  Geração de relatórios em arquivo `.txt`
-  Estrutura pronta para ler logs da AWS (simulados via JSON)

---

## 🛠️ Tecnologias utilizadas

- Python 3
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/)
- [YAML](https://pyyaml.org/)
- API pública [ipapi.co](https://ipapi.co/)


