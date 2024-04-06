import unittest

def is_prime(valor):
    num=valor-1
    while num>1:
        if valor%num==0:
            return False
        num=num-1
    return True


# def is_prime(valor):
#     if valor <= 1:
#         return False
#     for i in range (2,valor):
#        if valor % 1 == 0: 
#           return False
#     return True


# valor = 40 
# if is_prime ( valor):
#     print ("si")
# else:
#     print ("no")

class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result=is_prime(1)
        self.assertTrue(result)
    def test_with_2(self):
        result=is_prime(2)
        self.assertTrue(result)
    def test_with_3(self):
        result=is_prime(3)
        self.assertTrue(result)
    def test_with_4(self):
        result=is_prime(4)
        self.assertFalse(result)
    def test_with_5(self):
        result=is_prime(5)
        self.assertTrue(result)

unittest.main()