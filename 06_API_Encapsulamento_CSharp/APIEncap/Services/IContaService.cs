using APIEncap.Models;
using APIEncap.Models.DTOs;


namespace APIEncap.Services;


public interface IContaService
{
    IReadOnlyList<ContaView> Listar();
    ContaView? BuscarPorId(int id);
    ContaView Criar(CriarContaDto dto);
    ContaView Depositar(int id, DepositarDto dto);
    ContaView Sacar(int id, DepositarDto dto);
}