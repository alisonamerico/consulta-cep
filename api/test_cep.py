from api.conftest import mocked_responses
from http import HTTPStatus

from requests import Response

from api.consulta_cep import consultaCEP


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


def test_verifica_cep_formato_valido_porem_inexistente(
    mocked_responses_cep_formato_valido_porem_inexistente,
) -> None:
    cep = 12345678
    valor_esperado = f"""{cep} possui um formato válido, porém inexistente!
                        Certifique-se que CEP que existe."""
    assert consultaCEP(cep) == valor_esperado


def test_verifica_cep_formato_invalido(
    mocked_responses_verifica_cep_formato_invalido,
) -> None:
    cep = 3456
    valor_esperado = f"""
        Valor digitado possui um formato inválido!
        Dicas:
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
    """
    assert consultaCEP(cep) == valor_esperado


"""
Validações:
possibilidades de input com erro...
1 - usuário digita menos que 8 digitos (inteiros)
2 - usuário digita mais que 8 digitos (inteiros)
3 - usuário digita 8 digitos (inteiros), poŕem não correponde a um cep válido.
4 - usuário digita letras, caracteres especiais(string).
"""
