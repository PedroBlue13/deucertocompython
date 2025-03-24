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