# Função para mostrar o menor entre três números inteiros
def find_smallest(num1, num2, num3):
    return min(num1, num2, num3)


number1 = float(input("Escreva o primeiro numero: "))
number2 = float(input("Escreva o segundo numero: "))
number3 = float(input("Escreva o terceiro numero: "))

# Display the smallest number
smallest = find_smallest(number1, number2, number3)
print("O menor número é:", smallest)
