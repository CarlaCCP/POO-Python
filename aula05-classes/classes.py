class Tv:
    def __init__(self, tela, resolucao, fabricante, preco): #inicializa o objeto
        self.tela = tela
        self.resolucao = resolucao
        self.fabricante = fabricante
        self.__preco = preco
        self.fotos = []
        self.descricao = f'TV {resolucao} {tela}" - {fabricante}'

    def atualizar_preco(self,novo_preco):
        self.preco = novo_preco
    
    def aplicar_desconto(self, desconto):
        precoAntigo = self._Tv__preco
        descontoPreco = (precoAntigo * (desconto /100))
        precoNovo = precoAntigo - descontoPreco
        self.preco = precoNovo
   

tv_1 = Tv(43, 'FullHD', 'Samsung', 2400) #cria o objeto
tv_2 = Tv(50, '4k', 'LG', 3200)
print(f'Preço antigo: R$ {tv_1._Tv__preco:.2f}')
tv_1.atualizar_preco(2160)
tv_1.aplicar_desconto(10)
print(f'Preço novo: R$ {tv_1._Tv__preco:.2f}')

