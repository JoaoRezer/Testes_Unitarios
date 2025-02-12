import pytest

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum( 1 for letra in texto if letra in vogais)

def test_contar_vogais():
    assert contar_vogais("banana") == 3
    assert contar_vogais("PYTHON") == 1
    assert contar_vogais("rhythm") == 0


def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def test_eh_primo():
    assert eh_primo(2) == True
    assert eh_primo(3) == True
    assert eh_primo(4) == False
    assert eh_primo(5) == True
    assert eh_primo(11) == True
    assert eh_primo(15) == False

# ESTE CODIGO A SEGUIR IRÁ RETORNAR UM ERRO NO PYTEST

# ❌ def dividir(a, b):
#     return a / b  # Pode causar erro se b for 0

# def test_dividir():
#     assert dividir(10, 2) == 5
#     assert dividir(5, 0)  # Isso causará um erro!❌





# como corrigir

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def test_dividir():
    assert dividir(10, 2) == 5

    try:
        dividir(5, 0)
    except ValueError as e:
        assert str(e) == "Não é possível dividir por zero!"


