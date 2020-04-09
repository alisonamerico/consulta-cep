from http import HTTPStatus

import pytest
import requests
import responses
import json

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

cep_formato_valido_porem_inexistente = {"erro": True}


verifica_cep_formato_invalido = f"""
        Valor digitado possui um formato inválido!
        Dicas:
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
    """


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
    resp.status_code == HTTPStatus.OK


@pytest.fixture
def mocked_responses_cep_formato_valido_porem_inexistente():
    """Função que irá simular(mokar) o retorno do requests.

    Yields:
        [type] -- Retorna dados simulados pelo responses.
    """
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "https://viacep.com.br/ws/12345678/json/",
            json=cep_formato_valido_porem_inexistente,
        )
        resp = requests.get("https://viacep.com.br/ws/12345678/json/")
        assert resp.status_code == HTTPStatus.OK

        yield rsps
    # outside the context manager requests will hit the remote server
    resp = requests.get("https://viacep.com.br/ws/12345678/json/")
    resp.status_code == HTTPStatus.OK


@pytest.fixture
def mocked_responses_verifica_cep_formato_invalido():
    """Função que irá simular(mokar) o retorno do requests.

    Yields:
        [type] -- Retorna dados simulados pelo responses.
    """
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "https://viacep.com.br/ws/3456/json/",
            json=verifica_cep_formato_invalido,
        )
        resp = requests.get("https://viacep.com.br/ws/3456/json/")
        assert resp.status_code == HTTPStatus.OK
        yield rsps
    # outside the context manager requests will hit the remote server
    resp = requests.get("https://viacep.com.br/ws/3456/json/")
    resp.status_code == HTTPStatus.BAD_REQUEST
