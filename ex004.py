#Checar se o número é primo

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testar numeros de 1 a 100
for number in range(1, 101):
    print(f"{number}: {is_prime(number)}")
