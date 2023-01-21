import sys

str = "Hello world"

y=1

x = 1

def somar(primeiro_op,segundo_operador):
    print("Começou o método")
    print(f"O primeiro operador é: {primeiro_op}")
    print(f"O segundo operador é: {segundo_operador}")
    print(primeiro_op + segundo_operador)
    print("Terminou o método")

def subtrair(a ,b):
    print (a -b)

def multiplicar(a ,b):
    print (a *b)

print(str)

print(y)

print(x)

somar(x,y)

subtrair(x,y)

multiplicar(x ,y)
