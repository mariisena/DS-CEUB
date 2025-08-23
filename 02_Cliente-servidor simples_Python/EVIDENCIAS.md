# Evidências de Funcionamento da API

> Este documento apresenta as evidências de funcionamento da API de Personagens, demonstrando como consumir os endpoints utilizando diferentes ferramentas e métodos, conforme solicitado na descrição da atividade.

---

## 1) Executando api.py

![ExecutandoAPI](<evidencias_imagens/ExecutandoAPI.png>)

---

## 2) Executando cliente.py

![Resultado_cliente.py](<evidencias_imagens/Resultado cliente.py I.png>)
![Resultado_cliente.py](<evidencias_imagens/Resultado cliente.py II.png>)
![Resultado_cliente.py](<evidencias_imagens/Resultado cliente.py III.png>)
![Resultado_cliente.py](<evidencias_imagens/Resultado cliente.py IV.png>)
![Resultado_cliente.py](<evidencias_imagens/Resultado cliente.py V.png>)

---

## 3) Executando cliente_interativo.py

![Resultado cliente_interativo.py](<evidencias_imagens/Resultado I cliente_interativo.py.png>)
![Resultado cliente_interativo.py](<evidencias_imagens/Resultado II cliente_interativo.py.png>)

---

## 4) Consumo via Swagger UI

> A documentação interativa gerada pelo Flask-RESTX com o Swagger UI é a forma mais simples e visual de testar a API. Com o servidor em execução, basta acessar <http://127.0.0.1:5000>.

### Tela inicial Swagger UI

![Tela inicial da UI](<evidencias_imagens/01-Swagger. Tela inicial da UI.png>)

### Listando todos os personagens (GET /personagens/)

![GET /personagens/](<evidencias_imagens/02-Swagger. GET _personagens_ (expandindo).png>)

Try it out
![GET /personagens/ (Try it out)](<evidencias_imagens/03-Swagger GET _personagens_ (Try it out).png>)

### Criando um novo personagem (POST /personagens/)

![POST /personagens/](<evidencias_imagens/04-Swagger POST _personagens_ (expandido).png>)

Try it out
![POST /personagens/ (Try it out)](<evidencias_imagens/05-Swagger POST _personagens_ (Try it out).png>)

### Buscando um personagem pelo ID (GET /personagens/{id})

![GET /personagens/{id}](<evidencias_imagens/08-Swagger GET _personagens_{id} (expandido).png>)

Try it out
![GET /personagens/{id} (Try it out)](<evidencias_imagens/09-Swagger GET _personagens_{id} (Try it out).png>)

### Removendo um personagem pelo ID (DELETE /personagens/{id})

![DELETE /personagens/{id}](<evidencias_imagens/06-Swagger DELETE _personagens_{id} (expandido).png>)

Try it out
![DELETE /personagens/{id} (Try it out)](<evidencias_imagens/07-Swagger DELETE _personagens_{id} (Try it out).png>)

### Atualizando COMPLETAMENTE um personagem (PUT /personagens/{id})

![PUT /personagens/{id}](<evidencias_imagens/10-Swagger PUT _personagens_{id} (expandido).png>)

Try it out
![PUT /personagens/{id} (Try it out)](<evidencias_imagens/11-Swagger PUT _personagens_{id} (Try it out).png>)

### Models

![Models API](<evidencias_imagens/12.Swagger MODELS.png>)

---

## 5) Teste Rápido (cURL) - terminal

> Usando `-i` para ver headers e status code.

### 5.1 Listar todos os personagens (GET /personagens/)

```bash
curl -i http://127.0.0.1:5000/personagens/
```

![Listar todos personagens](<evidencias_imagens/curl_Listar todos personagens I.png>)
![Listar todos personagens](<evidencias_imagens/curl_Listar todos personagens II.png>)

### 5.2 Listar personagens com filtro e paginação

```bash
# Filtrar por universo "Naruto" com limite de 2 resultados
curl -i "http://127.0.0.1:5000/personagens/?universo=Naruto&limit=2&offset=0"
```

![Filtro + paginação](<evidencias_imagens/curl_Filtro+Paginação.png>)

### 5.3 Obter um personagem específico por ID (GET /personagens/{id})

```bash
curl -i http://127.0.0.1:5000/personagens/6
```

![Buscar por ID](<evidencias_imagens/curl_Buscar por id.png>)

### 5.4 Criar um novo personagem (POST /personagens/)

```bash
curl -X POST http://127.0.0.1:5000/personagens/ -H "Content-Type: application/json" -d "{\"nome\": \"Edward Elric\", \"universo\": \"Fullmetal Alchemist\", \"poder_principal\": \"Alquimia\"}"
```

![Criar personagem](<evidencias_imagens/curl_Criar personagem.png>)

### 5.5 Atualizar um personagem (PUT /personagens/{id})

```bash
curl -X PUT http://127.0.0.1:5000/personagens/11 -H "Content-Type: application/json" -d "{\"nome\": \"Edward Elric\", \"universo\": \"Fullmetal Alchemist\", \"poder_principal\": \"Alquimia Avançada\"}"
```

![Atualizar personagem](<evidencias_imagens/curl_Atualizar um personagem.png>)

### 5.6 Remover um personagem (DELETE /personagens/{id})

```bash
curl -i -X DELETE http://127.0.0.1:5000/personagens/6
```

![Remover personagem](<evidencias_imagens/curl_Remover personagem.png>)

---

## 6) Consumo via VS Code (REST Client)

![rest client I](<evidencias_imagens/X-Total-Count._vscode-01-get-200.png>)
![rest client II](<evidencias_imagens/id_vscode-01-get-200.png>)

---

## 7) Postman

Checklist de prints:

![postman 01](<evidencias_imagens/postman-01-coleção.png>)
![postman 02](<evidencias_imagens/postman-02-coleção.png>)
![postman 03](<evidencias_imagens/postman-03-listar.png>)
![postman 04](<evidencias_imagens/postman-04-Filtrar e paginar.png>)
![postman 05](<evidencias_imagens/postman-05-busca.png>)
![postman 06](<evidencias_imagens/postman-06-busca-404.png>)
![postman 07](<evidencias_imagens/postman-07-criar.png>)
![postman 08](<evidencias_imagens/postman-08-atualizar.png>)

## 7) Casos de Teste — Tabela Rápida

|   ID | Ação        | Requisição                               | Esperado                                 |
| ---: | ----------- | ---------------------------------------- | ---------------------------------------- |
| CT01 | Listar      | `GET /personagens/`                      | 200 + array de objetos + `X-Total-Count` |
| CT02 | Filtrar     | `GET /personagens/?universo=Naruto`      | 200 + somente itens de "Naruto"          |
| CT03 | Obter (OK)  | `GET /personagens/2`                     | 200 + objeto id=2                        |
| CT04 | Obter (404) | `GET /personagens/999`                   | 404 + `{ detail: ... }`                  |
| CT05 | Criar (OK)  | `POST /personagens/` body válido         | 201 + objeto com `id`                    |
| CT06 | Criar (400) | `POST /personagens/` body faltando campo | 400 + `{ detail: ... }`                  |
| CT07 | Atualizar   | `PUT /personagens/{id}` body válido      | 200 + objeto atualizado                  |
| CT08 | Remover     | `DELETE /personagens/{id}`               | 204 sem corpo                            |

---
