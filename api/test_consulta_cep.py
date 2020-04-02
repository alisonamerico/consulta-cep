import responses
import pytest
import requests
from http import HTTPStatus


dados_do_endereco = {
    "cep": "50870-480",
    "logradouro": "Rua Jataúba",
    "complemento": "",
    "bairro": "Caçote",
    "localidade": "Recife",
    "uf": "PE",
    "unidade": "",
    "ibge": "2611606",
    "gia": "",
}


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "https://viacep.com.br/ws/50870480/json/",
            json=dados_do_endereco,
        )
        yield rsps


# def test_api_status_code() -> None:
#     assert mocked_responses == 200


# def test_api_status_code() -> None:
#     assert setup_responses.status_code == 200


# def test_cep(setup_responses):
#     assert setup_responses == "50870-480"


# def test_logradouro() -> None:
#     cep = 50870480
#     assert consulta_cep(cep)["logradouro"] == "Rua Jataúba"


# def test_bairro() -> None:
#     cep = 50870480
#     assert consulta_cep(cep)["bairro"] == "Caçote"


# def test_cidade() -> None:
#     cep = 50870480
#     assert consulta_cep(cep)["localidade"] == "Recife"


# def test_uf() -> None:
#     cep = 50870480
#     assert consulta_cep(cep)["uf"] == "PE"
