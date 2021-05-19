from datetime import date
#atributos publicos
class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome #atributo e parametro
        self.sexo = sexo
        self.idade = idade
    
    def imprimir(self):
        print(self.nome)
    
    def calcular_nascimento(self, ano_atual):
        return ano_atual - self.idade

#Recebe uma instancia de pessoa
p1 = Pessoa('Maria', 'Feminino', 21)
p1.imprimir()
ano = date.today().year
print(f'{p1.nome} nasceu no ano {p1.calcular_nascimento(ano)}')

#Exercicio1
