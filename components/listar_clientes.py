def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"{c['id']} - {c['nome']} | Tel: {c['telefone']} | Pontos: {c['pontos']}")