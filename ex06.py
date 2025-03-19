alunos = [6, 7, 7, 5, 9]

def calcular_media():
    for notas in alunos:
        soma_notas = sum(alunos)

    media = soma_notas / 5
    return media

print(f"A média das notas dos alunos é {calcular_media()}")
