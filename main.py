import database
import time

class main:

    db = database.Database() # cria uma instância da classe Database para acessar os métodos de manipulação do banco de dados
    
    def __init__(self):
        while True:
            self.menu() # chama o método para exibir o menu de opções

    def menu(self):
        print("======================================")
        print("==============\033[1;36m FurStock \033[0m==============")
        print("========\033[1;36m Sistema de inventário! \033[0m======")
        print("======================================\n")

        print(" =======================")
        print("|\033[1;32mEscolha uma opção:     \033[0m|")
        print("|\033[1;32m1 - Adicionar produto  \033[0m|")
        print("|\033[1;32m2 - Listar produtos    \033[0m|")   
        print("|\033[1;32m3 - Atualizar produto  \033[0m|")
        print("|\033[1;32m4 - Deletar produto    \033[0m|")
        print("|\033[1;32m0 - Sair               \033[0m|")
        print(" =======================\n")

        opcao = int(input("Digite a opção desejada: ")) # lê a opção escolhida pelo usuário

        match opcao:
            case 1:
                self.adicionar_produto() # chama o método para adicionar um produto
            case 2:
                self.listar_Produtos() # chama o método para listar os produtos
            case 3:
                self.atualizar_produto() # chama o método para atualizar um produto
            case 4:
                self.deletar_produto() # chama o método para deletar um produto
            case 0:
                self.sair() # chama o método para sair do programa
            case _:
                print("Opção inválida!.\n\n")
                time.sleep(2)

    def menu_Atualizar(self):
       
       while True:
        print(" ========================")
        print("|\033[1;32mEscolha uma opção:      \033[0m|")
        print("|\033[1;32m1 - Atualizar nome      \033[0m|")
        print("|\033[1;32m2 - Atualizar quantidade\033[0m|")   
        print("|\033[1;32m3 - Atualizar preço     \033[0m|")
        print("|\033[1;32m0 - Voltar              \033[0m|")
        print(" ========================\n")

        opcao = int(input("Digite a opção desejada: ")) # lê a opção escolhida pelo usuário
        print("\n")

        match opcao:
            case 1:
                return 1 # retorna 1 para indicar que o nome do produto deve ser atualizado
            case 2:
                return 2 # retorna 2 para indicar que a quantidade do produto deve ser atualizada
            case 3:
                return 3 # retorna 3 para indicar que o preço do produto deve ser atualizado
            case 4:
                return 4 # retorna 4 para indicar que todos os campos do produto devem ser atualizados
            case 0:
                time.sleep(2)
            case _:
                print("Opção inválida!.\n\n")
                time.sleep(2)
                self.menu_Atualizar() # chama o método novamente para exibir o menu de opções de atualização


    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ") # lê o nome do produto
        quantidade = int(input("Digite a quantidade do produto: ")) # lê a quantidade do produto
        preco = float(input("Digite o preço do produto: ")) # lê o preço do produto
        self.db.adicionar_produto(nome, quantidade, preco) # chama o método para adicionar o produto no banco de dados
        print("Produto adicionado com sucesso!\n") # exibe uma mensagem de sucesso
        time.sleep(2) # espera 2 segundos antes de voltar ao menu

    def listar_Produtos(self):
        produtos = self.db.listar_produtos() # chama o método para listar os produtos do banco de dados
    
        print(" ================================================")
        print("|\033[1;32m  ID   |   Nome   |   Quantidade   |   Preço    \033[0m|")
        print(" ================================================")

        for produto in produtos: # percorre a lista de produtos e exibe cada um deles
            print(f"|\033[1;32m{produto[0]} | {produto[1]} - {produto[2]} - R${produto[3]:.2f} \033[0m")
            time.sleep(0.5) # espera 0.5 segundos antes de exibir o próximo produto
        print(" ===============================================\n")
        
        input("Pressione Enter para voltar ao menu...\n") # espera o usuário pressionar Enter para voltar ao menu
        time.sleep(2) # espera 2 segundos antes de voltar ao menu

    def atualizar_produto(self):

        opcao = self.menu_Atualizar() # chama o método para exibir o menu de opções de atualização e lê a opção escolhida pelo usuário

        id = int(input("Digite o ID do produto que deseja atualizar: ")) # lê o id do produto a ser atualizado

        if self.bd.atualizar_produto(0, id, None, None, None): # chama o método para verificar se o produto existe no banco de dados
            match opcao:
             case 1:
                    nome = input("Digite o novo nome: ") # lê o novo nome do produto
                    self.db.atualizar_produto(1, id, nome, None, None) # chama o método para atualizar o nome do produto
             case 2:
                    quantidade = int(input("Digite a nova quantidade: ")) # lê a nova quantidade do produto
                    self.db.atualizar_produto(2, id, None, quantidade, None) # chama o método para atualizar a quantidade do produto
             case 3:
                    preco = float(input("Digite o novo preço: ")) # lê o novo preço do produto
                    self.db.atualizar_produto(3, id, None, None, preco) # chama o método para atualizar o preço do produto
             case 4:
                    nome = input("Digite o novo nome: ") # lê o novo nome do produto
                    quantidade = int(input("Digite a nova quantidade: ")) # lê a nova quantidade do produto
                    preco = float(input("Digite o novo preço: ")) # lê o novo preço do produto
                    self.db.atualizar_produto(4, id, nome, quantidade, preco) # chama o método para atualizar todos os campos do produto
        
            print("Produto atualizado com sucesso!\n") 
            time.sleep(2)
        
        else:
            print("Produto não encontrado!\n")
            time.sleep(2)

    def deletar_produto(self):
        id = int(input("Digite o Id do produto que deseja deletar: ")) 
        verificacao = self.db.deletar_produto(id) # chama o método para deletar o produto no banco de dados

        if verificacao:
            print("Produto deletado com sucesso!\n")
        else:
            print("Produto não encontrado!\n")

        time.sleep(2)

    def sair(self):
        self.db.fechar_conexao() # chama o método para fechar a conexão com o banco de dados
        print("Saindo do programa...\n") 
        time.sleep(2) 
        exit() # encerra o programa

if __name__ == "__main__":
    main() # inicia o programa chamando a classe main