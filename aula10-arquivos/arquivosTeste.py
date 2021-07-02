##Escrita
f = open('teste.txt', 'w')
f.write('Olá Mundo!\n Estouy testando algumas linhas\nVamos ver se dá certo')
f.close()

## Escrita
with open('teste2.txt', 'w') as f:
    f.write('Olá novamente!\n')
    print(f'(dentro do bloco with) arquivo fechado? {f.closed}')
 
print(f'(fora do bloco with) arquivo fechado? {f.closed}')

## Leitura
with open('teste.txt', 'r') as f:
    print(f.tell())  # exibe a posição atual
    f.seek(5)        # move a posição atual para o índice 5
    print(f.tell())  # exibe a posição atual

with open('teste.txt', 'r') as f:
    texto = f.read()
    print(texto)
# código que utiliza a variável texto após o bloco with

with open('teste.txt', 'r') as f:
    linha1 = f.readline()
    linha2 = f.readline()
    linha3 = f.readline()
    print(linha1,linha2, linha3)
 
# código que utiliza as variáveis após o bloco with

# Iterando sobre um arquivo diretamente
with open('teste.txt', 'r') as f:
    for linha in f:
        print(linha)
#Ler duas vezes o msm arquivo resulta em string vazia
#use o seek para voltar o marcador para zero
with open('teste.txt', 'r') as f:
    leitura1 = f.read()  # irá conter os dados do arquivo
    #f.seek(0)
    leitura2 = f.read()  # será uma string vazia
    print(f'string vazia: {leitura2}')

#  Escrita
texto = 'escrevendo a primeira frase'
with open('teste.txt', 'w') as f:
    f.write(texto)
    print(f)

s = ['linha 1', 'linha 2', 'linha 3', 'linha 4']
with open('teste.txt', 'a') as f:
    f.writelines(s)
    print(f)

#Para adicionar quebras de linhas
texto2 = texto + '\n'
s2 = [f'{linha}\n' for linha in s]  # list comprehension
with open('teste2.txt', 'w') as f:
    f.write(texto2)
    f.writelines(s2)

#Usando print
texto = 'escrevendo a primeira frase'
s = ['linha 1', 'linha 2', 'linha 3', 'linha 4']
with open('print.txt', 'w') as f:
    print(texto, file=f)
    for linha in s:
        print(linha, file=f)


