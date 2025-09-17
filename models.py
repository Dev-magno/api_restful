from pydantic import BaseModel, EmailStr


class UserInput(BaseModel):
    nome: str
    email: EmailStr
