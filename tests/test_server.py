from fastapi.testclient import TestClient

from src import server

client = TestClient(server.app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Maerklin MyWorld universal remote API"
