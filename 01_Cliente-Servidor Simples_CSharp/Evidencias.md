# Evidências — Atividade 1 (API Personagens)

## Ambiente

- SO: Windows 10/11
- .NET SDK: 8.0/9.0
- IDE: VS Code

## Execução

- `dotnet run` → URLs: `http://localhost:5066`

![ExecutandoAPI](<evidencias_imagens/01_dotnet_run.png>)

## Swagger

- ### Tela inicial da UI 
  
![TelaInicial](<evidencias_imagens/02_Swagger_TelaInicial.png>)

- ### ``GET /personagens`` — **200**

![GET /personagens](<evidencias_imagens/03_Swagger_GET_personagens_200.png>)

- ### ``GET /personagens/3`` — **200**

![GET /personagens/3](<evidencias_imagens/04_Swagger_GET_personagens_3_200.png>)

- ### ``GET /personagens/999`` — **404**

![GET /personagens/999](<evidencias_imagens/04_Swagger_GET_personagens_999_404.png>)

- ### ``POST /personagens`` — **201**

![POST /personagens](<evidencias_imagens/05_Swagger_POST_personagens.png>)
![POST /personagens](<evidencias_imagens/05_Swagger_POST_personagens_201.png>)
  
## VS Code REST Client

### Arquivo `APIpersonagens.http`(pasta APIpersonagens)

![APIpersonagens.http](<evidencias_imagens/06_APIpersonagens_http.png>)

### Execução das requisições

![APIpersonagens.http](<evidencias_imagens/06_APIpersonagens_http.png>)
![APIpersonagens.http](<evidencias_imagens/07_APIpersonagens_http_Lista (sem filtro).png>)
![APIpersonagens.http](<evidencias_imagens/08_APIpersonagens_http_Lista filtrando por universo.png>)
![APIpersonagens.http](<evidencias_imagens/09_APIpersonagens_http_Busca por ID.png>)
![APIpersonagens.http](<evidencias_imagens/10_APIpersonagens_http_Busca por ID.png>)
![APIpersonagens.http](<evidencias_imagens/11_APIpersonagens_http_criar.png>)

## Cliente Console

- Saída do terminal

![ClienteCOnsole](<evidencias_imagens/12_Cliente_console.png>)
