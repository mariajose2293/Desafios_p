texto = input("Digite uma frase: ")
vogais = 'aeiou'
count = sum(1 for char in texto.lower() if char in vogais)
print("Vogais:", count)