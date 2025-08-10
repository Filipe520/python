# Lista os pedidos do cliente
def listar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido registrado.")
    else:
        for p in pedidos:
            print(f"Pedido {p['id']} - Cliente: {p['cliente']} - Total: R${p['total']:.2f} - Data: {p['data']}")