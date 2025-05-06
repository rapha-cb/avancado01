def imprime_nome(nome):
    print(f"Nome: {nome}")

def piramide(n):
    for i in range(1,n+1):
        for j in range(0, i):
            print(i, end= " ")
        print()

def vogais(texto):
    contagem = 0
    for i in range(0, len(texto)):
        if texto[i] == "a" or texto[i] =="e" or texto[i] == "i" or texto[i] =="o" or texto[i] =="u":
            contagem+= 1
    print(contagem)
def valor_estoque(produto, qntd, valor):
    valor_total= qntd* valor
    return valor_total

def caractere(numero):
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return 'Z'

def soma(*a):
    somar= 0
    for x in range(len(a)):
        somar += a[x]
    print(somar)

def texto_principal(texto, ):
    cont = 0
    for i in range(len(texto)):
        if texto[i] != " ":
            cont+= 1
    print(f"quantidade de letras: {cont}")
    for j in range(len(texto)-1,-1,-1):
        print(texto[j], end=" ")

def verifica_lista(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    print(nova_lista)





