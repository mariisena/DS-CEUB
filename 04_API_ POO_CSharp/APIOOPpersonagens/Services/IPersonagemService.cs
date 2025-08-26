using APIOOPpersonagens.Models.Abstracoes;
using APIOOPpersonagens.Models.DTOs;

namespace APIOOPpersonagens.Services;

public interface IPersonagemService
{
    IReadOnlyList<PersonagemBase> Listar(string? classe = null);
    PersonagemBase? BuscarPorId(int id);
    PersonagemBase Criar(CriarPersonagemDto dto);
    string Atacar(int id);
}