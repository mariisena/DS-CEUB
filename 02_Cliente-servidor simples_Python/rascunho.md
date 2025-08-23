# Missão 2 — Evidências e Testes Manuais da API

## 2) Testes via Swagger UI (navegador)

1. Abra **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.
2. Expanda o grupo **personagens**.
3. Clique em **Try it out** em cada operação.
4. Valide **códigos de status** (200/201/204/404) e o **schema** retornado.
5. No `GET /personagens/`, confira o header `X-Total-Count` (total antes da paginação).

---


## 5) Postman — Coleção pronta (importar)

1. Abra o Postman → **Import** → **Raw text** e cole o JSON abaixo (ou salve como `Personagens.postman_collection.json`).
2. Após importar, defina a variável de ambiente `baseUrl` (por exemplo `http://127.0.0.1:5000`).

```json

```

---

## 6) Insomnia — Export (importar)

1. Insomnia → **Create** → **Import From** → **Clipboard** e cole o JSON.
2. Ajuste a variável `baseUrl` se necessário.

```json

```

---

## 7) Template de Relatório de Evidências (`EVIDENCIAS.md`)

Copie este modelo para um arquivo `EVIDENCIAS.md` e preencha com capturas de tela e saídas de comandos.

```markdown


---


---

## 10) Próximos Passos (opcionais)

* Adicionar **campos opcionais** (ex.: `rank`, `time_criacao`).
* Adicionar **paginação via Link headers**.
* Criar **pipeline de testes** com `pytest` e `requests` para smoke tests.
* Publicar o `README.md` e evidências no repositório.

# API de Personagens — Flask + Swagger

Pequena API REST para demonstrar **arquitetura cliente–servidor** e o uso de **HTTP**. Implementada em **Python + Flask-RESTx**, com **Swagger UI** automático para testes.

> Para evidências detalhadas (cURL, Postman, Insomnia, requests.http e checklist), veja **EVIDENCIAS.md** neste projeto.

---

## 1) Visão Geral

- **Stack:** Python 3.10+, Flask, Flask-RESTx  
- **Objetivo:** CRUD de personagens (dados fictícios), expondo endpoints REST  
- **Docs interativas (Swagger):** disponíveis na raiz do servidor

---

## 2) Como rodar a API

```bash
# (opcional) criar venv
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# instalar dependências
pip install -r requirements.txt
# ou, se preferir:
# pip install flask flask-restx

# executar
python api.py
