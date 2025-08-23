#!/usr/bin/env python3
"""
Cliente de console interativo para a API de Personagens (Flask-RESTx).

Funcionalidades:
- Listar (com filtros: universo, limit, offset)
- Obter por ID
- Criar
- Atualizar (PUT)
- Remover (DELETE)

Configuração:
  API_BASE_URL=http://127.0.0.1:5000/personagens
"""
from __future__ import annotations
import os
import sys
import json
from typing import Any, Dict, Optional

import requests
from requests import Response

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:5000/personagens").rstrip("/")
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "10"))

# ----------------- utilidades -----------------

def is_json_response(resp: Response) -> bool:
    ctype = resp.headers.get("Content-Type", "").lower()
    return ctype.startswith("application/json") or ctype.endswith("+json")


def print_json(data: Any) -> None:
    try:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception:
        print(str(data))


def print_resp(resp: Response) -> None:
    """Imprime resposta com sensibilidade a JSON e mostra status/headers úteis."""
    print(f"HTTP {resp.status_code}")
    total = resp.headers.get("X-Total-Count")
    if total is not None:
        print(f"X-Total-Count: {total}")
    if is_json_response(resp):
        try:
            print_json(resp.json())
        except Exception:
            print(resp.text)
    else:
        print(resp.text)


def read_nonempty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("⚠️  Campo obrigatório. Tente novamente.")


def read_int(prompt: str, *, allow_empty: bool = False) -> Optional[int]:
    while True:
        raw = input(prompt).strip()
        if allow_empty and raw == "":
            return None
        try:
            return int(raw)
        except ValueError:
            print("⚠️  Digite um número inteiro válido.")


# ----------------- operações HTTP -----------------

session = requests.Session()


def listar() -> None:
    print("\n== Listar personagens ==")
    universo = input("Filtrar por universo (ENTER para ignorar): ").strip() or None
    limit = read_int("Limit (ENTER=50): ", allow_empty=True) or 50
    offset = read_int("Offset (ENTER=0): ", allow_empty=True) or 0

    params = {"limit": limit, "offset": offset}
    if universo:
        params["universo"] = universo

    try:
        resp = session.get(f"{BASE_URL}/", params=params, timeout=TIMEOUT)
        print_resp(resp)
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão: {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")


def obter_por_id() -> None:
    print("\n== Obter por ID ==")
    pid = read_int("ID: ")
    try:
        resp = session.get(f"{BASE_URL}/{pid}", timeout=TIMEOUT)
        print_resp(resp)
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão: {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")


def criar() -> None:
    print("\n== Criar personagem ==")
    nome = read_nonempty("Nome: ")
    universo = read_nonempty("Universo: ")
    poder = read_nonempty("Poder principal: ")

    payload = {"nome": nome, "universo": universo, "poder_principal": poder}

    try:
        resp = session.post(f"{BASE_URL}/", json=payload, timeout=TIMEOUT)
        print_resp(resp)
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão: {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")


def atualizar() -> None:
    print("\n== Atualizar (PUT) ==")
    pid = read_int("ID: ")
    nome = read_nonempty("Nome: ")
    universo = read_nonempty("Universo: ")
    poder = read_nonempty("Poder principal: ")
    payload = {"nome": nome, "universo": universo, "poder_principal": poder}

    try:
        resp = session.put(f"{BASE_URL}/{pid}", json=payload, timeout=TIMEOUT)
        print_resp(resp)
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão: {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")


def remover() -> None:
    print("\n== Remover (DELETE) ==")
    pid = read_int("ID: ")
    confirma = input(f"Confirmar exclusão do ID {pid}? (s/N): ").strip().lower()
    if confirma != "s":
        print("Operação cancelada.")
        return
    try:
        resp = session.delete(f"{BASE_URL}/{pid}", timeout=TIMEOUT)
        print_resp(resp)
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Erro de conexão: {e}")
    except requests.exceptions.Timeout:
        print("⏳ Tempo de requisição esgotado.")


# ----------------- menu -----------------

def show_header() -> None:
    print("""
============================================
  Cliente da API — Personagens (Swagger)
============================================
Base URL: {base}
Comandos:
  1) Listar
  2) Obter por ID
  3) Criar
  4) Atualizar (PUT)
  5) Remover (DELETE)
  9) Alterar Base URL
  0) Sair
""".format(base=BASE_URL))

def alterar_base_url() -> None:
    global BASE_URL
    nova = input(f"Nova BASE_URL (atual: {BASE_URL}): ").strip()
    if nova:
        BASE_URL = nova.rstrip("/")  # evita barra dupla
        print(f"✅ BASE_URL alterada para: {BASE_URL}")
    else:
        print("(Mantida a URL atual)")

def main() -> None:
    # ping inicial (opcional)
    try:
        r = session.get(BASE_URL + "/", timeout=TIMEOUT)
        print(f"Conexão inicial: HTTP {r.status_code}")
    except Exception:
        print("(Aviso) Não foi possível contactar a API agora. Você ainda pode tentar pelas opções abaixo.")

    while True:
        show_header()
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            listar()
        elif op == "2":
            obter_por_id()
        elif op == "3":
            criar()
        elif op == "4":
            atualizar()
        elif op == "5":
            remover()
        elif op == "9":
            alterar_base_url()
        elif op == "0":
            print("Tchau! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\n(ENTER para continuar)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Até mais!")
        sys.exit(0)