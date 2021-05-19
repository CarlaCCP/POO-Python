class Produto:
    def __init__ (self, nome, descricao, preco):
        self.nome = nome #atributo, parametro
        self.descricao = descricao
        self.preco = preco #nao publico #um ponto de validacao, chama o setter
    
    
    #getter- retorna o valor do atributo nao publico
    @property
    def preco(self):
        return self.__preco
    
    #Serve quando existe uma regra de negocio
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError
        self.__preco = novo_preco
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not isinstance(nova_descricao, str):
            raise TypeError
        self.__descricao = nova_descricao

    def imprimir(self):
        print(f'\nProduto: {self.nome}\nDescricao: {self.descricao}\nPreço: R$ {self.preco}')

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual/100)
    

#Testando a classe produto
prod1 = Produto('mouse', 'sem fio', 80.90)
prod2 = Produto('teclado', 'slim', 155.99)
prod2.preco #chama  o property

try: #nao é necessario na atividade
    prod3 = Produto('Monitor', 'Curvo', 3000.0)
except:
    print('\n===Preço não pode ser nagativo')

prod3.aplicar_desconto(10)

prod1.imprimir()
print('-'*30)
prod2.imprimir()
prod2.descricao = "Teste"
print('-'*30)
prod3.imprimir()

#1 underline e dois underline deixao nao publico
#2 underline faz desfiguracao de nome
#prod2.preco seta um outro atributo nesse objeto se o preco for nao publico
#se o preco for __preco, bloqueio o acesso
#quando oculta nao pode setar