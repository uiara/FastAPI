import pytest
from fastapi.testclient import TestClient
from app.main import app  # Substitua pelo caminho correto para o seu app FastAPI

# Criando a fixture
@pytest.fixture
def client():
    # Instanciar o TestClient
    with TestClient(app) as client:
        yield client

def test_home_route(client):
    response = client.get("/")  
    assert response.status_code == 200 
    assert response.json() == {"msg": "Hello World"}

def test_create_user(client):
    user_data = {
        "name": "Bianka Uiara",
        "email": "bianka@uiara.com",
    }

    # Enviar a requisição POST
    response = client.post("/users/", json=user_data)

    # Verificar a resposta
    assert response.status_code == 200, f"Erro: {response.json()}"
    data = response.json()

    # Validar os dados retornados
    assert data["email"] == user_data["email"]
    assert "id" in data

