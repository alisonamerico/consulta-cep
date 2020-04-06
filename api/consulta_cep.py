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


def verifica_cep_valor_invalido(cep: int) -> Response:
    try:
        return f"""
        CEP: {consultaCEP(cep)['cep']}
        Logradouro: {consultaCEP(cep)['logradouro']}
        Complemento: {consultaCEP(cep)['complemento']}
        Bairro: {consultaCEP(cep)['bairro']}
        Localidade: {consultaCEP(cep)['localidade']}
        UF: {consultaCEP(cep)['uf']}
        """

    except ValueError:
        return f"""
        {cep} valor inválido!
        Dicas: 
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
        """


def verifica_cep_chave_invalida(cep: int) -> Response:
    try:
        return f"""
        CEP: {consultaCEP(cep)['cep']}
        Logradouro: {consultaCEP(cep)['logradouro']}
        Complemento: {consultaCEP(cep)['complemento']}
        Bairro: {consultaCEP(cep)['bairro']}
        Localidade: {consultaCEP(cep)['localidade']}
        UF: {consultaCEP(cep)['uf']}
        """

    except KeyError:
        return f"""
        {cep} chave inválida!
        Dicas: 
        1. Certifique-se que CEP possua 8 dígitos.
        2. Sem letras ou caracteres especiais.
        3. Certifique-se que CEP que existe.
        """


if __name__ == "__main__":

    print()
    input_cep = input("Informe um CEP para consulta: ")
    print()
    try:
        cep = int(input_cep)
        print(f"CEP: {consultaCEP(cep)['cep']}")
        print(f"Logradouro: {consultaCEP(cep)['logradouro']}")
        print(f"Complemento: {consultaCEP(cep)['complemento']}")
        print(f"Bairro: {consultaCEP(cep)['bairro']}")
        print(f"Localidade: {consultaCEP(cep)['localidade']}")
        print(f"UF: {consultaCEP(cep)['uf']}")

    except ValueError:
        print(f"{input_cep} inválido!")
        print()
        print("Dicas: ")
        print("1. Certifique-se que CEP possua 8 dígitos.")
        print("2. Sem letras ou caracteres especiais.")
        print("3. Certifique-se que CEP que existe.")
        exit()

    except KeyError:
        print(f"{input_cep} inválido!")
        print()
        print("Dicas: ")
        print("1. Certifique-se que CEP possua 8 dígitos.")
        print("2. Sem letras ou caracteres especiais.")
        print("3. Certifique-se que CEP que existe.")
        exit()
