def eh_par(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
num = int(input("Digite um número: "))
print(eh_par(num))