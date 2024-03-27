#1. Escreva um programa que imprima "Olá, mundo!" na tela.
print("Olá, mundo!")

#2. Escreva um programa que solicite ao usuário seu nome e o cumprimente.
#nome = input("Digite seu nome:")
#print(f"Olá {nome}!")

#3. Escreva um programa que calcule a soma de dois números inseridos pelo usuário.
"""num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
print(f"A soma dos números é : {num1 + num2}")"""

#4. Escreva um programa que verifique se um número inserido pelo usuário é par ou ímpar.
numero = int(input("Digite o numero para verificação: "))
if numero %2==0:
  print("Par")
else:
  print("Impar")  

#5. Escreva um programa que solicite ao usuário um número e imprima todos os números de 1 até esse número.
valor = int(input("Digite um valor:"))
for index in range(valor):
  print(index)


