namespace APIEncap.Models.Abstracoes;

public abstract class EntidadeBase
{
    public int Id { get; internal set; } // Acessível dentro do projeto, mas não externamente
    public DateTime CriadoEm { get; private set; } = DateTime.UtcNow;
    public DateTime? AtualizadoEm { get; private set; }

    public void DefinirId(int id) => Id = id;
    protected void MarcarAtualizado() => AtualizadoEm = DateTime.UtcNow;
}