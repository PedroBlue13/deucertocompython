"""
3 - Josephus
Um grupo de homens foram capturados pelo exército inimigo, e foram obrigados a se posicionarem em círculo. Onde o primeiro homem deveria atirar no segundo, o terceiro no quarto o quinto no sexto e assim por diante, até que não sobre mais ninguém e uma única pessoa sobreviva.
Na imagem acima, apenas o homem 3 sobreviveu. Para que você tenha mais chance de sobreviver crie um programa que receba a quantidade de pessoas no círculo e retorno qual será a pessoa sobrevivente.
Entradas
Um número inteiro que indica a quantidade de pessoas no círculo.
Saída
Um número inteiro que indica o homem sobrevivente
Exemplo de entradas
10
13
5
Exemplo de saídas
5
11
3
"""


def josephus(n):
    pessoas = list(range(1, n + 1))
    indice = 1
    
    while len(pessoas) > 1:
        pessoas.pop(indice)
        indice = (indice + 1) % len(pessoas)
    
    return pessoas[0]

def main():
    n = int(input())
    sobrevivente = josephus(n)
    print(sobrevivente)

if __name__ == "__main__":
    main()