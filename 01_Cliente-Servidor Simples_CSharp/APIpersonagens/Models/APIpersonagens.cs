namespace APIpersonagens.Models;

public class Personagem
{
    public int Id { get; init; }
    public required string Nome { get; init; }
    public required string Universo { get; init; }
    public required string PoderPrincipal { get; init; }
}