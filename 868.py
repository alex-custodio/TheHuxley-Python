lista_ler = []
lista_d = []
while True:
    n, d = input().split(" ")
    n = int(n)
    d = int(d)
    if 5 <= n <= 1000 and 0 <= d <= 9:
        break
for numero in range(0, n):
    n = int(input())
    if (n < 0):
        break
    lista_ler.append(n)
for elemento in lista_ler:
    if str(elemento).endswith(str(d)):
        lista_d.append(int(elemento))
    else:
        lista_d.append(-1)
lista_d.sort()
lista_ultimos = [lista_d[-5], lista_d[-4],
                 lista_d[-3], lista_d[-2], lista_d[-1]]
for elemento in lista_ultimos:
    print(elemento)
