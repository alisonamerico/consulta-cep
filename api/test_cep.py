from http import HTTPStatus

import pytest
import requests
import responses

from api.consulta_cep import consultaCEP


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


def test_api_status_code(mocked_responses) -> None:
    """assert resp.status_code -> HTTPStatus.OK"""
    resp = requests.get("https://viacep.com.br/ws/50870480/json/")
    assert resp.status_code == HTTPStatus.OK


def test_cep(mocked_responses) -> None:
    """assert consultaCEP(50870480)["cep"] -> "50870-480" """
    assert consultaCEP(50870480)["cep"] == "50870-480"


def test_logradouro(mocked_responses) -> None:
    """assert consultaCEP(50870480)["logradouro"] -> "Rua Jataúba" """
    assert consultaCEP(50870480)["logradouro"] == "Rua Jataúba"


def test_bairro(mocked_responses) -> None:
    """assert consultaCEP(50870480)["bairro"] -> "Caçote" """
    assert consultaCEP(50870480)["bairro"] == "Caçote"


def test_cidade(mocked_responses) -> None:
    """assert consultaCEP(50870480)["localidade"] == "Recife" """
    assert consultaCEP(50870480)["localidade"] == "Recife"


def test_uf(mocked_responses) -> None:
    """assert consultaCEP(50870480)["uf"] == "PE" """
    assert consultaCEP(50870480)["uf"] == "PE"
