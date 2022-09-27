# Ler 3 notas e tirar a média
n1 = float(input())
n2 = float(input())
n3 = float(input())

mediaNormal = (n1 + n2 + n3) / 3
mediaPonderada1 = (n1 * 2 + n2 * 2 + n3 * 3) / (2 + 2 + 3)
mediaPonderada2 = (n1 * 1 + n2 * 2 + n3 * 2) / (1 + 2 + 2)
print(f"{mediaNormal:.2f}")
print(f"{mediaPonderada1:.2f}")
print(f"{mediaPonderada2:.2f}")
