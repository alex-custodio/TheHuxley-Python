# Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

n1 = int(input())
n2 = int(input())
n3 = int(input())
numeros = []
numeros.extend([n1, n2, n3])
numeros.sort()
for num in numeros:
    print(num)
