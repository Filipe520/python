from components.salvar_dados import salvar_dados

# Vai cadastrar os produtos da loja
def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    
    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    produtos.append(produto)

    ARQ_PRODUTOS = "json/produtos.json"
    salvar_dados(ARQ_PRODUTOS, produtos)
    print("Produto cadastrado com sucesso ✅")