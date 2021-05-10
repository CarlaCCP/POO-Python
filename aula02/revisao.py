## Revisão python básico
print (type(3))
print(type("3"))

##String
texto  = ''' ola
loalala
laoalla '''
print(texto)
textos = "Olá mundo!\nescrito em\nvárias linhas"
print(textos)

##String formatadas
mensagem = f'2 + 3 = {2 + 3}, entendeu?'
print(mensagem)
salario = 3500.0
mensagem = f'20% a mais em R$ {salario} dará R$ {salario*1.2}'
print(mensagem)
##
pi = 3.14159265
print(f'{pi:f}') # sem especificar, o padrão é de 6 casas decimais
print(f'{pi:.3f}') # note o arredondamento na última casa decimal
print(f'{pi:7.3f}') # 7 colunas totais, 3 casas decimais
 
##Variaveis 
# O tipo de dados está relacionado
# ao valor atribuído e não a variavel que
#recebeu esse valor 
#Case- sensitive

#Funcoes
def soma_2 (x):
    return x + 2

print(soma_2(5))

# Debug 