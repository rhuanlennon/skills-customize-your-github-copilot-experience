from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Modelo Pydantic para validação de dados
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., gt=0, le=datetime.now().year)
    isbn: str = Field(..., min_length=10, max_length=13)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "O Senhor dos Anéis",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "isbn": "9788533615540"
            }
        }

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="Biblioteca API",
    description="API REST para gerenciar uma biblioteca de livros",
    version="1.0.0"
)

# Simula um banco de dados em memória
books_db = {}

@app.get("/")
async def read_root():
    """Endpoint raiz - retorna mensagem de boas vindas"""
    return {"message": "Bem-vindo à API da Biblioteca!"}

# TODO: Implementar endpoints CRUD aqui:
# GET /books - listar todos
# GET /books/{id} - obter um livro
# POST /books - criar novo livro
# PUT /books/{id} - atualizar livro
# DELETE /books/{id} - remover livro

# Exemplo de endpoint implementado:
@app.get("/books", response_model=List[Book])
async def list_books():
    """Lista todos os livros cadastrados"""
    return list(books_db.values())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)