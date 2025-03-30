"""
1. Escreva uma função que recebe um número e retorna True se ele for primo e
False se não for primo.
2. Um número é primo se ele for divisível apenas por 1 e ele mesmo.
3. Escreva outra função, que gere uma lista de 10 números em um intervalo
qualquer.
4. Multiplique todos os primos dessa lista e retorne o resultado.
"""

from random import randint

# para verificar se um número n é primo, basta ver ser sqrt(n) % i == 0, para todo i = 2, ..., sqrt(n) + +1 (teto)
# se for verdade para algum i, a função retorna False
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

def listaAleatoria ():
    l = []
    for i in range (0, 10):
        l.append(randint(0,100))
    return l

def mulPrimos (l):
    produto = 1
    for i in l:
        if (primo(i)):
            produto *= i
    return produto

l = listaAleatoria()
print("Lista com num geredos aleatoriamente: " + str(l))
print("Produto dos números primos da lista: " + str(mulPrimos(l)))



