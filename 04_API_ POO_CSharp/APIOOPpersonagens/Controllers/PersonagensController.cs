using Microsoft.AspNetCore.Mvc;
using APIOOPpersonagens.Models.DTOs;
using APIOOPpersonagens.Services;


namespace APIOOPpersonagens.Controllers;


[ApiController]
[Route("personagens")]
public class PersonagensController : ControllerBase
{
    private readonly IPersonagemService _svc;
    public PersonagensController(IPersonagemService svc) => _svc = svc;


    // GET /personagens?classe=Ninja
    [HttpGet]
    public IActionResult Listar([FromQuery] string? classe)
    => Ok(_svc.Listar(classe));


    // GET /personagens/{id}
    [HttpGet("{id:int}")]
    public IActionResult Buscar(int id)
    => _svc.BuscarPorId(id) is { } p ? Ok(p) : NotFound(new { detail = "Personagem não encontrado." });


    // POST /personagens
    [HttpPost]
    public IActionResult Criar([FromBody] CriarPersonagemDto dto)
    {
        try
        {
            var criado = _svc.Criar(dto);
            return CreatedAtAction(nameof(Buscar), new { id = GetId(criado) }, criado);
        }
        catch (ArgumentException ex)
        {
            return ValidationProblem(ex.Message);
        }
    }


    // GET /personagens/{id}/ataque
    [HttpGet("{id:int}/ataque")]
    public IActionResult Atacar(int id)
    {
        try
        {
            var msg = _svc.Atacar(id);
            var p = _svc.BuscarPorId(id)!;
            return Ok(new { id = GetId(p), classe = p.Classe, ataque = msg });
        }
        catch (KeyNotFoundException)
        {
            return NotFound(new { detail = "Personagem não encontrado." });
        }
    }


    // helper: obter Id (mesma estratégia do service)
    private static int GetId(object p) => (int)(p.GetType().GetProperty("Id")!.GetValue(p)!);
}