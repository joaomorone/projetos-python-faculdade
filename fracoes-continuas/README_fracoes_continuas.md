Conversor de números racionais e frações contínuas

Programa em Python que converte um número racional em sua **fração contínua** e faz o caminho inverso, reconstruindo a fração a partir dos coeficientes. Foi desenvolvido para uma apresentação da disciplina.

## O que ele faz

**1. Racional → fração contínua**
Recebe numerador e denominador e calcula os coeficientes `a_0, a_1, a_2, ...` pelo algoritmo de Euclides (divisões sucessivas).

**2. Fração contínua → racional**
Recebe a quantidade de termos e os coeficientes e reconstrói a fração `numerador/denominador`, usando a relação de recorrência dos convergentes.

## Conceitos praticados

- Algoritmo de Euclides
- Frações contínuas
- Laços `while` e relações de recorrência
- Validação de entrada (denominador zero, número de termos inválido)

## Como executar

Requer Python 3:

fracoes_continuas.py

## Exemplo

Para `415/93`:

```
NÚMERO RACIONAL -> FRAÇÃO CONTÍNUA

Numerador: 415
Denominador: 93
a_0 =  4
a_1 =  2
a_2 =  6
a_3 =  7
```

Ou seja, `415/93 = [4; 2, 6, 7]`. Para voltar:

```
FRAÇÃO CONTÍNUA -> NÚMERO RACIONAL

Quantidade de termos (n+1): 4
a_0: 4
a_1: 2
a_2: 6
a_3: 7

Número racional: 415/93
```

## Observações

- A fração reconstruída é apresentada sem simplificação adicional, mas os convergentes já saem em forma irredutível.
- O programa trabalha com inteiros positivos.
