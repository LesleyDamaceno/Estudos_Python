def primo(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True

def n_primos(n):
    cont = 0
    i = 2
    while i <= n:
        if primo(i):
            cont = cont + 1
        i = i + 1
    return cont

n = int(input("Digite um número inteiro maior ou igual a 2: "))
while n < 2:
    n = int(input("Digite um número inteiro maior ou igual a 2: "))

print(n_primos(n))