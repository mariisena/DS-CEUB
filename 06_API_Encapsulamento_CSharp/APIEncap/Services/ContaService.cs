using APIEncap.Models;
using APIEncap.Models.DTOs;

namespace APIEncap.Services;

public class ContaService : IContaService
{
    private readonly List<ContaBancaria> _contas = new();
    private int _nextId = 1;
    private readonly object _lock = new();

    public ContaService()
    {
        // Dados de teste que aparecerão ao iniciar a API
        var conta1 = new ContaBancaria("Clark Kent", "007", 1500.50m);
        conta1.DefinirId(_nextId++);
        _contas.Add(conta1);

        var conta2 = new ContaBancaria("Bruce Wayne", "001", 99999.99m);
        conta2.DefinirId(_nextId++);
        _contas.Add(conta2);

        var conta3 = new ContaBancaria("Diana Prince", "1984", 5000m);
        conta3.DefinirId(_nextId++);
        _contas.Add(conta3);
    }


    public IReadOnlyList<ContaView> Listar() => _contas.Select(Map).ToList();


    public ContaView? BuscarPorId(int id)
    {
        var c = _contas.FirstOrDefault(x => GetId(x) == id);
        return c is null ? null : Map(c);
    }


    public ContaView Criar(CriarContaDto dto)
    {
        var conta = new ContaBancaria(dto.Titular, dto.NumeroConta, dto.DepositoInicial);
        lock (_lock)
        {
            conta.DefinirId(_nextId++);
            _contas.Add(conta);
        }
        return Map(conta);
    }


    public ContaView Depositar(int id, DepositarDto dto)
    {
        lock (_lock)
        {
            var c = _contas.FirstOrDefault(x => GetId(x) == id) ?? throw new KeyNotFoundException("Conta não encontrada.");
            c.Depositar(dto.Valor);
            return Map(c);            
        }
    }


    public ContaView Sacar(int id, DepositarDto dto)
    {
        lock (_lock)
        {
            var c = _contas.FirstOrDefault(x => GetId(x) == id) ?? throw new KeyNotFoundException("Conta não encontrada.");
            c.Sacar(dto.Valor);
            return Map(c);            
        }

    }


    private static int GetId(ContaBancaria c) => c.Id;


    private static ContaView Map(ContaBancaria c) => new(
        Id: GetId(c),
        Titular: c.Titular,
        NumeroConta: c.NumeroConta,
        Saldo: c.Saldo,
        CriadoEm: c.CriadoEm.ToString("O"),
        AtualizadoEm: c.AtualizadoEm?.ToString("O")
    );
}