while True:
    print("\nMenu:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "5":
        break
    
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        continue
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        print("Resultado:", num1 * num2)
    elif opcao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero!")