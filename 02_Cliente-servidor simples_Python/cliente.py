"""
cliente.py — Versão "script" (não interativa) do cliente HTTP para a API de Personagens (Flask-RESTx + Swagger).

- Consome endpoints REST usando `requests`.
- Mostra exemplos de: listar, obter por ID, criar, atualizar (PUT) e remover (DELETE).
- BASE_URL configurável por variável de ambiente `API_BASE_URL`.

API_BASE_URL=http://127.0.0.1:5000/personagens python cliente.py
"""
from __future__ import annotations
import os
import json
from typing import Any, Dict, Optional

# Importando bibliotecas
import requests
from requests import Response

# Definição do endereço base da API
BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:5000/personagens").rstrip("/")
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "10"))

session = requests.Session()

# --------------- utilidades ---------------
def is_json_response(resp: Response) -> bool:
    ctype = resp.headers.get("Content-Type", "").lower()
    return ctype.startswith("application/json") or ctype.endswith("+json")

def print_json(data: Any) -> None:
    try:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception:
        print(str(data))

def print_resp(resp: Response, *, show_headers: bool = True) -> None:
    print("-" * 60)
    print(f"HTTP {resp.status_code}")
    if show_headers:
        total = resp.headers.get("X-Total-Count")
        if total is not None:
            print(f"X-Total-Count: {total}")
        ctype = resp.headers.get("Content-Type")
        if ctype:
            print(f"Content-Type: {ctype}")
    if is_json_response(resp):
        try:
            print_json(resp.json())
        except Exception:
            print(resp.text)
    else:
        print(resp.text)

# --------------- wrappers HTTP ---------------

def listar(*, universo: Optional[str] = None, limit: int = 50, offset: int = 0) -> Response:
    params = {"limit": limit, "offset": offset}
    if universo:
        params["universo"] = universo
    return session.get(f"{BASE_URL}/", params=params, timeout=TIMEOUT)

def obter_por_id(pid: int) -> Response:
    return session.get(f"{BASE_URL}/{pid}", timeout=TIMEOUT)

def criar(payload: Dict[str, Any]) -> Response:
    return session.post(f"{BASE_URL}/", json=payload, timeout=TIMEOUT)

def atualizar(pid: int, payload: Dict[str, Any]) -> Response:
    return session.put(f"{BASE_URL}/{pid}", json=payload, timeout=TIMEOUT)

def remover(pid: int) -> Response:
    return session.delete(f"{BASE_URL}/{pid}", timeout=TIMEOUT)

# --------------- fluxo de exemplo ---------------

def main() -> None:
    print(f"Consumindo API em: {BASE_URL}")

    try:
        # 1) Listar (sem filtro)
        print("\n[1] GET lista")
        r = listar()
        print_resp(r)

        # 2) Criar um novo personagem
        print("\n[2] POST criar")
        novo = {
            "nome": "Edward Elric",
            "universo": "Fullmetal Alchemist",
            "poder_principal": "Alquimia",
        }
        r = criar(novo)
        print_resp(r)
        created_id = None
        if is_json_response(r) and r.status_code == 201:
            created_id = r.json().get("id")

        # 3) Listar com filtro/paginação
        print("\n[3] GET lista (filtro=Naruto, limit=2)")
        r = listar(universo="Naruto", limit=2, offset=0)
        print_resp(r)

        # 4) Obter por ID (o criado se possível, senão 1)
        alvo = created_id or 1
        print(f"\n[4] GET por ID ({alvo})")
        r = obter_por_id(alvo)
        print_resp(r)

        # 5) Atualizar (PUT) — só se foi criado agora
        if created_id is not None:
            print(f"\n[5] PUT atualizar ({created_id})")
            alterado = {
                "nome": "Edward Elric",
                "universo": "Fullmetal Alchemist",
                "poder_principal": "Alquimia Avançada",
            }
            r = atualizar(created_id, alterado)
            print_resp(r)

        # 6) Remover — só se foi criado agora
        if created_id is not None:
            print(f"\n[6] DELETE remover ({created_id})")
            r = remover(created_id)
            print_resp(r)

        # 7) Listar final
        print("\n[7] GET lista (final)")
        r = listar()
        print_resp(r)

    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão (a API está rodando?): {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")

if __name__ == "__main__":
    main()