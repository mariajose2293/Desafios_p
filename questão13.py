pares = []
impares = []
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Pares:", pares)
print("Ímpares:", impares)