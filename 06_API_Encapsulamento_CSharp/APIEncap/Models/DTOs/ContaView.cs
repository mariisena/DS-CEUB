namespace APIEncap.Models.DTOs;

// Exposta para o cliente — não revela campos privados
public record ContaView(int Id, string Titular, string NumeroConta, decimal Saldo, string CriadoEm, string? AtualizadoEm);