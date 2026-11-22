Busca de números multibinários

Programa em Python que encontra os números que, escritos nas bases **2, 3, 4 e 5**, usam **apenas os algarismos 0 e 1**. Chamei esses números de "multibinários".

## O que ele faz

1. Pede um limite superior.
2. Para cada número de 2 até o limite, converte o número para as bases 2, 3, 4 e 5.
3. Verifica, com uma função recursiva, se todos os algarismos são 0 ou 1 em cada base.
4. Imprime a lista dos números que passam no teste.

## Conceitos praticados

- Mudança de base por divisões sucessivas
- Recursão
- Decomposição do problema em funções pequenas (`converteBase`, `procuraZeroUm`, `multibinario`)

## Como executar

Requer Python 3:

tema3Desafio1.py

## Exemplo

```
Procurar multibinários até: 100000
Números multibinários (bases 2 a 5): [82000]
```

Nos testes que fiz, até 2.000.000 o único número encontrado foi **82000**. Ele escreve-se como `10100000001010000` (base 2), `11011111001` (base 3), `110001100` (base 4) e `10111000` (base 5), todos só com 0 e 1.
