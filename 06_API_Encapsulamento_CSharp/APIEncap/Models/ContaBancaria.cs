using APIEncap.Models.Abstracoes;

namespace APIEncap.Models;

public class ContaBancaria : EntidadeBase
{
    private decimal _saldo;

    public string Titular { get; private set; }
    public string NumeroConta { get; private set; }

    // Propriedade somente leitura pública, escrita controlada internamente
    public decimal Saldo => _saldo;

    // Encapsula criação garantindo invariantes
    public ContaBancaria(string titular, string numeroConta, decimal depositoInicial)
    {
        if (string.IsNullOrWhiteSpace(titular))
            throw new ArgumentException("Titular obrigatório.");
        if (string.IsNullOrWhiteSpace(numeroConta))
            throw new ArgumentException("Número da conta obrigatório.");
        if (depositoInicial < 0)
            throw new ArgumentException("Depósito inicial não pode ser negativo.");

        Titular = titular.Trim();
        NumeroConta = numeroConta.Trim();
        _saldo = 0m;
        if (depositoInicial > 0)
            Depositar(depositoInicial, "Depósito inicial");
    }

    // Único caminho para alterar _saldo — regras ficam aqui
    public void Depositar(decimal valor, string? descricao = null)
    {
        if (valor <= 0)
            throw new ArgumentException("Valor de depósito deve ser positivo.");
        _saldo += valor;
        MarcarAtualizado();
        // (log/auditoria poderiam ser disparados aqui)
    }

    public void Sacar(decimal valor, string? descricao = null)
    {
        if (valor <= 0)
            throw new ArgumentException("Valor de saque deve ser positivo.");
        if (valor > _saldo)
            throw new InvalidOperationException("Saldo insuficiente.");
        _saldo -= valor;
        MarcarAtualizado();
    }
}