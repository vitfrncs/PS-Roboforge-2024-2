"""
1.Se precisar use: from math import *.
2.Dado 3 pontos cartesianos da forma (x,y), faça o que se pede:
3.Calcule os três lados do triângulo e imprima-os na tela.
4.Calcule os três ângulos do triângulo e imprima-os na tela.
5.Calcule o perímetro e a área do triângulo e imprima na tela.
6.Imprima se o triângulo é equilátero, isósceles ou escaleno.
7.Imprima se o triângulo é acutângulo, retângulo ou obtusângulo.

"""

from math import *

# para calcular os lados do triângulo, basta usar a formula da distância entre 2 pontos
# um ponto é uma tupla
def dist (pontoA, pontoB):
        return sqrt((pontoB[0] - pontoA[0])**2 + (pontoB[1] - pontoA[1])**2)

# usa-se a lei dos cossenos para calcular os ângulos do triangulo, já que temos os valores dos 3 lados
# math.acos() calcula arcosseno em rad, para passar para ° usa-se dregrees
def angulo (a, b, c):
        return degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))

def perimetro (a, b, c):
    return a+b+c

# como temos os três lados do triângulo, dá para usar a fórmula de heron
def area (a, b, c):
    p = perimetro(a,b,c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

# recebe os lados do triângulo como argumento:
def tipoTriangulo (a, b, c):
      if a == b == c:
            return "Equilátero"
      elif a != b and b != c and a != c:
            return "Escaleno"
      else: 
            return "Isoceles"

# recebe os ângulos do triângulo como argumento:
def tipoAngulo (a, b, c):
    if a < 90 and b < 90  and c < 90:
        return "Acutângulo"
    elif a == 90 or b == 90 or c == 90:
        return "Retângulo"
    else: 
          return "Obtusângulo" # palavra absurda
    

# lendos os pontos:
def ler_ponto(numero):
    while True:
            valores = list(map(float, input(f"Digite as coordenadas do ponto {numero} (x y): ").split()))
            if len(valores) != 2:
                print("Entrada inválida! Digite dois números separados por espaço.")
            else: return tuple(valores)
        

while True: 
    p1 = ler_ponto(1)
    p2 = ler_ponto(2)
    p3 = ler_ponto(3)

    # calculando lados 
    l1 = dist(p1, p2)
    l2 = dist(p2, p3)
    l3 = dist(p3, p1) 

    if p1 == p2 or p2 == p3 or p3 == p1:
        print("Há dois pontos iguais, digite os valores novamente :D")
    elif area(l1, l2, l3) == 0:
        print("Os pontos fornecidos são colineares, digite os valores novamente :D")
    else: 
        break
         
print(f'Pontos digitados p1 = {p1}, p2 = {p2} e p3 = {p3}.')

print(f'Os lados do triângulo são {l1}, {l2} e {l3}.')

# calculando ângulos:
a1 = angulo(l1, l2, l3)
a2 = angulo(l2, l3, l1)
a3 = angulo(l3, l1, l2)

print(f'Os ângulos do triângulo são a1 = {a1}, a2 = {a2} e a3 = {a3}.')

print(f'O triângulo é {tipoTriangulo(l1, l2, l3)} e {tipoAngulo(a1, a2, a3)}.')

# inventei que a unidade é centimetros pra ficar bonitinha a mensagem
print(f'Seu perimetro é de {perimetro(l1,l2,l3)}cm e a área é de {area(l1,l2,l3)}cm².')