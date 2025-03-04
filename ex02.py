contador = 0
frase = str(input("Digite uma frase: "))
palavras = frase.split()

for palavra in palavras:
    if palavra.startswith("a"):
        contador += 1

print(f"A quantidade de palavras que começa com a letra a é {contador}")
