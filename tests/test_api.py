import requests
from pytest_voluptuous import S
from schemas import schemas
from schemas.schemas import base_url


def test_register_single_user():
    email = 'eve.holt@reqres.in'
    password = 'q1234'

    result = requests.post(
        url=f"{base_url}api/register",
        json={'email': email, 'password': password}
    )
    assert result.status_code == 200
    assert result.json() == S(schemas.register_single_user)
    assert len(result.json()['token']) == 17


def test_create_user():
    name = 'ololoshka'
    job = 'QA'

    result = requests.post(
        url=f"{base_url}api/users",
        json={'name': name, 'job': job}
    )

    assert result.status_code == 201
    assert result.json() == S(schemas.create_single_user)

    assert result.json()['name'] == name
    assert result.json()['job'] == job


def test_update_user():
    name = 'ololoshka'
    job = 'QA'

    result = requests.post(
        url=f"{base_url}api/users/2",
        json={'name': name, 'job': job}
    )
    name = 'ololoshka1'
    job = 'QA1'

    result = requests.put(
        url=f"{base_url}api/users/2",
        json={'name': name, 'job': job}
    )
    assert result.status_code == 200
    assert result.json() == S(schemas.update_single_user)
    assert result.json()['name'] == 'ololoshka1'
    assert result.json()['job'] == 'QA1'


def test_register_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    result = requests.post(
        url=f"{base_url}api/register",
        json={'email': email, 'password': password}
    )

    assert result.status_code == 200
    assert result.json()['id'] == 4
    assert result.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessful():
    result = requests.post(
        url=f"{base_url}api/register",
        json={"email": "sydney@fife"}
    )

    assert result.status_code == 400
    assert result.json()['error'] == 'Missing password'


def test_delete_user():
    result = requests.delete(url=f"{base_url}api/users/2")

    assert result.status_code == 204