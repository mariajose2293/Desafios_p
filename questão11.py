numeros = []
for i in range(5):
    num = float(input(f"Digite o número {i+1}: "))
    numeros.append(num)
print("Soma:", sum(numeros))