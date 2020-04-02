from typing import Dict

import requests
from requests import Response


def consultaCEP(cep: int) -> Response:
    """Função que busca dados de um CEP informado.
    
    Arguments:
        cep {int} -- CEP informado.
    
    Returns:
        Response -- Retorna o dados do CEp.
    """
    consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados_do_endereco = consulta.json()
    return dados_do_endereco


# if __name__ == "__main__":
#     cep = int(input("Informe um CEP para consulta: "))

#     if len(str(cep).strip()) != 8:
#         print(f"{cep} inválido!")
#         print()
#         print("Dicas: ")
#         print("1. Certifique-se que CEP possua 8 dígitos.")
#         print("2. Sem letras ou caracteres especiais.")
#         exit()
#     else:
#         print(f"{consulta_cep(cep)}")
