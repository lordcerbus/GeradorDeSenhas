# gerador de senha tem que gera letra maiuscula, simbolo, numero e letra minuscula
import random
import string
letramai = string.ascii_uppercase
letramin = string.ascii_lowercase
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
especiais = ['!', '@', '#', '$', '%', '&', '*', '?']
todososcaracteres = ''
todososcaracteres += ''.join(letramai)
todososcaracteres += ''.join(letramin)
todososcaracteres += ''.join(numeros)
todososcaracteres += ''.join(especiais)
contador = 0


def removeduplicatas(senha):
    senhasemduplicatas = []
    for caractere in senha:
        if caractere not in senhasemduplicatas:
            senhasemduplicatas.append(caractere)
    senhasemduplicatas.sort()
    return senhasemduplicatas


def geradordesenhas():
    senha = ''
    if len(senha) == 0:
        senha += ''.join(random.choice(todososcaracteres) for _ in range(8))
        senha = ''.join(removeduplicatas(senha))

        while len(senha) < 8:
            senha += ''.join(random.choice(todososcaracteres))
            senha = ''.join(removeduplicatas(senha))

    print(senha)


geradordesenhas()
