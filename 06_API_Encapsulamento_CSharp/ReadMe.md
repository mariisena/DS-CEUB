# Atividade 6 — API com Encapsulamento em C#/.NET

Este repositório contém a implementação de uma API REST em C#/.NET com foco no conceito de Encapsulamento.
A API simula um sistema de contas bancárias, protegendo os atributos internos e permitindo operações apenas por métodos controlados (Depositar, Sacar).

---

## 📌 Objetivo da Atividade

- Demonstrar encapsulamento em classes.
- Proteger atributos internos com campos privados e propriedades de leitura.
- Utilizar métodos controlados para alterar estado (Depositar, Sacar).
- Expor dados ao cliente via DTO/View (sem vazar os objetos internos).
- Consumir a API via Swagger, VS Code REST Client (.http) ou Postman.
- Documentar evidências de funcionamento.

---

## 📃 Estrutura do Projeto

```bash
/APIEncap
├── Controllers/
│   └── ContasController.cs
├── Models/
│   ├── Abstracoes/
│   │   └── EntidadeBase.cs
│   ├── ContaBancaria.cs
│   └── DTOs/
│       ├── CriarContaDto.cs
│       ├── DepositarDto.cs
│       └── ContaView.cs
├── Services/
│   ├── IContaService.cs
│   └── ContaService.cs
├── Program.cs
├── APIEncap.csproj
└── APIEncap.http   (arquivo para VS Code REST Client)
```

---

## 🚀 Como rodar a API

```bash
dotnet restore
dotnet build
dotnet run
```

A aplicação deve subir em algo como:

```Now listening on: <http://localhost:5134>```

Acesse no navegador:

- Swagger: <http://localhost:5134/swagger>
- Endpoint base: <http://localhost:5134/contas>

---

## 📚 Endpoints disponíveis

`GET /contas` → lista todas as contas
`GET /contas/{id}` → busca uma conta por ID
`POST /contas → cria` uma nova conta
`POST /contas/{id}/depositar` → deposita valor
`POST /contas/{id}/sacar` → saca valor

Exemplo de criação de conta (POST /contas):

```bash
{
  "titular": "Mari",
  "numeroConta": "0001-9",
  "depositoInicial": 100
}
```

Exemplo de depósito:
```{ "valor": 50 }```

---

## 🛠️ Testando a API

### 1) Swagger

Acesse <http://http://localhost:5134/swagger>

Use Try it out para executar criação, depósito e saque

---

### 2) VS Code REST Client

Arquivo `APIEncap.http` contém requests como:

```http
@base = http://localhost:5134

### Criar conta
POST {{base}}/contas
Content-Type: application/json

{
  "titular": "Mari",
  "numeroConta": "0001-9",
  "depositoInicial": 100
}

### Depositar
POST {{base}}/contas/1/depositar
Content-Type: application/json

{ "valor": 50 }
```

---

## 📷 Evidências

As evidências estão documentadas em Evidencias_ATV6.md (prints do Swagger e REST Client).

---

## ✅ Conclusão

- API criada para exemplificar encapsulamento em C#.
- Campos privados e métodos controlam alterações do estado (_saldo).
- Saída controlada via ContaView (não expõe objeto interno).
- Testada via Swagger, VS Code REST Client e Postman.
- Evidências anexadas no repositório.
