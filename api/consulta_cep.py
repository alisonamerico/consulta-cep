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


if __name__ == "__main__":
    print()
    cep = int(input("Informe um CEP para consulta: "))
    print()
    if len(str(cep).strip()) != 8:
        print(f"{cep} inválido!")
        print()
        print("Dicas: ")
        print("1. Certifique-se que CEP possua 8 dígitos.")
        print("2. Sem letras ou caracteres especiais.")
        exit()
    else:
        print(f"CEP: {consultaCEP(cep)['cep']}")
        print(f"Logradouro: {consultaCEP(cep)['logradouro']}")
        print(f"Complemento: {consultaCEP(cep)['complemento']}")
        print(f"Bairro: {consultaCEP(cep)['bairro']}")
        print(f"Localidade: {consultaCEP(cep)['localidade']}")
        print(f"UF: {consultaCEP(cep)['uf']}")
