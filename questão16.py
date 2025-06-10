numeros = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
soma = sum(num for num in numeros if num % 5 == 0)
print("Soma dos múltiplos de 5:", soma)