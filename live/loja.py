from produto import Produto

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self._produtos =[]

    @property
    def produtos(self):
        return self._produtos
    
    def inserir_produto(self, produto):
        self._produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self._produtos:
            produto.imprimir()

lojinha = Loja("YellowSub")
lojinha.inserir_produto(Produto('mouse', 'sem fio', 80.90))
lojinha.inserir_produto(Produto('Carteira', 'sem fio', 80.90))
lojinha.inserir_produto(Produto('teclado', 'sem fio', 80.90))
print(f'========== Lojinha {lojinha.nome}\n')
lojinha.listar_produtos()
