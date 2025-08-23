# Importando bibliotecas necessárias
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)  # criando aplicação Flask
api = Api(
    app,
    title="API de personagens",
    version="1.0",
    description="API REST de personagens de anime com Swagger (Flask-RESTx)",
)

ns = api.namespace("personagens", description="Operações com personagens")

# Modelo usado para validar e documentar os dados
personagem_model = api.model(
    "Personagem",
    {
        "nome": fields.String(
            required=True, description="Nome do personagem", example="Naruto Uzumaki"
        ),
        "universo": fields.String(
            required=True, description="Universo de origem", example="Naruto"
        ),
        "poder_principal": fields.String(
            required=True, description="Habilidade principal", example="Rasengan"
        ),
    },
)

personagem_out = api.inherit(
    "PersonagemOut",
    personagem_model,
    {
        "id": fields.Integer(
            readonly=True, description="Identificador gerado pelo servidor", example=11
        )
    },
)

erro_out = api.model(
    "Erro",
    {
        "detail": fields.String(
            description="Descrição do erro", example="Personagem não encontrado."
        )
    },
)

# "Base de dados" fictícia em memória
personagens = [
    {"id": 1, "nome": "Naruto", "universo": "Naruto", "poder_principal": "Rasengan"},
    {"id": 2, "nome": "Luffy", "universo": "One Piece", "poder_principal": "Gomu Gomu"},
    {"id": 3, "nome": "Ichigo", "universo": "Bleach", "poder_principal": "Getsuga Tensho"},
    {"id": 4, "nome": "Sasuke", "universo": "Naruto", "poder_principal": "Sharingan/Rinnegan"},
    {"id": 5, "nome": "Tanjiro Kamado", "universo": "Demon Slayer", "poder_principal": "Respiração do Sol"},
    {"id": 6, "nome": "Goku", "universo": "Dragon Ball", "poder_principal": "Kamehameha"},
    {"id": 7, "nome": "Izuku Midoriya", "universo": "My Hero Academia", "poder_principal": "One For All"},
    {"id": 8, "nome": "Gojo Satoru", "universo": "Jujutsu Kaisen", "poder_principal": "Ilimitado"},
    {"id": 9, "nome": "Eren Yeager", "universo": "Attack on Titan", "poder_principal": "Titã de Ataque"},
    {"id": 10, "nome": "Gon Freecss", "universo": "Hunter x Hunter", "poder_principal": "Jajanken"},
]
proximo_id = 11

def buscar_por_id(id: int):
    """Função de ajuda para encontrar um personagem pelo ID."""
    return next((p for p in personagens if p["id"] == id), None)

# LISTA + CRIAÇÃO
@ns.route("/")
class ListaPersonagens(Resource):
    @ns.doc(
        "listar_personagens",
        params={
            "universo": "Filtra por universo exato (ex.: Naruto, One Piece)",
            "limit": "Quantidade máxima de itens (default=50)",
            "offset": "Deslocamento/paginação (default=0)",
        },
    )
    @ns.marshal_list_with(personagem_out, code=200)
    def get(self):
        """Lista personagens com filtro por universo e paginação"""
        universo = request.args.get("universo", type=str)
        limit = request.args.get("limit", default=50, type=int)
        offset = request.args.get("offset", default=0, type=int)

        data = personagens
        if universo:
            data = [p for p in data if p["universo"].lower() == universo.lower()]

        # paginação simples
        total = len(data)
        data = data[offset : offset + limit]

        return data, 200, {"X-Total-Count": str(total)}

    @ns.doc("criar_personagem")
    @ns.expect(personagem_model, validate=True)
    @ns.marshal_with(personagem_out, code=201, description="Criado")
    @ns.response(400, "Requisição inválida", erro_out)
    def post(self):
        """Adiciona um novo personagem"""
        global proximo_id
        data = request.json or {}
        novo = {
            "id": proximo_id,
            "nome": data["nome"].strip(),
            "universo": data["universo"].strip(),
            "poder_principal": data["poder_principal"].strip(),
        }
        personagens.append(novo)
        proximo_id += 1
        return novo, 201  # HTTP 201 = Created

# BUSCA / ATUALIZA / REMOVE POR ID
@ns.route("/<int:id>")
@ns.param("id", "ID do personagem", _in="path")
class Personagem(Resource):
    @ns.doc("obter_personagem")
    @ns.marshal_with(personagem_out, code=200)
    @ns.response(404, "Não encontrado", erro_out)
    def get(self, id):
        """Busca o personagem pelo ID"""
        p = buscar_por_id(id)
        if not p:
            api.abort(404, "Personagem não encontrado.")
        return p, 200

    @ns.doc("atualizar_personagem")
    @ns.expect(personagem_model, validate=True)
    @ns.marshal_with(personagem_out, code=200, description="Atualizado")
    @ns.response(404, "Não encontrado", erro_out)
    def put(self, id):
        """Atualiza COMPLETAMENTE um personagem (PUT)"""
        p = buscar_por_id(id)
        if not p:
            api.abort(404, "Personagem não encontrado.")
        data = request.json
        p.update(
            {
                "nome": data["nome"].strip(),
                "universo": data["universo"].strip(),
                "poder_principal": data["poder_principal"].strip(),
            }
        )
        return p, 200

    @ns.doc("remover_personagem")
    @ns.response(204, "Removido com sucesso")
    @ns.response(404, "Não encontrado", erro_out)
    def delete(self, id):
        """Remove um personagem pelo id"""
        p = buscar_por_id(id)
        if not p:
            api.abort(404, "Personagem não encontrado.")
        personagens.remove(p)
        return "", 204

# Rota raiz / saúde
@app.get("/")
def raiz():
    return {"status": "ok", "swagger": "veja a UI neste mesmo host"}

if __name__ == "__main__":
    app.run(debug=True)  # por padrão: http://127.0.0.1:5000