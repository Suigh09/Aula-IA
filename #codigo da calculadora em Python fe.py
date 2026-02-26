#codigo da calculadora em Python feito na aula 

import math

def Opções():
    print("\n ------ Calculadora -------")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - potenciação")
    print("6 - radiciação")
    print("0 - Finalizar")
    
while True: 
    Opções()
    escolha = input("\nEscolha uma das opções: ")
    
    if escolha == "0":
       print("Obrigado por usar nossa calculadora") 
       break
   
    if escolha in ['1', '2', '3', '4', '5']:
       numero1 = float(input("Adicione o primeiro numero: "))
       numero2 = float(input("Adicione o segundo numero: "))
   
    if escolha == '1':
            print(f"Resultado: {numero1 + numero2}")
    elif escolha == '2':
            print(f"Resultado: {numero1 - numero2}")
    elif escolha == '3':
            print(f"Resultado: {numero1 * numero2}")
    elif escolha == '4':
            if numero2 != 0:
                print(f"Resultado: {numero1 / numero2}")
            else:
                print("Erro: Serio? Dividir por 0 é foda.")
    elif escolha == '5':
            print(f"Resultado: {numero1 ** numero2}")

    elif escolha == '6':
        num = float(input("Adicione o número para extrair a raiz: "))
        if num >= 0:
            print(f"Resultado: {math.sqrt(num)}")
        else:
            print("Erro: Não é possível calcular raiz quadrada de número negativo.")
    
    else:
        print("Opção inválida! Tente novamente.")