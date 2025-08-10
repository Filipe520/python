# vai listar os produtos no terminal
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(f"{p['id']} - {p['nome']} | R${p['preco']:.2f} | Estoque: {p['estoque']}")