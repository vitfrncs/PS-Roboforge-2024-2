"""
1. Crie uma variável que receba os dados que você digitar e mostre o tipo dela na
tela. Ex: você digita “2” e retorna que é int,“casa” e retorna que é string.
2. Printe na tela o tipo e a variável.
3. Crie uma lista que recebe os dados que você digitar e printe na tela.
4.Crie uma função que codifica essa lista em uma string EXATAMENTE nesse formato:
“(str: ’casa’), (float: 3.14,) list(str: ‘Roboforge’, bool: True]” e mostre na tela.
5. Crie uma função que decodifique e mostre na tela.
"""


import sys, re



# Primeiro testei o comando print(int(x)) com x = 2.1 e o erro ValueError foi retornado
# Testei o mesmo comando com x = "True" e o mesmo erro foi retornado. Então usei uma estrutura de try-catch
# pra transforma o que foi digitado em um tipo correto
# função que transforma uma str tipo de dado adequado:
def transformaString(x):
    if x == "True":
        return True
    elif x == "False":
        return False
    if x.startswith("[") and x.endswith("]"): # para listas aninhadas :D
                elementos = x[1:-1].split(",")  # remove colchetes e divide os elementos qunado tem ","
                lista = []
                for i in elementos:
                    i = i.strip()  # removendo espaços 
                    lista.append(transformaString(i))  # #transforma cada elemento da lista
                return lista 
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError: 
            return x


def retornaTipoStr(x):
    tipo = str(type(x))
    if tipo == "<class 'float'>":
         return "float"
    elif tipo == "<class 'int'>":
         return"int"
    elif tipo == "<class 'bool'>":
         return "bool"
    elif tipo == "<class 'list>":
        return "list"
    else: 
         return "str"
        
  
def codifica(l):
    elementos_codificados = []
    for i in l:
        if isinstance(i, list):
            itens_codificados = codifica(i)  # recursão para listas aninhadas
            elementos_codificados.append(f"list([{itens_codificados}])") # coloca elem da lista aninhada dentro de list([])
        else:
            valor = f"'{i}'" if isinstance(i, str) else i # para que quando for string, ela seja mostrada com ''
            elementos_codificados.append(f"({retornaTipoStr(i)}: {valor})")
    return ", ".join(elementos_codificados) # junta todos os elem da lista e os separa com ","

def decodifica(codigo):
    """se o código estiver todo encapsulado (começando com "list([" e terminando com "])"),
       a função remove esse encapsulamento e separa em partes utilizando a função 'separaPartes'."""
    codigo = codigo.strip() # tira esp da string do argumento
    if codigo.startswith("list([") and codigo.endswith("])"): # verifica se é lista aninhada
        interior = codigo[6:-2].strip()  # remove o "list([" do início e "])" do final
        partes = separaPartes(interior)  #se a condição do if não for satisfeita, separaParte é chamado direito na string
        return [decodifica(p) for p in partes] # chama a função de novo para cada elem p/ caso de listas aninhadas
    partes = separaPartes(codigo)
    if len(partes) == 1:
        return trataParte(partes[0])
    else:
        return [trataParte(p) for p in partes]

# separa cada elemento de um lista
# Ex: se tiver(int: 23), list[(int: 1), (str: 'oiiii')] retorna uma lista [(int: 23), list[(int: 1), (str: 'oiiii')]]
def separaPartes(codigo):
    partes = []
    buffer = ""
    nivel = 0
    for char in codigo:
        if char in "([":
            nivel += 1
        elif char in ")]":
            nivel -= 1
        if char == "," and nivel == 0:
            partes.append(buffer.strip())
            buffer = ""
        else:
            buffer += char
    if buffer.strip():
        partes.append(buffer.strip())
    return partes

# usa tranformaString para transformar a string no tipo de dado original
def trataParte(parte):
    parte = parte.strip()
    if parte.startswith("list("): # se for lista aninhada chama decodifica de novo
        return decodifica(parte)
    if parte.startswith("(") and parte.endswith(")"):
        inner = parte[1:-1].strip()  # remove os parênteses do começo e final
        comps = inner.split(":", 1) # divide a string em dois componentes usando o caractere : como separador
        if len(comps) == 2: 
            tipo = comps[0].strip()
            valor = comps[1].strip()
            if tipo == "str":
                return valor.strip("'").strip() # tira '' da string
            else:
                return transformaString(valor)
        else:
            return parte
    return parte


######### TESTES #######################################################################################

sys.stdin.flush()
x = input('Digite um dado: ')

print(retornaTipoStr(transformaString(x)) + ': ' + x + "\n")

# criando uma lista vazia que irá receber os dados que digitarei na tela:
l = []

while (True):
     sys.stdin.flush()
     elem = input("Digite um dado que deseja armazenar: (ou sair para sair do loop) ")
     if (elem == "sair"):
          break
     l.append(transformaString(elem))

print("Lista criada: ", l)

p = codifica(l)

print ("Lista Codificada: ", p)
print("Lista decodificada: ", decodifica(p))


     

