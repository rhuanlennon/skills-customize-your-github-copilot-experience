from fastapi.testclient import TestClient
from starter_code import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API da Biblioteca!"}

def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# TODO: Adicionar mais testes para os outros endpoints
# test_create_book()
# test_get_book()
# test_update_book()
# test_delete_book()