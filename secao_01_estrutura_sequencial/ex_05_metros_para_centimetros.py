"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 362.1 cm

"""


def metros_para_centimetros(metros):
    """Escreva aqui em baixo a sua solução"""
    centimetros = metros * 100 # Fórmula para calcular metros em cm; cm = X metros * 100 (1 metro = 100 cm) 
    return centimetros 

try:
    metros = float(input("Digite o valor em metros: ")) # interação o usuário informa um valor em metros 
    centimetros = metros_para_centimetros(metros) # converte para cm 
    print(f"{metros} metros equivalem a {centimetros} centímetros.") #exibe na tela o valor em cm 
except ValueError:
    print("Valor inválido. Certifique-se de digitar um número válido.") # Caso valor informado seja incorreto, uma letra ou caractere por exemplo retorna uma mensagem de erro 

    
