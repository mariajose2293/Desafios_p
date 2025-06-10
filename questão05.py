num = int(input("Digite um número: "))
soma = sum(i for i in range(1, num+1) if i % 2 != 0)
print("Soma dos ímpares:", soma)