import unittest

def calcular_media(n1,n2):
    n3 = n1 + n2
    return n3/2

class TesteMedia(unittest.TestCase):
    def test_media(self):
        n1 = 10
        n2 = 20
        resultado_esperado = 15
        
        resultado_real = calcular_media(n1,n2)
        self.assertEqual(resultado_real, resultado_esperado)

if __name__ == '__main__':
    unittest.main()
