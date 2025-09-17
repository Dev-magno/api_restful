from fastapi import FastAPI, HTTPException
from models import UserInput
from starlette.responses import Response
from crud import create_user, list_users, get_user_by_id, update_user, delete_user

app = FastAPI()


# Rota para listar usuários
@app.get("/users/")
def get_users():
    result = list_users()

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# Rota para obter usuário por ID
@app.get("/users/{id}")
def get_user(id: int):
    result = get_user_by_id(id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# Rota para criar um novo usuário
@app.post("/users/", status_code=201)
def create_new_user(user: UserInput):
    result = create_user(user.nome, user.email)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


# Rota para atualizar um usuário por ID
@app.put("/users/{id}")
def update_existing_user(id: int, user: UserInput):
    result = update_user(id, user.nome, user.email)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# Rota para deletar um usuário por ID
@app.delete("/users/{id}")
def delete_existing_user(id: int):
    result = delete_user(id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return Response(status_code=204)
