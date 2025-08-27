# OOP API – Personagens (FastAPI)

API de exemplo para a disciplina **Desenvolvimento de Sistemas** demonstrando **POO (classes, herança, polimorfismo)** em Python com FastAPI.

---

## Tecnologias

- Python, FastAPI, Uvicorn, Pydantic

---

## Estrutura

```bash
05_API_POO_PYTHON/
├─ docs_pdf/
├─ evidencias_img/
├─ oop-api-python/
│   └─ app/
│      ├─ init.py
│      ├─ main.py
│      ├─ models.py
│      ├─ repository.py
│      └─ schemas.py
│   └─ requirements.txt
│   └─ client.http
├─ EVIDENCIAS.md
└─ ReadMe.md
```

---

## Conceitos de POO aplicados

- **Classe base abstrata**: `Character` define a interface comum.
- **Herança**: `Wizard` e `Ninja` especializam `Character`.
- **Polimorfismo**: método `speak()` implementado de formas diferentes.
- **Encapsulamento**: propriedades com validação (ex.: `name`).

---

## Como rodar

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
# Docs: http://127.0.0.1:8000/docs  |  ReDoc: http://127.0.0.1:8000/redoc
```

Se der bloqueio na ativação:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS (bash/zsh)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
# Docs: http://127.0.0.1:8000/docs  |  ReDoc: http://127.0.0.1:8000/redoc
```

## Rotas

- `GET /` → healthcheck
- `GET /characters` → lista todos
- `POST /characters` → cria (exige type)
  - **wizard**: {"type":"wizard","name":"Gandalf","universe":"Middle-earth","spell":"You shall not pass"}
  - **ninja**: {"type":"ninja","name":"Kakashi","universe":"Naruto","technique":"Chidori"}
- ``GET /characters/{id}`` → obtém por id
- ``GET /characters/{id}/speak`` → polimorfismo (fala depende da subclasse)
- ``GET /characters/type/{kind}`` → filtra por tipo (wizard | ninja)
- ``DELETE /characters/{id}`` → remove

> Dica: use o arquivo `client.http` no VS Code (REST Client) e clique em **Send Request** em cada bloco.
