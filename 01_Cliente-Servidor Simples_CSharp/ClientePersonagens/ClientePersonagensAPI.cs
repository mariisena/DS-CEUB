using System.Net.Http.Json;
using System.Text.Json;

const string BASE = "http://localhost:5066"; // ajuste para sua porta/protocolo

var http = new HttpClient { BaseAddress = new Uri(BASE) };
var opts = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };

Console.WriteLine("--- Cliente da API Personagens ---\n");

// 1) GET lista
Console.WriteLine("Listando personagens...");
var lista = await http.GetFromJsonAsync<List<Personagem>>("/personagens", opts);
Console.WriteLine($"Recebidos: {lista?.Count} itens\n");

// 2) GET por ID existente
Console.WriteLine("Buscando personagem ID 3...");
var p3 = await http.GetFromJsonAsync<Personagem>("/personagens/3", opts);
Console.WriteLine(p3 is null ? "Não encontrado" : $"Encontrado: {p3.Nome} ({p3.Universo})\n");

// 3) GET por ID inexistente (tratando 404)
Console.WriteLine("Buscando personagem ID 999...");
var r404 = await http.GetAsync("/personagens/999");
Console.WriteLine($"Status: {(int)r404.StatusCode} {r404.StatusCode}\n");

// 4) POST criar novo
Console.WriteLine("Criando novo personagem (Gojo)...");
var novo = new CriarPersonagemDto("Satoru Gojo", "Jujutsu Kaisen", "Infinito");
var rpost = await http.PostAsJsonAsync("/personagens", novo);
Console.WriteLine($"Status: {(int)rpost.StatusCode} {rpost.StatusCode}");
var criado = await rpost.Content.ReadFromJsonAsync<Personagem>(opts);
Console.WriteLine(criado is null ? "Erro ao criar" : $"Criado com Id {criado.Id}\n");

Console.WriteLine("Fim. Pressione ENTER para sair.");
Console.ReadLine();

record Personagem(int Id, string Nome, string Universo, string PoderPrincipal);
record CriarPersonagemDto(string Nome, string Universo, string PoderPrincipal);