using APIpersonagens.Models;
using System.Collections.Concurrent;

namespace APIpersonagens.Data;

public static class PersonagemStore
{
    private static readonly ConcurrentBag<Personagem> _personagens = new()
    {
        new () {Id = 1, Nome = "Naruto Uzumaki", Universo = "Naruto", PoderPrincipal = "Rasengan"},
        new () {Id = 2, Nome = "Luffy", Universo = "One Piece", PoderPrincipal =  "Gomu Gomu"},
        new () {Id = 3, Nome = "Ichigo", Universo = "Bleach", PoderPrincipal =  "Getsuga Tensho"},
        new () {Id = 4, Nome = "Sasuke", Universo = "Naruto", PoderPrincipal =  "Sharingan/Rinnegan"},
        new () {Id = 5, Nome = "Tanjiro Kamado", Universo = "Demon Slayer", PoderPrincipal = "Respiração do Sol"},
        new () {Id = 6, Nome = "Goku", Universo = "Dragon Ball", PoderPrincipal = "Kamehameha"},
        new () {Id = 7, Nome = "Izuku Midoriya", Universo = "My Hero Academia", PoderPrincipal = "One For All"},
        new () {Id = 8, Nome = "Gojo Satoru", Universo = "Jujutsu Kaisen", PoderPrincipal = "Ilimitado"},
        new () {Id = 9, Nome = "Eren Yeager", Universo = "Attack on Titan", PoderPrincipal = "Titã de Ataque"},
        new () {Id = 10, Nome = "Gon Freecss", Universo = "Hunter x Hunter", PoderPrincipal = "Jajanken"},
    };

    private static int _proximoId = 11;

    public static List<Personagem> GetPersonagens() => _personagens.OrderBy(p => p.Id).ToList();
    public static Personagem? GetPersonagensPorId(int id) => _personagens.FirstOrDefault(p => p.Id == id);
    public static Personagem AddPersonagem(string nome, string universo, string poder)
    {
        var novoId = Interlocked.Increment(ref _proximoId);

        var novoPersonagem = new Personagem
        {
            Id = novoId,
            Nome = nome,
            Universo = universo,
            PoderPrincipal = poder
        };

        _personagens.Add(novoPersonagem);
        return novoPersonagem;
    }
}
