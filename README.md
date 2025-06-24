# 🔐 AWS-SECURITY – Monitoramento de Acessos Suspeitos com Python

Este é um projeto pessoal desenvolvido com o objetivo de identificar e alertar tentativas de login suspeitas a partir de logs simulados, com foco em segurança em ambientes baseados na nuvem (como AWS). O sistema realiza a verificação da geolocalização de IPs, valida países autorizados e envia alertas automáticos por e-mail.

---
## Tecnologias Utilizadas

- Python – Linguagem principal
- Pandas – Para análise e tratamento de dados dos logs
- Requests – Para chamadas HTTP à API de geolocalização
- PyYAML – Para leitura do arquivo de configurações
- SMTP (email) – Para envio automático de alertas
- API ipapi.co – Para identificar o país de origem dos IPs

---

## 🌐 Fonte dos Dados

Os dados utilizados simulam logs de login, como os que podem ser extraídos do AWS CloudTrail. A geolocalização dos IPs é feita por meio da API pública [ipapi.co](https://ipapi.co/).

---

## ⚙️ Funcionalidades

- Leitura de logs locais (CSV ou JSON simulado)
- Consulta do país de origem do IP
- Verificação contra uma lista de países permitidos
- Geração automática de relatório de alertas
- Envio de e-mail em caso de acesso suspeito
- Estrutura pronta para integração com AWS S3 e CloudTrail

---

## 🎯 Objetivos do Projeto

- Simular um sistema de segurança com base em análise de logs
- Praticar integração com APIs externas (ipapi)
- Automatizar notificações por e-mail
- Aprimorar boas práticas com Python voltado à cibersegurança
- Construir uma solução pronta para futura integração com a AWS



