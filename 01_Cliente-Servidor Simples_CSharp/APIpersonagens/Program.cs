var builder = WebApplication.CreateBuilder(args);

// Adiciona serviços ao contêiner.
builder.Services.AddControllers();

// Adiciona o gerador de Swagger 
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configura o pipeline de requisições HTTP.
if (app.Environment.IsDevelopment())
{
    // Habilita o Swagger e a UI do Swagger
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();

// Mapeia os controladores para que as rotas funcionem
app.MapControllers();

app.Run();