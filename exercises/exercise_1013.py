valor = input().split()
A = int(valor[0])
B = int(valor[1])
C = int(valor[2])
maior_ab = (A + B + abs(A - B)) // 2

maior_b = (maior_ab + C + abs(maior_ab - C)) // 2

print(f"{maior_b} eh o maior")