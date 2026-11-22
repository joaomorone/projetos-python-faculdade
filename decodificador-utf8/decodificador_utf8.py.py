# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:39:11 2026

@author: PauloVictor
"""


def decimal_para_hex(numero):
    if numero == 0:
        return '0'
    letras_hex = '0123456789ABCDEF'
    resultado = ''
    while numero > 0:
        resto = numero % 16
        resultado += letras_hex[resto]
        numero = numero // 16
    return resultado[::-1]


def lerArq():
    arq = open('Binario.txt', 'r')
    frase = arq.readline()
    arq.close()
    return frase


def corte8(s):
    lista = []
    for bites in range(0, len(s), 8):
        lista.append(s[bites:bites+8])
    return lista


def convHex(l):
    print('Lista de bytes:', l)
    lDecimal = []
    for item in l:
        lDecimal.append(int(item, 2))
    fHex = ''
    for elem in lDecimal:
        fHex += decimal_para_hex(elem)
    print('Mensagem em hexadecimal:', fHex)
    return fHex


def codigo(lBytes):
    lBinario = []
    for byte in lBytes:
        if byte[0] == '0':
            lBinario.append(byte[1:])
        elif byte[1] == '0':
            lBinario[-1] = lBinario[-1] + byte[2:]
        elif byte[2] == '0':
            lBinario.append(byte[3:])
        elif byte[3] == '0':
            lBinario.append(byte[4:])
        elif byte[4] == '0':
            lBinario.append(byte[5:])

    lNumeros = []
    for binário in lBinario:
        total = 0
        tam = len(binário) - 1
        for dig in binário:
            dig = int(dig)
            total += dig * 2**tam
            tam = tam - 1
        lNumeros.append(total)

    print('Lista de pontos de código:', lNumeros)
    return lNumeros


def convCaractere(lNumeros):
    frase = ''
    for num in lNumeros:
        caractere = chr(num)
        frase += caractere
    print('Frase em português:', frase)
    return frase


def arquivo(frase):
    arquivo = open('Portugues.txt', 'w')
    arquivo.write(frase)
    arquivo.close()
    return


# Bloco principal
lido = lerArq()
lista = corte8(lido)
convHex(lista)
lNumeros = codigo(lista)
frase = convCaractere(lNumeros)
arquivo(frase)
