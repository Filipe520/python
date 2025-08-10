from components.listar_produtos import listar_produtos
from components.cadastrar_produto import cadastrar_produto
from components.listar_clientes import listar_clientes
from components.cadastrar_clientes import cadastrar_cliente
from components.listar_pedidos import listar_pedidos
from components.fazer_pedido import fazer_pedido
from components.salvar_dados import carregar_dados

# App Coffee Shop Tia Rosa
def menu():
    # Arquivos JSON do app 
    ARQ_PRODUTOS = "json/produtos.json"
    ARQ_CLIENTES = "json/clientes.json"
    ARQ_PEDIDOS = "json/pedidos.json"
    
    # Laço infinito até finaliza o app
    while True:
        print("\n--- Coffee Shop Tia Rosa ---")
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Listar clientes")
        print("4 - Cadastrar cliente")
        print("5 - Listar pedidos")
        print("6 - Fazer pedido")
        print("0 - Sair")

        # Aqui vai carregar os dados JSON
        pedidos = carregar_dados(ARQ_PEDIDOS)
        produto = carregar_dados(ARQ_PRODUTOS)
        cadastrar = carregar_dados(ARQ_PRODUTOS)
        clientes = carregar_dados(ARQ_CLIENTES)
        clientes_cadastrados = carregar_dados(ARQ_CLIENTES)

        op = input("Escolha: ")
        
        if op == "1":
            listar_produtos(produtos=produto)
        elif op == "2":
            cadastrar_produto(produtos=cadastrar)
        elif op == "3":
            listar_clientes(clientes=clientes)
        elif op == "4":
            cadastrar_cliente(clientes_cadastrados)
        elif op == "5":
            listar_pedidos(pedidos=pedidos)
        elif op == "6":
            fazer_pedido(
                produtos=produto, 
                clientes=clientes, 
                pedidos=pedidos
            )
        elif op == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
