def isprime(x):
    """
    determina daca un nr intreg e prim
    param. x - un numar intreg
    return - True daca x e prim, False in caz contrar
    """
    if x < 2: return False
    for i in range(2, x//2+1):
        if x % i == 0: return False
    return True
    

def test_isprime():
    assert isprime(0) == False
    assert isprime(2) == True
    assert isprime(997) == True


test_isprime()


def get_largest_prime_below(n):
    """
    Găsește ultimul număr prim mai mic decât un număr dat
    param. n - numarul dat
    return - ultimul număr prim mai mic decât n
    """
    for i in range(n-1, 1, -1):
        if isprime(i): return i
    return None


def test_get_largest_prime_below():
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(149) == 139


test_get_largest_prime_below()


def is_palindrome(n) -> bool:
    """
    Determină dacă un număr dat este palindrom
    param. n - numarul dat
    return - True daca n este palindrom, False in caz contrar
    """
    copie_n = n
    oglindit_n = 0
    while copie_n > 0:
        oglindit_n = 10 * oglindit_n + copie_n % 10
        copie_n = copie_n // 10
    if n == oglindit_n: return True
    return False


def test_is_palindrome():
    assert is_palindrome(0) == True
    assert is_palindrome(6498946) == True
    assert is_palindrome(481579) == False


test_is_palindrome()