def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


def eh_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True


lista = []
for i in range(2, 101):
    if eh_primo(i):
        lista.append(i)

print("Lista de primos até 100:", lista)
numero = int(input("Qual número você quer procurar? "))
resultado = pesquisa_binaria(lista, numero)

if resultado is not None:
    print(f"Número encontrado na posição: {resultado}")
else:
    print("Número não encontrado.")