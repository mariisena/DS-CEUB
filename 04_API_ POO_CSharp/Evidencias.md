# Evidências — Atividade 4 (API OOP em C#/.NET)

## Ambiente

- SO: Windows 11
- .NET SDK: 9.0
- Editor: VS Code

## Execução

- `dotnet run` → URL: <http://localhost:5275>
  
![terminal](<evidencias_imagens/01_execução.png>)

## Swagger

![TelaInicial](<evidencias_imagens/02_swagger_inicial.png>)

- GET /personagens

![GET /personagens](<evidencias_imagens/03_swagger_get_personagens.png>)
![GET /personagens](<evidencias_imagens/04_swagger_get_personagens.png>)

- POST /personagens — 201

![POST /personagens](<evidencias_imagens/05_swagger_post_personagens.png>)

- GET /personagens/2 — 200

![GET /personagens/{id}](<evidencias_imagens/06_swagger_get_personagens_200.png>)
![GET /personagens/{id}](<evidencias_imagens/07_swagger_get_personagens_200.png>)

- GET /personagens/999

![GET /personagens/{id}](<evidencias_imagens/08_swagger_get_personagens_404.png>)
![GET /personagens/{id}](<evidencias_imagens/09_swagger_get_personagens_404.png>)

- GET /personagens/{id}/ataque

![ataque](<evidencias_imagens/10_swagger_get_personagens_ataque.png>)
![ataque](<evidencias_imagens/11_swagger_get_personagens_ataque.png>)

## VS Code REST Client

- Arquivo `APIOOPpersonagens.http`

![ListarTodos](<evidencias_imagens/12_http_listar_todos.png>)
![Filtrar](<evidencias_imagens/13_http_filtrar_por_classe.png>)
![Buscar](<evidencias_imagens/14_http_buscar_por_id.png>)
![Buscar](<evidencias_imagens/15_http_buscar_por_id.png>)
![Criar](<evidencias_imagens/16_http_criar.png>)
![Polimorfismo](<evidencias_imagens/17_http_polimorfismo.png>)
