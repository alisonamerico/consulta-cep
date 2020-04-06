from http import HTTPStatus

import pytest
import requests
import responses
from json import load, loads

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
    """Função que irá simular(mokar) o retorno do requests.
    
    Yields:
        [type] -- Retorna dados simulados pelo responses.
    """
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "https://viacep.com.br/ws/50870480/json/",
            json=dados_do_endereco,
        )
        resp = requests.get("https://viacep.com.br/ws/50870480/json/")
        assert resp.status_code == HTTPStatus.OK

        yield rsps
    # outside the context manager requests will hit the remote server
    resp = requests.get("https://viacep.com.br/ws/50870480/json/")
    resp.status_code == HTTPStatus.NOT_FOUND


# @pytest.fixture
# def mocked_responses_failed():
#     """Função que irá simular(mokar) o retorno do requests.

#     Yields:
#         [type] -- Retorna dados simulados pelo responses.
#     """
#     with responses.RequestsMock() as rsps:
#         rsps.add(
#             responses.GET, "https://viacep.com.br/ws/12345678/json/", json=um_erro,
#         )
#         resp = requests.get("https://viacep.com.br/ws/50870480/json/")
#         assert resp.status_code == HTTPStatus.OK

#         yield rsps
#     # outside the context manager requests will hit the remote server
#     resp = requests.get("https://viacep.com.br/ws/50870480/json/")
#     resp.status_code == HTTPStatus.NOT_FOUND
