from http import HTTPStatus
import requests
from requests import Response


def consultaCEP(cep: int) -> Response:
    """Função que busca dados de um CEP informado.
    
    Arguments:
        cep {int} -- CEP informado.
    
    Returns:
        Response -- Retorna valores esperados para cada condição.
    """
    try:
        consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados_do_endereco = consulta.json()
        if not "erro" in dados_do_endereco:
            return dados_do_endereco
        else:
            return f"""{cep} possui um formato válido, porém inexistente!
                        Certifique-se que CEP que existe."""
    except ValueError:
        return f"""
        Valor digitado possui um formato inválido!
        Dicas:
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
    """


if __name__ == "__main__":

    while True:
        try:
            print()
            cep = int(input("Informe um CEP para consulta: "))
            if not "erro" in consultaCEP(cep):
                print(consultaCEP(cep))
                break
            else:
                print(
                    f"""
                    {cep} possui um formato válido, porém inexistente!
                    Certifique-se que CEP que existe.
                    """
                )
                print()
        except ValueError:
            print()
            print(
                f"""
                    Valor digitado possui um formato inválido!
                    Dicas:
                    1. Certifique-se que CEP possua 8 dígitos.
                    2. Sem letras ou caracteres especiais.
                    3. Certifique-se que CEP que existe.
                """
            )
            print()
