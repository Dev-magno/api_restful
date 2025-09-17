import os
from dotenv import load_dotenv
from config import create_client

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera a URL e a chave do Supabase do arquivo .env
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Criar o cliente e os argumento corretos
client = create_client(url, key)


# Lista todos os usuários
def list_users():
    response = client.table("users").select("*").execute()

    if not response.data:
        return {"error": "Nenhum usuário encontrado."}
    return response.data


# Lista usuário por ID
def get_user_by_id(id):
    response = client.table("users").select(
        "id, nome, email").eq("id", id).execute()

    if not response.data:
        return {"error": "Usuário não encontrado."}
    return response.data[0]


# Insere usuários no banco
def create_user(nome, email):
    if not nome.strip() or not email.strip():
        return {"error": "Nome e email são obrigatórios."}

    data = {"nome": nome, "email": email}
    response = client.table("users").insert(data).execute()

    if not response.data:
        return {"error": "Erro ao criar usuário"}
    return response.data[0]


# Atualiza usuário por id
def update_user(id, nome, email):
    response = client.table("users").update(
        {"nome": nome, "email": email}).eq("id", id).execute()

    if not response.data:
        return {"error": "Usuário não encontrado."}
    return response.data[0]


# Deleta usuário por ID
def delete_user(id):
    response = client.table("users").delete().eq("id", id).execute()

    if not response.data:
        return {"error": "Usuário não encontrado."}
    return response.data[0]
