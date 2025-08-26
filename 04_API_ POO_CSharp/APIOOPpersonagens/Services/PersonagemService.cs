using System.Collections.Concurrent;
using APIOOPpersonagens.Models;
using APIOOPpersonagens.Models.Abstracoes;
using APIOOPpersonagens.Models.DTOs;


namespace APIOOPpersonagens.Services;

public class PersonagemService : IPersonagemService
{
    private readonly List<PersonagemBase> _itens = new()
    {
        new Ninja { Nome = "Naruto", Universo = "Naruto", Tecnica = "Rasengan" },
        new Pirata { Nome = "Luffy", Universo = "One Piece", Haki = "Haki do Rei" },
        new Shinigami { Nome = "Ichigo", Universo = "Bleach", Zanpakuto = "Zangetsu" }
    };
    private int _nextId = 1;
    private readonly object _lock = new();


    public PersonagemService()
    {
        // atribui Ids iniciais
        for (int i = 0; i < _itens.Count; i++)
            _itens[i].DefinirId(_nextId++);
    }


    public IReadOnlyList<PersonagemBase> Listar(string? classe = null)
    {
        IEnumerable<PersonagemBase> q = _itens;
        if (!string.IsNullOrWhiteSpace(classe))
            q = q.Where(p => p.Classe.Equals(classe, StringComparison.OrdinalIgnoreCase));
        return q.OrderBy(p => p.Apresentar()).ToList();
    }

    public PersonagemBase? BuscarPorId(int id) => _itens.FirstOrDefault(p => GetId(p) == id);


    public PersonagemBase Criar(CriarPersonagemDto dto)
    {
        var tipo = dto.Tipo?.Trim().ToLowerInvariant();
        PersonagemBase novo = tipo switch
        {
            "ninja" => new Ninja { Nome = dto.Nome, Universo = dto.Universo, Tecnica = dto.Atributo ?? "Rasengan" },
            "pirata" => new Pirata { Nome = dto.Nome, Universo = dto.Universo, Haki = dto.Atributo ?? "Haki do Rei" },
            "shinigami" => new Shinigami { Nome = dto.Nome, Universo = dto.Universo, Zanpakuto = dto.Atributo ?? "Zangetsu" },
            _ => throw new ArgumentException("Tipo inválido. Use: ninja | pirata | shinigami.")
        };


        lock (_lock)
        {
            novo.DefinirId(_nextId++);
            _itens.Add(novo);
        }
        return novo;
    }


    public string Atacar(int id)
    {
        var p = BuscarPorId(id) ?? throw new KeyNotFoundException("Personagem não encontrado.");
        // POLIMORFISMO: chama a implementação concreta de Atacar()
        return p.Atacar();
    }

    private static int GetId(PersonagemBase p)
    {
        // gambit: refletir via Apresentar/ToString? Melhor expor método para leitura do Id
        // já temos DefinirId e campo privado, então usamos reflexão mínima:
        var prop = typeof(PersonagemBase).GetProperty("Id");
        return (int)(prop!.GetValue(p) ?? 0);
    }
}