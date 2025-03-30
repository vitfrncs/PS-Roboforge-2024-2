"""1.Escreva uma função que receba um número.
2.Se este número for divisível por 3 retorne “Fizz”.
3.Se este número for divisível por 5 retorne “Buzz”.
4.Se este número for divisível por 3 e por 5 retorne “FizzBuzz”.
5.Se nada disso for verdade retorne “#”."""

def funcao(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0: 
        return 'Buzz'
    else:
        return '#'  

x = int(input('Digite um número: '))
print('Resultado: ' + funcao(x))


    

