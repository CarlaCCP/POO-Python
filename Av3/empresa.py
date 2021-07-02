# Programação Orientada a Objetos
# AC03 - Herança e polimorfismo
#
# Email Impacta: carla.paula@aluno.faculdadeimpacta.com.br

class Pessoa:
    def __init__(self, nome, idade):
        self.validaConstrutor(nome, idade)
        self.__nome = nome
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    def validaConstrutor(self,nome, idade):
        if type(nome) != str:
            raise TypeError
        if (nome == ""):
            raise ValueError
        if type(idade) != int:
            raise TypeError
        if (idade < 0):
            raise ValueError
        
    def aniversario(self):
        self.__idade += 1 

class Funcionario(Pessoa):
    def __init__ (self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade)
        self.email = email
        self.carga_horaria = carga_horaria
        self.horaTrabalho
    

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

    @property
    def carga_horaria(self):
        """
        Retorna a carga horária semanal de trabalho do funcionário.

        (não implementar aqui)
        """
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        """
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno.

        (não implementar aqui)
        """
        raise NotImplementedError

    def calcula_salario(self):
        """
        Calcula e retorna o salário do mês para o funcionário.

        (não implementar aqui)
        """
        raise NotImplementedError

    
    def aumenta_salario(self):
        self.horaTrabalho = (self.horaTrabalho * 0.05) + self.horaTrabalho
               
class Programador(Funcionario):
    def __init__ (self, nome, idade, email, carga_horaria):
       self.horaTrabalho = 35.0
       super().__init__(nome, idade, email, carga_horaria)
       self.carga_horaria = carga_horaria
       
    
    @property
    def carga_horaria(self):
       return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if(nova_carga_horaria < 20 or nova_carga_horaria > 40):
            raise ValueError
        else:
            self.__carga_horaria = nova_carga_horaria
    
    def calcula_salario(self):
        salario = (self.horaTrabalho * self.carga_horaria * 4.5)
        return salario

    
    def aumenta_salario(self):
        return super().aumenta_salario()

class Estagiario(Funcionario):
    def __init__ (self, nome, idade, email, carga_horaria):
       self.horaTrabalho = 15.50
       self.__auxilio = 250.0
       super().__init__(nome, idade, email, carga_horaria)
       self.carga_horaria = carga_horaria
       
    @property
    def carga_horaria(self):
       return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if(nova_carga_horaria < 16 or nova_carga_horaria > 30):
            raise ValueError
        else:
            self.__carga_horaria = nova_carga_horaria
    
    
    def calcula_salario(self):
        salario = ((self.horaTrabalho * self.carga_horaria * 4.5) + self.__auxilio) 
        return salario
    
    def aumenta_salario(self):
        return super().aumenta_salario()

class Vendedor(Funcionario):
    def __init__ (self, nome, idade, email, carga_horaria):
       self.horaTrabalho = 30.00
       super().__init__(nome, idade, email, carga_horaria)
       self.carga_horaria = carga_horaria
       
       self.__auxilio = 350.00
       self.__porVisitas = 30.00
       self.__auxilioTransporte = 30.00
       self.__visitas = 0
    
    @property
    def visitas(self):
        return self.__visitas

    @property
    def carga_horaria(self):
       return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if(nova_carga_horaria < 15 or nova_carga_horaria > 45):
            raise ValueError("Carga horaria errada")
        else:
            self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        
        valeTransporte = self.__auxilioTransporte * self.__visitas

        salario = ((self.horaTrabalho * self.carga_horaria * 4.5) 
        + self.__auxilio  + valeTransporte) 
        
        return salario
    
    def aumenta_salario(self):
        return super().aumenta_salario()
    
    def realizar_visita(self, n_visitas):
        if(type(n_visitas) == int):
            if(n_visitas <= 10 or n_visitas >= 0):
                self.__visitas = self.__visitas + n_visitas
        if(type(n_visitas) != int):
            raise TypeError
        if(n_visitas < 0 or n_visitas >10):
            raise ValueError
    
    def zerar_visitas(self):
        self.__visitas = 0
    
class EmpresaCreationError(Exception):
    """ Classe de erro personalizada, não editar"""
    pass

class Empresa:
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        self.valida_atributos(nome, cnpj,area_atuacao,equipe)
        
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.__equipe = equipe
    
    def valida_atributos(self, nome, cnpj, area_atuacao, equipe):
        if(type(nome) != str or type(cnpj) != str or type(area_atuacao) != str):
            raise EmpresaCreationError
        for i in equipe:
            if(not isinstance(i, Funcionario)):
                raise EmpresaCreationError
        
    
    @property
    def equipe(self):
        return self.__equipe
    
    #Sem retorno
    def contrata(self, novo_funcionario):
        
        if(not isinstance(novo_funcionario, Funcionario)):
            raise TypeError
        self.equipe.append(novo_funcionario)
    
    def folha_pagamento(self):
        contaSalario = 0
        for teste in self.__equipe:
           contaSalario = teste.calcula_salario() + contaSalario
        return contaSalario
    
    
    def dissidio_anual(self):
        for teste in self.__equipe:
            teste.aumenta_salario()

    def listar_visitas(self):
        dicionario = {}
        for i in self.equipe:
            if(isinstance(i, Vendedor)):
                dicionario[i.email] = i.visitas
        return dicionario

    def zerar_visitas_vendedores(self):
        for i in self.equipe:
            if(isinstance(i, Vendedor)):
                i.zerar_visitas()

programador = Programador("Carla Cristina", 24, "carla@carla", 40)
estagiario = Estagiario("Estag", 25, "estag@estag", 30)
vendedor = Vendedor("Vendedor", 24, "ven@ven", 40)
vendedor1 = Vendedor("Vendedor", 24, "ven1@ven", 40)
vendedor2 = Vendedor("Vendedor", 24, "ven2@ven", 40)
vendedor.realizar_visita(5)
vendedor.realizar_visita(5)
vendedor1.realizar_visita(5)
vendedor2.realizar_visita(5)
empresa = Empresa("Zup", "74635", "Consultoria", [programador, estagiario, vendedor, vendedor1, vendedor2])
print(len(empresa.equipe))
print(empresa.listar_visitas())
empresa.zerar_visitas_vendedores()
print(empresa.listar_visitas())
print(vendedor1.visitas)