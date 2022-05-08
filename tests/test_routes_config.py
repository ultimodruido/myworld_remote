from fastapi.testclient import TestClient
import json

from src import server

client = TestClient(server.app)


def test_remote_status():
    response = client.get("/remote_status")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {'entry_point': '/remote_status', 'result': True, 'data': {'port': '', 'status': False}}
    assert response_dict == expected_response


def test_register_remote():
    response = client.post("/register/remote/COM7")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {'entry_point': '/register/remote/COM7', 'result': False, 'data': {}}
    assert response_dict == expected_response


def test_register_train():
    response = client.post("/register/newtrain/funky_train/T")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/register/newtrain/funky_train/T", "result": True, "data": {}}
    assert response_dict == expected_response


def test_set_train_name():
    response = client.post("/register/train/0/name/bloomby")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/register/train/0/name/bloomby", "result": True, "data": {}}
    assert response_dict == expected_response


def test_set_train_name_wrong_input():
    response = client.post("/register/train/99/name/bloomby")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/register/train/99/name/bloomby",
                         "result": False,
                         "data": {"error": "Train not found"}
                         }
    assert response_dict == expected_response


def test_set_train_name_wrong_input2():
    response = client.post("/register/train/AA/name/bloomby")
    assert response.status_code == 422


def test_set_train_frequency():
    response = client.post("/register/train/0/frequency/P")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/register/train/0/frequency/P",
                         "result": True,
                         "data": {}
                         }
    assert response_dict == expected_response


def test_set_train_box():
    response = client.post("/register/train/0/box/11223")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/register/train/0/box/11223",
                         "result": True,
                         "data": {}
                         }
    assert response_dict == expected_response


def test_remove_train():
    response = client.post("/remove/train/0")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/remove/train/0",
                         "result": True,
                         "data": {}
                         }
    assert response_dict == expected_response


def test_remove_train_wrong_input():
    response = client.post("/remove/train/90")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/remove/train/90",
                         "result": False,
                         "data": {"error": "Train not found"}
                         }
    assert response_dict == expected_response


def test_remove_train_wrong_input2():
    response = client.post("/remove/train/xs")
    assert response.status_code == 422
