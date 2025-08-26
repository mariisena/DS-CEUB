using APIOOPpersonagens.Models.Abstracoes;

namespace APIOOPpersonagens.Models;

public class Shinigami : PersonagemBase
{
    public override string Classe => "Shinigami";
    public string Zanpakuto { get; set; } = "Zangetsu";
    public override string Atacar() => $"{Nome} lança Getsuga Tensho com {Zanpakuto}!";
}