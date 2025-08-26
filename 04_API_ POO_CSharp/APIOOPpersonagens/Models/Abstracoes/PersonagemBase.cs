namespace APIOOPpersonagens.Models.Abstracoes;

public abstract class PersonagemBase
{
    public int Id { get; private set; }
    public string Nome { get; set; } = null!;
    public string Universo { get; set; } = null!;

    // Exposto para o cliente sem precisar de RTTI
    public abstract string Classe { get; }

    // Método abstrato: cada subclasse implementa seu "estilo" de ataque
    public abstract string Atacar();

    public virtual string Apresentar() => $"{Nome} de {Universo} — classe {Classe}";

    // Controle interno de Id (sem set público)
    public void DefinirId(int id) => Id = id;
}