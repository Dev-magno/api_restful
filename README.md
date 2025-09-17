# 🚀 API RESTful com FastAPI + Supabase

Este projeto é uma API RESTful desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) e integrada ao [Supabase](https://supabase.com/) como backend de banco de dados. A API permite operações CRUD (Create, Read, Update, Delete) sobre usuários.

---

## 📦 Tecnologias Utilizadas

- **FastAPI** – Framework moderno e rápido para APIs com Python
- **Supabase** – Backend como serviço com PostgreSQL
- **Pydantic** – Validação de dados
- **Uvicorn** – Servidor ASGI para rodar a aplicação
- **dotenv** – Gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do Projeto
```
api_restful/
├── api.py             # Arquivo principal com as rotas da API
├── crud.py            # Funções de acesso ao banco Supabase
├── models.py          # Modelos Pydantic para validação
├── config.py          # Função para criar o cliente Supabase
├── .env               # Variáveis de ambiente (não versionar)
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```
https://github.com/Dev-magno/api_restful.git
```
### 2. Crie e ative o ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Configure o arquivo .env
Crie um arquivo .env com suas credenciais do Supabase:

```
SUPABASE_URL=https://xyzcompany.supabase.co
SUPABASE_KEY=your-anon-or-service-role-key
```

### 5. Execute a API

```
uvicorn api:app --reload
```
## 🔗 Endpoints da API

| Método  | Rota          | Descrição                  |
|---------|---------------|----------------------------|
| GET     | /users/       | Lista todos os usuários    |
| GET     | /users/{id}   | Busca usuário por ID       |
| POST    | /users/       | Cria novo usuário          |
| PUT     | /users/{id}   | Atualiza usuário por ID    |
| DELETE  | /users/{id}   | Deleta usuário por ID      |


# 📄 Exemplo de JSON para criação

```
{
  "nome": "Mariane Amaral",
  "email": "mariana@gmail.com"
}
```

# 🧪 Testes

http://localhost:8000/docs → Swagger UI

http://localhost:8000/redoc → Redoc

# 📌 Observações

- O campo id é gerado automaticamente pelo Supabase.

- O campo email é validado com EmailStr via Pydantic.

- A API retorna erros padronizados com HTTPException.

# 🛠️ Futuras melhorias

- Autenticação com JWT

- Paginação de resultados

- Validação de duplicidade de e-mail

- Deploy com Docker ou Railway