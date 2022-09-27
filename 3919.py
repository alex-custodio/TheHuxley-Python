# Leia um inteiro N.
# Depois, leia até 20 inteiros X0, X1, ..., X20. Seu programa deve imprimir quantas vezes o inteiro N aparece nos X inteiros.

# 1 - Ler um número N
# 2 - Contador de vezes para aparições de N nos próximos 20 numeros
# 3 - Para cada numero num range de 0 a 20:
#   se o numero for -1:
#     para de repetir
#   se o numero for igual a N:
#       contador += 1
n = int(input(""))
contador = 0
for numero in range(0, 20):
    numero = int(input(""))
    if numero == -1:
        break
    if numero == n:
        contador += 1
print(f"{n} apareceu {contador} vezes")
