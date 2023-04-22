def es_primo(numero):

    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
print(es_primo(9))  # False
print(es_primo(11)) # True


def primos_hasta(n):

    primos = []
    for i in range(2, n+1):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos
print(primos_hasta(10)) # [2, 3, 5, 7]
print(primos_hasta(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
