conjunto_moletom = {
            "preço": 100,
            "moletom": {
                "cor": "vermelho",
                "tipo": "canguru",
            },
            "calça": {
                "cor": "preto",
                "tipo": "jogger"
            }
        }
kit_periferico_gamer = {
    "preço": 300,
    "mouse": {
        "cor": "RGB",
        "tipo": "bluetooth"
    },
    "teclado": {
        "cor": "RGB",
        "tipo": "bluetooth",
        "switch": "red"
    },
    "headeset": {
        "cor": "RGB",
        "tipo": "bluetooth"
    }
}
material_escolar = {
    "preço": 500,
    "estojo": {
        "conteúdo": ["lápis grafite", "borracha", "caneta azul", "caneta preta"]
    },
    "caderno": {
        "tipo": "inteligente"
    }
}
livros_universitarios = {
    "preço": 150,
    "matemática": {
        "tipo": "superior"
    },
    "computação": {
        "tipo": "superior"
    },
    "scrum": {
        "tipo": "superior"
    }
}

global carrinho
carrinho = []

global preco_total
preco_total = []

menu = """"
=-=-Bem_vindo_à_Loja_de_Compras=-=
[1] Conjunto de Moletom
[2] Kit Periféricos Gamer
[3] Material Escolar
[4] Livros Universitários
[5] Sair
[6] Finalizar
--> """

while (True):
    opcao = input(menu)


    if (opcao == "5"):
        break

    elif (opcao == "1"):
        print(f"Esse é o conjunto de moletom: {conjunto_moletom}")
        escolha = str(input("Deseja adicionar ao carrinho? [S/N]: ")).upper()
        if (escolha == "S"):
            carrinho.append(conjunto_moletom)
            preco_total.append(conjunto_moletom["preço"])
        else:
            continue

    elif (opcao == "2"):
        print(f"Esse é o kit periférico gamer: {kit_periferico_gamer}")
        escolha = str(input("Deseja adicionar ao carrinho? [S/N]: ")).upper()
        if (escolha == "S"):
            carrinho.append(kit_periferico_gamer)
            preco_total.append(kit_periferico_gamer["preço"])
        else:
            continue

    elif (opcao == "3"):
        print(f"Esse é o material escolar: {material_escolar}")
        escolha = str(input("Deseja adicionar ao carrinho? [S/N]: ")).upper()
        if (escolha == "S"):
            carrinho.append(material_escolar)
            preco_total.append(material_escolar["preço"])
        else:
            continue

    elif (opcao == "4"):
        print(f"Esses são os livros universitários: {livros_universitarios}")
        escolha = str(input("Deseja adicionar ao carrinho? [S/N]: ")).upper()
        if (escolha == "S"):
            carrinho.append(livros_universitarios)
            preco_total.append(livros_universitarios["preço"])
        else:
            continue

    elif (opcao == "6"):
        valor = sum(preco_total)
        print(f"Compras solicitadas: {carrinho}, \nPreço total: {valor}")
