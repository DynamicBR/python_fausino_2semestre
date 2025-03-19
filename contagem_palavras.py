def contar_palavras(texto):
    guardar_texto = {
        "maisculo":  f"Texto totalmente em maiúsculo {texto.upper()}",
        "minusculo": f"Texto totalmente em minúsculo {texto.lower()}",
        "separacao": f"Separação do texto: {texto.split()}",
        "contagem": f"Contagem de letras {len(texto)}"
    }
    return guardar_texto
