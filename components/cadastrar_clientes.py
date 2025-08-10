from components.salvar_dados import salvar_dados

# Vai cadastrar um novo cliente no json - clientes.json
def cadastrar_cliente(clientes):
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "telefone": telefone,
        "pontos": 0
    }

    ARQ_CLIENTES = "json/clientes.json"

    clientes.append(cliente)
    salvar_dados(ARQ_CLIENTES, clientes)
    print("Cliente cadastrado com sucesso. 👉🤖")