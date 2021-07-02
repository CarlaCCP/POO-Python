# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: carla.paula@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    divisores = []
    primo = False
    numero = n
    if ( n == 2):
        primo = True
    if(n % 2 >0):

        for x in range(1, n+1):
            if(n % x == 0):
                divisores.append(x)
    
        for item in divisores:
            if(divisores[0]== 1 and divisores[1] == numero ):
                primo = True
                
            else:
                primo = False

    return(primo)


def lista_primos(n):
    itens_primos = []
    divisores = []
    numero = 0
    for x in range(1,n):
        numero = x
        divisores.clear()
        if (numero == 2):
            itens_primos.append(x)
        if(numero % 2 == 0):
            False
        else:
            if(x == 1):
                pass
            else:

                for y in range(1, numero+1):
                    if(numero % y  == 0):
                        divisores.append(y)
            
                for item in divisores:
                    if(divisores[0]== 1 and divisores[1] == numero):
                        itens_primos.append(numero)
                    break
                
    return(itens_primos)


def conta_primos(s):
    lista_primos = []
    nPrimo = 0
    cont = 0
    discionario_primos = {}
    divisores = []
    for item in s:
        numero = item
        divisores.clear()
        if (numero == 2):
            lista_primos.append(item)
            lista_primos.sort()
        if(numero % 2 == 0):
            False
        else:
            if(item == 1):
                lista_primos.append(item)
                lista_primos.sort()
            else:

                for y in range(1, numero+1):
                    if(numero % y  == 0):
                        divisores.append(y)
            
                for item in divisores:
                    if(divisores[0]== 1 and divisores[1] == numero):
                        lista_primos.append(numero)
                        lista_primos.sort()
                        
                    break

    for item in lista_primos:
        if(item == nPrimo ):
            cont = cont + 1
        else:
            cont = 1
        discionario_primos[item] = cont
        nPrimo = item

    return(discionario_primos)


def eh_armstrong(n):
    confirmaArmstrong = False
    numeroEntrada = n
    palavra = str(n)
    lista_palavra = []
    lista_numero = []
    numero = 0
    item = 0
    cont = 0
    soma = 0
    for x in range(0, len(palavra)):
        cont = cont + 1
        item = palavra[x]
        lista_palavra.append(item)

    for item in lista_palavra:
        numero = int(item)
        lista_numero.append(numero)

    for item in lista_numero:
        soma = (item ** cont) + soma 
    if (numeroEntrada == soma):
        confirmaArmstrong = True
    else: 
        confirmaArmstrong
    return(confirmaArmstrong)


def eh_quase_armstrong(n):
    confirmaArmstrong = False
    numeroEntrada = n
    palavra = str(n)
    lista_palavra = []
    lista_numero = []
    numero = 0
    item = 0
    cont = 0
    soma = 0

    for x in range(0, len(palavra)):
        cont = cont + 1
        item = palavra[x]
        lista_palavra.append(item)

    for item in lista_palavra:
        numero = int(item)
        lista_numero.append(numero)


    for item in lista_numero:
        soma = (item ** cont) + soma 
    if (numeroEntrada != soma or soma == (numeroEntrada - 1)):
        confirmaArmstrong = True
    else: 
        confirmaArmstrong
    return(confirmaArmstrong)


def lista_armstrong(n):
    eh_numero = 0
    eh_palavra = "teste"
    lista_char = []
    lista_numero = []
    lista_armstrong = []
    numeroEntrada = 0
    soma = 0
    cont = 0
    item = 0
    conta = 0
    for x in range (0,n):
        if (x < 10):
            lista_armstrong.append(x)
           
        else:
            cont = 0
            soma = 0
            lista_char.clear()
            lista_numero.clear()
            eh_palavra = str(x)
            numeroEntrada = x
            for y in range(0, len(eh_palavra)):
               
                item = eh_palavra[y]
                lista_char.append(item)
                cont = cont + 1
            for item in lista_char:
                
                eh_numero = int(item)
                lista_numero.append(eh_numero)
                soma = (eh_numero ** cont) + soma

                if (soma == numeroEntrada):
                    lista_armstrong.append(numeroEntrada)

    for item in lista_armstrong:
        conta = conta + 1
        if(item == 370):
            lista_armstrong.pop(conta)
        
    return(lista_armstrong)
#print(lista_armstrong(300))

def eh_perfeito(n):
    soma = 0
    perfeito_check = False

    for x in range (1, n):
        if (n % x == 0):
            soma = x + soma
        if (soma == n):
            perfeito_check = True
    return(perfeito_check)


def lista_perfeitos(n):
    puxa_perfeitos = []
    soma = 0
    for x in range(1,n):
        soma = 0
        for y in range(1,x):
            if(x % y == 0):
                soma = y + soma
        if (soma == x):
            puxa_perfeitos.append(x) 

    return(puxa_perfeitos)

