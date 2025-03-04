SALDO_LIMITE = 1000

carrinho = []

while (True):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    quantidade_produto = int(input("Digite a quantidade do produto: "))

    custo_total = preco_produto * quantidade_produto

    if (custo_total > SALDO_LIMITE):
        print("Saldo insuficiente! Você não pode adicionar este produto ao carrinho.")
    else:
        carrinho.append({
            "nome": nome_produto,
            "preco": preco_produto,
            "quantidade": quantidade_produto,
            "custo_total": custo_total
        })
        SALDO_LIMITE -= custo_total
        print(f"Produto adicionado ao carrinho! Saldo restante: R$ {SALDO_LIMITE:.2f}")

    continuar = input("Deseja adicionar mais itens? [S/N]: ").upper()
    if (continuar) != "S":
        break

print("\n=== Carrinho de Compras ===")
for item in carrinho:
    print(f"{item['quantidade']}x {item['nome']} - R$ {item['preco']:.2f} cada (Total: R$ {item['custo_total']:.2f})")

print(f"\nSaldo final da carteira: R$ {SALDO_LIMITE:.2f}")
