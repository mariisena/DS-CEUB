namespace APIOOPpersonagens.Models.DTOs;

public record CriarPersonagemDto(
    string Tipo, // "ninja" | "pirata" | "shinigami"
    string Nome,
    string Universo,
    string? Atributo // Técnica/Haki/Zanpakuto (opcional)
);