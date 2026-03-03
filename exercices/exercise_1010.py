linha1 = input().split()
cod1 = int(linha1[0])
num1 = int(linha1[1])
val1 = float(linha1[2])

linha2 = input().split()
cod2 = int(linha2[0])
num2 = int(linha2[1])
val2 = float(linha2[2])

TOTAL1 = num1 * val1
TOTAL2 = num2 * val2

TOTAL = TOTAL1 + TOTAL2

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")
