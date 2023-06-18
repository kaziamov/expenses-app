from fastapi.testclient import TestClient
from ..expenses_app.api import app

client = TestClient(app)


def test_create_item():
    data = {"name": "Ноутбук", "price": 1500.0}
    response = client.post("/api/v1/expenses/create", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Item created successfully"}
