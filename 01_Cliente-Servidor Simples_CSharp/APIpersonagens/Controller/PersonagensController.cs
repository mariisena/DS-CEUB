using Microsoft.AspNetCore.Mvc;
using APIpersonagens.Data;
using APIpersonagens.Models;

namespace APIpersonagens.Controller;

[ApiController]
[Route("personagens")]
public class PersonagensController : ControllerBase
{
    [HttpGet]
    public IActionResult Listar([FromQuery] string? universo, [FromQuery] int limit = 50, [FromQuery] int offset = 0)
    {
        var personagens = PersonagemStore.GetPersonagens().AsQueryable();

        if (!string.IsNullOrEmpty(universo))
        {
            personagens = personagens.Where(p => p.Universo.Equals(universo, StringComparison.OrdinalIgnoreCase));
        }

        Response.Headers.Append("X-Total-Count", personagens.Count().ToString());

        var resultadoPaginado = personagens.Skip(offset).Take(limit).ToList();

        return Ok(resultadoPaginado);
    }

    // GET /personagens/{id}
    [HttpGet("{id:int}")]
    public IActionResult BuscarPorId(int id)
    {
        var personagens = PersonagemStore.GetPersonagensPorId(id);
        if (personagens is null)
        {
            return NotFound(new { Detail = "Personagem não encontrado." });
        }
        return Ok(personagens);
    }

    //  DTO (Data Transfer Object) para a criação, sem o campo Id
    public record CriarPersonagemDto(string Nome, string Universo, string PoderPrincipal);

    // POST /personagens
    [HttpPost]
    public IActionResult Criar([FromBody] CriarPersonagemDto novoPersonagemDto)
    {
        var personagemCriado = PersonagemStore.AddPersonagem(
            novoPersonagemDto.Nome,
            novoPersonagemDto.Universo,
            novoPersonagemDto.PoderPrincipal
        );

        // Retorna 201 Created com a localização do novo recurso
        return CreatedAtAction(nameof(BuscarPorId), new { id = personagemCriado.Id }, personagemCriado);
    }
}
