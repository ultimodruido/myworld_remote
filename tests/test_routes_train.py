from fastapi.testclient import TestClient
import json

from src import server

client = TestClient(server.app)


def test_train_list():
    # test empty list
    response = client.get("/train_list")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train_list", "result": True, "data": {"train_list": []}}
    assert response_dict == expected_response
    # add a random train
    client.post("/register/newtrain/funky_train/T")
    # test once more
    response = client.get("/train_list")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train_list",
                         "result": True,
                         "data": {
                             "train_list": [{
                                 "name": "funky_train",
                                 "frequency": "T",
                                 "box": ""
                             }]
                         }
                         }
    assert response_dict == expected_response


def test_set_train_speed():
    # add a random train first
    client.post("/register/newtrain/funky_train/T")
    response = client.post("/train/0/speed/F1")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train/0/speed/F1", "result": True, "data": {}}
    assert response_dict == expected_response


def test_toggle_train_light():
    # add a random train
    client.post("/register/newtrain/funky_train/T")
    response = client.post("/train/0/light")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train/0/light", "result": True, "data": {}}
    assert response_dict == expected_response


def test_blow_train_horn():
    # add a random train
    client.post("/register/newtrain/funky_train/T")
    response = client.post("/train/0/horn")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train/0/horn", "result": True, "data": {}}
    assert response_dict == expected_response


def test_train_sound():
    # add a random train
    client.post("/register/newtrain/funky_train/T")
    response = client.post("/train/0/sound1")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train/0/sound1", "result": True, "data": {}}
    assert response_dict == expected_response
    response = client.post("/train/0/sound2")
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    expected_response = {"entry_point": "/train/0/sound2", "result": True, "data": {}}
    assert response_dict == expected_response
