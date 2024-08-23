1
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Venda:
    def __init__(self):
        self.produtos_vendidos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos_vendidos.append((produto, quantidade))

    def calcular_total(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self.produtos_vendidos)
        return total

    def exibir_relatorio(self):
        print("\n--- Relatório de Vendas ---")
        for produto, quantidade in self.produtos_vendidos:
            print(f"{produto.nome} - Quantidade: {quantidade}, Total: R${produto.preco * quantidade:.2f}")
        print(f"\nValor total recebido: R${self.calcular_total():.2f}")

# Função principal para rodar o sistema
def sistema_vendas():
    venda = Venda()

    while True:
        print("\n1. Adicionar produto vendido")
        print("2. Exibir relatório de vendas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço do produto: R$"))
            quantidade_produto = int(input("Quantidade vendida: "))

            produto = Produto(nome_produto, preco_produto)
            venda.adicionar_produto(produto, quantidade_produto)

        elif opcao == '2':
            venda.exibir_relatorio()

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema
sistema_vendas()