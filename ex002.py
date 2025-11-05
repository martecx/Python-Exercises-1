# Ler os três valores inteiros
a = int(input("Escreva um valor para a: "))
b = int(input("Escreva um valor para b: "))
c = int(input("Escreva um valor para c: "))

# Checar se os valores formam um triângulo
if a < b + c and b < a + c and c < a + b:
    print(f"Os valores {a}, {b}, and {c} formam um triângulo.")
else:
    if a >= b + c:
        print(f"Os valores não formam um triângulo, o {a} é maior.")
    elif b >= a + c:
        print(f"Os valores não formam um triângulo, o {b} é maior.")
    else:
        print(f"Os valores não formam um triângulo, o {c} é maior.")
