# Gerador de senhas
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simbolos = ["!", "#", "$", "%", "&", "*", "+"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("Seja bem-vindo ao gerador de senhas.")

num_letras = int(input("Quantas letras você deseja na sua senha? "))
num_simbolos = int(input("Quantos simbolos você deseja? "))
num_numeros = int(input("Quantos números você deseja? "))

senha_lista = []

for letra in range(num_letras):
    senha_lista.append(random.choice(letras))

for simbolo in range(num_simbolos):
    senha_lista.append(random.choice(simbolos))

for _numero in range(num_numeros):
    senha_lista.append(random.choice(numeros))

random.shuffle(senha_lista)

senha = ''.join(senha_lista)
print(f"Sua senha segura: {senha}")
