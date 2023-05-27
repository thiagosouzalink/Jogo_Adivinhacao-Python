"""

    Pacote de utilidades
    Autor: Thiago Souza

"""
from typing import IO


def ler_letra(txt):
    """
    Função que valida letra digitada pelo usuário.
    :param txt: Caracter digitado pelo usuário
    :return: Letra validada corretamente.
    """
    while True:
        letra = input(txt).strip()
        if not letra:
            print("Você não digitou nenhuma letra, tente novamente...")
            continue

        if not letra.isalpha():
            print("Você não digitou uma letra válida, tente novamente...")
            continue

        if len(letra) > 1:
            print("Entrada inválida, digite apenas uma letra")
            continue

        break
    return letra


def abrir_arquivo(file: str) -> IO:
    """Função que realiza processo de abertura de arquivo.

    Args:
        file (str): path arquivo a ser aberto.

    Returns:
        (IO): Objeto de arquivo de leitura.
    """

    try:
        arquivo = open(file, "r", encoding='UTF=8')

    except FileNotFoundError:
        print("Arquivo não existente, criando arquivo...")
        arquivo = open(file, 'wt+', encoding='UTF=8')
        return arquivo

    except:
        print("ERRO! O arquivo não pode ser aberto")

    else:
        return arquivo


def ler_arquivo(file: str) -> list:
    """
    Função que faz leitura de conteúdo de arquivo

    Args:
        file (str): path arquivo a ser aberto.
    
    Returns:
        (list): Dados com conteúdo do arquivo.
    """

    with abrir_arquivo(file) as arquivo:
        if arquivo:
            dados = []
            for linha in arquivo:
                dados.append(linha.strip())
            return dados


forca = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
 |   |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
 |   |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\\  |
 |   |
/ \\  |
     |
=========''']


