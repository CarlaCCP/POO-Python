class Cliente:
    def __init__(self,nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        arroba = '@'
        if(type(novo_email) != str):
            raise TypeError
        if(novo_email.count(arroba) != 1):
            raise ValueError
        else:
            self.__email = novo_email
    
    @telefone.setter
    def telefone(self, novo_telefone):
        caracteres_permitidos = [' ', '-', '(', ')']
        if(type (novo_telefone) != str):
            raise TypeError
        apenas_numeros = ''
        for caractere in novo_telefone: 
            if caractere not in caracteres_permitidos:
                apenas_numeros += caractere
        if(not apenas_numeros.isdigit()):
            raise ValueError
        else:
            self.__telefone = novo_telefone  
       
class Conta():
    def __init__(self,Cliente, numero, saldo ):
        self.__clientes = [Cliente]
        self.__numero = numero
        self.__saldo = saldo
        self.__historico = []

    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo


    def sacar(self, valor):
        if len(self.__historico) == 0:
            self.__historico.append(('saldo inicial', self.__saldo))
        if(valor > self.__saldo):
            raise ValueError
        self.__saldo = self.__saldo - valor
        self.__historico.append(("saque", valor))
    
    def depositar(self, deposito):
        if len(self.__historico) == 0:
            self.__historico.append(('saldo inicial', self.__saldo))
        self.__saldo = self.__saldo + deposito
        self.__historico.append(("deposito", deposito))
    
   
    def tirar_extrato(self):
        if len(self.__historico) == 0:
            self.__historico.append(('saldo inicial', self.__saldo))
        return self.__historico 




class Banco:
    def __init__ (self, nome):
        self.__nome = nome
        self.__clientes = [Cliente]
        self.__contas = []
        self.__cont = 0 
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def contas(self):
        return self.__contas
    
    def abrir_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError 
        else:
            
            self.__cont = len(self.__contas) + 1 #conta certo
            self.__contas.append(Conta([clientes],self.__cont, saldo_inicial))

    
