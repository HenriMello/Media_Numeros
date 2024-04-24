def calcular_media(n1,n2):
    n3 = n1 + n2
    return n3/2

def test_media():
    n1 = 10
    n2 = 20

    resultado = calcular_media(n1,n2)

    assert resultado == 15.0, "A média calculado não está correta"

