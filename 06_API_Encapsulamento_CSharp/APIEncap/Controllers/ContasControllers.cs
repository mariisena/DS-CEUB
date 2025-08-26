using Microsoft.AspNetCore.Mvc;
using APIEncap.Models.DTOs;
using APIEncap.Services;


namespace APIEncap.Controllers;


[ApiController]
[Route("contas")]
public class ContasController : ControllerBase
{
    private readonly IContaService _svc;
    public ContasController(IContaService svc) => _svc = svc;


    [HttpGet]
    public IActionResult Listar() => Ok(_svc.Listar());


    [HttpGet("{id:int}")]
    public IActionResult Buscar(int id)
    => _svc.BuscarPorId(id) is { } v ? Ok(v) : NotFound(new { detail = "Conta não encontrada." });


    [HttpPost]
    public IActionResult Criar([FromBody] CriarContaDto dto)
    {
        try { var criada = _svc.Criar(dto); return CreatedAtAction(nameof(Buscar), new { id = criada.Id }, criada); }
        catch (ArgumentException ex) { return ValidationProblem(ex.Message); }
    }


    [HttpPost("{id:int}/depositar")]
    public IActionResult Depositar(int id, [FromBody] DepositarDto dto)
    {
        try { return Ok(_svc.Depositar(id, dto)); }
        catch (KeyNotFoundException) { return NotFound(new { detail = "Conta não encontrada." }); }
        catch (ArgumentException ex) { return ValidationProblem(ex.Message); }
    }


    [HttpPost("{id:int}/sacar")]
    public IActionResult Sacar(int id, [FromBody] DepositarDto dto)
    {
        try { return Ok(_svc.Sacar(id, dto)); }
        catch (KeyNotFoundException) { return NotFound(new { detail = "Conta não encontrada." }); }
        catch (ArgumentException ex) { return ValidationProblem(ex.Message); }
        catch (InvalidOperationException ex) { return Problem(title: "Operação inválida", detail: ex.Message, statusCode: 400); }
    }
}