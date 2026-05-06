import sqlite3

class Database:

    def __init__(self):
        self.banco = sqlite3.connect('inventario.db') # conecta ao banco de dados inventario.db, se ele não existir, ele será criado
        self.cursor = self.banco.cursor() # cria um cursor para executar comandos SQL
        self.criar_tabela() # chama o método para criar a tabela produtos

    def criar_tabela(self):
        
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    quantidade INTEGER NOT NULL,
                                    preco REAL NOT NULL)''') # cria a tabela produtos se ela não existir
            self.banco.commit() # salva as alterações no banco de dados
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")

    def adicionar_produto(self, nome, quantidade, preco):
        
        try:
            self.cursor.execute('''INSERT INTO produtos (nome, quantidade, preco) 
                                    VALUES (?, ?, ?)''', (nome, quantidade, preco)) # adiciona um produto na tabela
            self.banco.commit()
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")

    def listar_produtos(self):
        self.cursor.execute('SELECT * FROM produtos') # seleciona todos os produtos da tabela
        return self.cursor.fetchall() # retorna os produtos como uma lista de tuplas
    
    def atualizar_produto(self, opcao ,id, nome, quantidade, preco):

        match opcao: # verifica a opção escolhida pelo usuário para atualizar o produto
            case 1:
                try:
                    self.cursor.execute('''UPDATE produtos 
                                SET nome = ? 
                                WHERE id = ?''', (nome, id)) # somente o nome do produto é atualizado
                    self.banco.commit()
                except Exception as e:
                    print(f"Erro ao atualizar nome do produto: {e}")

            case 2:
                try:
                    self.cursor.execute('''UPDATE produtos 
                                SET quantidade = ? 
                                WHERE id = ?''', (quantidade, id)) # somente a quantidade do produto é atualizada
                    self.banco.commit()
                except Exception as e:
                    print(f"Erro ao atualizar quantidade do produto: {e}")

            case 3:
                try:
                    self.cursor.execute('''UPDATE produtos 
                                SET preco = ? 
                                WHERE id = ?''', (preco, id)) # somente o preço do produto é atualizado
                    self.banco.commit()
                except Exception as e:
                    print(f"Erro ao atualizar preço do produto: {e}")

            case 4:
                try:
                    self.cursor.execute('''UPDATE produtos 
                                SET nome = ?, quantidade = ?, preco = ? 
                                WHERE id = ?''', (nome, quantidade, preco, id)) # atualiza todos os campos do produto
                    self.banco.commit()
                except Exception as e:
                    print(f"Erro ao atualizar produto: {e}")

            case 0:
                try:
                    self.cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,)) # seleciona o produto com o id especificado
                    if self.cursor.fetchone() is None:
                        print("Produto não encontrado!")
                        return False
                except Exception as e:
                    print(f"Erro ao achar o produto: {e}")
                    return False

    def deletar_produto(self, id):  
        try:
            self.cursor.execute('DELETE FROM produtos WHERE id = ?', (id,)) # deleta um produto com base no id
            self.banco.commit()

            if self.cursor.rowcount == 0: # verifica se algum produto foi deletado
                return False
            else:
                return True
            
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")

    def fechar_conexao(self):
        self.banco.close() # fecha a conexão com o banco de dados

    