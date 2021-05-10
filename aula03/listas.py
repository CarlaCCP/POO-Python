# lista - mutaveis
# tuplas - imutaveis 

inteiros = [1,10,3, 20, 40, 80, 60]
compras =['Pao', 'Uva', 'Leite']
lista_vazia =[]

# Acessando
inteiros[1]
inteiros[-1] # ultimo elemento da lista
inteiros[1] = 30 # muda elemento
inteiros.insert(1, 20)
print(inteiros)

#remove
del inteiros[-1]
print(inteiros)

inteiros.pop # remove o ultimo
inteiros.pop(3)
inteiros.remove(30)
print(inteiros)

# Acrescentar
inteiros.append([100, 20, 50, 30])
print(inteiros)

# Concatenar duas listas
print(compras + inteiros)

# Tuplas
tupla = (1, 10, 3)
tupla_vazia = ()
tupla_de_um_item = (3,)
nao_eh_tupla = (5)

print(tupla[1])
print(tupla + tupla_de_um_item)

# Desempacotamente de Sequências
a , b = [1,2]
print("a: " , a , " b: ", b)

lista =[('a', 1), ('b', 2), ('c', 3)]
for item in lista:
    print(f'{item}')

for letra, numero in lista:
    print(f'{letra}: {numero}')

#Dicionarios
dicionario_vazio = {}
notas = {'Jack': 8.3, 'Anna': 9.0, 'Cris': 7.5}
print(notas.get('Jack'))

for chave in notas:
    print(chave, notas[chave])

print(list(notas.keys()))
print(list(notas.values()))
print(list(notas.items()))
