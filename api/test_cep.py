from api.conftest import mocked_responses
from http import HTTPStatus

from requests import Response

from api.consulta_cep import (
    consultaCEP,
    verifica_cep_valor_invalido,
    verifica_cep_chave_invalida,
)


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
    """assert consultaCEP(50870480)["localidade"] -> "Recife" """
    assert consultaCEP(50870480)["localidade"] == "Recife"


def test_uf(mocked_responses) -> None:
    """assert consultaCEP(50870480)["uf"] -> "PE" """
    assert consultaCEP(50870480)["uf"] == "PE"


def test_verifica_cep_valor_invalido() -> None:
    cep = 3456677
    assert (
        verifica_cep_valor_invalido(3456677)
        == f"""
        {cep} valor inválido!
        Dicas: 
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
        """
    )


def test_verifica_cep_chave_invalida() -> None:
    cep = 12345678
    assert (
        verifica_cep_chave_invalida(12345678)
        == f"""
        {cep} chave inválida!
        Dicas: 
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
        """
    )


"""
Validações:
possibilidades de input com erro...
1 - usuário digita menos que 8 digitos (inteiros)
2 - usuário digita mais que 8 digitos (inteiros)
3 - usuário digita 8 digitos (inteiros), poŕem não correponde a um cep válido.
4 - usuário digita letras, caracteres especiais(string).
"""
