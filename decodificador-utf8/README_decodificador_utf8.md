Decodificador de UTF-8 feito à mão

Programa em Python que lê uma mensagem escrita em binário (0s e 1s), decodifica segundo as regras do **UTF-8** e recupera o texto original em português, sem usar `.decode()`.

## O que ele faz

1. Lê a sequência de bits do arquivo `Binario.txt`.
2. Divide a sequência em bytes de 8 bits.
3. Mostra a mensagem em hexadecimal (conversão implementada manualmente).
4. Interpreta os bytes pelas regras do UTF-8:
   - `0xxxxxxx`: caractere de 1 byte (ASCII);
   - `110xxxxx`, `1110xxxx`, `11110xxx`: byte inicial de caractere com 2, 3 ou 4 bytes;
   - `10xxxxxx`: byte de continuação.
5. Converte os bits restantes em pontos de código (números) e depois em caracteres.
6. Grava o texto final em `Portugues.txt`.

## Conceitos praticados

- Sistemas de numeração (binário, decimal e hexadecimal)
- Codificação de caracteres (Unicode e UTF-8)
- Manipulação de strings e listas
- Leitura e escrita de arquivos

## Como executar

Requer Python 3. Coloque o `Binario.txt` na mesma pasta do script e rode:

```bash
python desafio2.py
```

O repositório já traz um `Binario.txt` de exemplo.

## Limitações conhecidas

- A conversão para hexadecimal não completa com zero à esquerda os bytes menores que `0x10` (ex.: `0x0A` aparece como `A`).
- Não há tratamento de erro para arquivo ausente ou bits inválidos.
