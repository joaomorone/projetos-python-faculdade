def fracaoContinua():
    print('NÚMERO RACIONAL -> FRAÇÃO CONTÍNUA ')
    a = int(input('\nNumerador: '))
    b = int(input('Denominador: '))
    if b == 0 :
        print('\nO denominador não pode ser 0')
    else: 
        i = 0
        while b != 0:
            print('a_' + str(i) + ' = ', a//b )
            resto = a%b
            a = b
            b = resto
            i += 1
    print('-' * 30)            
            
def numRacional():
    
    print('\nFRAÇÃO CONTÍNUA -> NÚMERO RACIONAL')
    n = int(input('\nQuantidade de termos (n+1): '))
    if n<= 0 :
        print('\nÉ necessário pelo menos um termo!')
    else: 
        num = 1
        den = 0
        numAnt = 0
        denAnt = 1
        i = 0
        while i<n:
            a_i = int(input('a_' + str(i) + ': '))
            numNovo = a_i * num + numAnt
            denNovo = a_i * den + denAnt
            numAnt = num
            denAnt = den
            num = numNovo
            den = denNovo
            i += 1
        print('\nNúmero racional: ' + str(num) + '/' + str(den))
     
fracaoContinua()    
numRacional()
                