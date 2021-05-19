#Exemplo Herança
class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        pass

    def fugir(self, destino):
        pass

class PassaroAereo(Passaro):
    def voar (self):
        pass

class PassaroAquatico(Passaro):
    def nadar(self):
        pass

class PassaroCompanhia(PassaroAereo):
    def __init__(self, vida, ataque, defesa, companheiro): #sobreescreveu o init de passaro, recebendo somente os atributos
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)
        

class Pinguin(PassaroAquatico):
    def __init__(self, vida, ataque, defesa, peso):
        self.peso = peso
        super().__init__(vida, ataque, defesa)


p_ar = PassaroAereo(100, 300, 250)
p_agua = PassaroAquatico(140, 80, 400)
aguia = PassaroCompanhia(100, 300, 250, 'Carla')
pinguim = Pinguin(140, 80, 400, 5)
#Passaro.__init__(pinguim, 140, 300, 345) no lugar disso faça o super