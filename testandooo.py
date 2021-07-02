class Animal(object):
    def fala(self):
        raise NotImplementedError("Erro")

class Pessoa(Animal):
    def fala(self):
        return "fala"

class Gato(Animal):
    pass

pessoa = Pessoa()
pessoa.fala()
gato = Gato()
gato.fala()