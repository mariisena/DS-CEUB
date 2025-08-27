# Evidências – API OOP (Python)

## 1. Execução do servidor

- Terminal com `uvicorn app.main:app --reload` e log "Uvicorn running on <http://127.0.0.1:8000>".

![terminal](<evidencias_img/01_terminal_uvicorn.png>)

- Print do Swagger UI (`/docs`).

![swagger](<evidencias_img/11_swagger.png>)

- Print do ReDoc (`/redoc`)

![ReDoc](<evidencias_img/12_redoc.png>)

## 2. Consumo via VS Code – REST Client

- **Healthcheck**: resposta JSON de `/`.

![healthcheck](evidencias_img/02_http_Healthcheck.png)

- **Criar Wizard** (201).
  
![post_wizard](evidencias_img/04_http_criar%20wizard.png)

- **Criar Ninja** (201).

![post_ninja](evidencias_img/05_http_criar%20ninja.png)

- **Listar** `/characters`

![list_characters](<evidencias_img/06_http_listar novamente.png>)

- **Obter por ID** `/characters/{id}`: resposta do item 1.

![get_by_id](<evidencias_img/07_http_obter por id.png>)

- **Polimorfismo** `/characters/1/speak` e `/characters/2/speak`.

![speak_wizard](<evidencias_img/08_http_polimorfismo falar wizard.png>)
![speak_ninja](<evidencias_img/09_http_polimorfismo falar ninja.png>)

- **Remover** `/characters/2`.

![delete](<evidencias_img/10_http_remover.png>)

## 3. Observações técnicas

- Como a fábrica no `POST /characters` decide qual classe instanciar com base em `type`.
- Encapsulamento com propriedades (`name`).
