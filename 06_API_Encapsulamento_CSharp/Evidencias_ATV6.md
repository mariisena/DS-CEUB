# Evidências — Atividade 6 (Encapsulamento)

## Ambiente

- SO: Windows 11
- .NET SDK: 9.0
- Editor: VS Code

## Execução

- ``dotnet run`` → URL: <http://localhost:5134>

![execução](<evidencias_imagens/01_execucao.png>)

## Swagger

- swagger/index

![index](<evidencias_imagens/02_swagger_telainicial.png>)

- GET /contas

![GET /contas](<evidencias_imagens/03_swagger_get_contas.png>)

- POST /contas — 201 — [PRINT]

![POST /contas](<evidencias_imagens/04_swagger_post_contas.png>)

- GET /contas/{id} — 200

![GET /contas/{id}](<evidencias_imagens/05_swagger_get_contas_id.png>)

- GET /contas/{id} — 404

![GET /contas/{id}](<evidencias_imagens/10_swagger_get_contas_id.png>)

- POST /contas/{id}/depositar — 200

![POST /contas/{id}/depositar](<evidencias_imagens/06_swagger_post_contas_id_depositar.png>)
![POST /contas/{id}/depositar](<evidencias_imagens/07_swagger_post_contas_id_depositar.png>)

- POST /contas/{id}/sacar — 200 — [PRINT]

![POST /contas/{id}/sacar](<evidencias_imagens/08_swagger_post_contas_id_sacar.png>)
![POST /contas/{id}/sacar](<evidencias_imagens/09_swagger_post_contas_id_sacar.png>)

- POST /contas/{id}/sacar — 400 — **Operação inválida: Saldo insuficiente.**

![400](evidencias_imagens/11_swagger_post_contas_id_sacar.png)

## VS Code REST Client

- Arquivo `APIEncap.http`
- Execução dos requests (criar, listar, buscar, depositar, sacar, erro)
![criar](<evidencias_imagens/12_http_criar conta.png>)
![listar](<evidencias_imagens/13_http_listar conta.png>)
![buscar](<evidencias_imagens/14_http_buscar por id.png>)
![depositar](<evidencias_imagens/15_http_depositar.png>)
![sacar](<evidencias_imagens/16_http_sacar_ok.png>)
![saque_insuficiente](<evidencias_imagens/17_http_sacar_insuficiente.png>)

## Conclusão

- Encapsulamento evidenciado por: campos privados, propriedades read-only, métodos controladores de estado e exposição via DTO/View.
