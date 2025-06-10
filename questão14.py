nomes = []
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
print("Nomes em ordem inversa:", nomes[::-1])