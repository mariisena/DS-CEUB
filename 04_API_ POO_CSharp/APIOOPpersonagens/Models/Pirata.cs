using APIOOPpersonagens.Models.Abstracoes;

namespace APIOOPpersonagens.Models;

public class Pirata : PersonagemBase
{
    public override string Classe => "Pirata";
    public string Haki { get; set; } = "Haki do Rei";
    public override string Atacar() => $"{Nome} ativa {Haki} e estica o braço!";
}