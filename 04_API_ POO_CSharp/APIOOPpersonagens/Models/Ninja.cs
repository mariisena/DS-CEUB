using APIOOPpersonagens.Models.Abstracoes;

namespace APIOOPpersonagens.Models;

public class Ninja : PersonagemBase
{
    public override string Classe => "Ninja";
    public string Tecnica { get; set; } = "Rasengan";
    public override string Atacar() => $"{Nome} usa {Tecnica}!";
}