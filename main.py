from random import choice
from time import sleep
import sys

from unidecode import unidecode

from utils import ler_arquivo, ler_letra, forca


print(f"{'#'*20} BEM VINDO AO JOGO DA ADIVINHAÇÃO {'#'*20}")
# Obtêm arquivo com as profissões
profissoes = ler_arquivo("profissoes.txt")
if not profissoes:
    print("Erro ao carregar as profissões...")
    sys.exit(1)

profissao = choice(profissoes) # Sorteia uma profissão
# profissao = unidecode.unidecode(profissao_original).lower()

letras_digitadas = []  # Lista com as letras digitadas
letras_acertadas = [" "]  # Lista com as letras acertadas
chances = 7  # Número de chances

# Laço com execução do programa
while True:
    # Atualiza o estado da oalavra secreta
    secreto_temporario = ''
    for letra_secreta in profissao:
        if unidecode(letra_secreta.lower()) in letras_acertadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    # Verifica se o usuário acertou a palavra secreta.
    if secreto_temporario == profissao:
        sleep(1)
        print("\nParabéns! Você acertou!")
        print(f'A palavra secreta era "{profissao}".')
        break
    else:
        sleep(1)
        print(forca[chances])
        print(f"Palavra secreta: {secreto_temporario}\n")

    print(f"Você ainda tem {chances} chance(s).")
    letra = ler_letra("Digite uma letra: ").lower()

    # verifica se a leta já foi digitada
    if letra in letras_digitadas:
        print("\nEsta letra já foi digitada, tente outra...\n")
        sleep(1.5)
        continue

    letras_digitadas.append(letra)

    # Verifica se a letra está presente na palavra secreta
    if letra in unidecode(profissao.lower()):
        print(f'\nA letra "{letra}" está presente na palavra secreta.\n')
        letras_acertadas.append(letra)
    else:
        print(f'\nA letra "{letra}" não está presente na palavra secreta.\n')
        chances -= 1
        if chances == 0:
            sleep(1)
            print(forca[chances])
            print("\nVocê perdeu!")
            print(f'A palavra secreta era "{profissao}".')
            break

    sleep(1)



