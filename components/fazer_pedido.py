from components.listar_produtos import listar_produtos
from components.salvar_dados import salvar_dados
from datetime import datetime

def fazer_pedido(produtos, clientes, pedidos):
    if not produtos:
        print("Nenhum produto disponível para venda.")
        return
    
    tel = input("Telefone do cliente (ou ENTER se não for cadastrado): ")
    cliente_nome = "Não cadastrado"
    if tel:
        cliente = next((c for c in clientes if c['telefone'] == tel), None)
        if cliente:
            cliente_nome = cliente['nome']
        else:
            print("Cliente não encontrado.")
    
    carrinho = []
    total = 0
    while True:
        listar_produtos(produtos)
        cod = input("Digite o ID do produto (ou ENTER para finalizar): ")
        if cod == "":
            break
        produto = next((p for p in produtos if str(p['id']) == cod), None)
        if not produto:
            print("Produto não encontrado.")
            continue
        qtd = int(input("Quantidade: "))
        if qtd > produto['estoque']:
            print("Estoque insuficiente.")
            continue
        produto['estoque'] -= qtd
        valor = produto['preco'] * qtd
        total += valor
        carrinho.append({"produto": produto['nome'], "quantidade": qtd, "valor": valor})
    
    if not carrinho:
        print("Pedido vazio, cancelado.")
        return
    
    pedido = {
        "id": len(pedidos) + 1,
        "cliente": cliente_nome,
        "itens": carrinho,
        "total": total,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    pedidos.append(pedido)

    ARQ_PRODUTOS = "json/produtos.json"
    ARQ_PEDIDOS = "json/pedidos.json"

    salvar_dados(ARQ_PEDIDOS, pedidos)
    salvar_dados(ARQ_PRODUTOS, produtos)
    print("Pedido registrado com sucesso. 👨‍💻")