import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.topla(10,5),15)
        self.assertEqual(calc.topla(-1,1),0)
        self.assertEqual(calc.topla(-1,-1),-2)
    def test_subt(self):
        self.assertEqual(calc.cikar(10,5),5)
        self.assertEqual(calc.cikar(-1,1),-2)
        self.assertEqual(calc.cikar(-1,-1),0) 
    def test_mul(self):
        self.assertEqual(calc.carp(10,5),50)
        self.assertEqual(calc.carp(-1,1),-1)
        self.assertEqual(calc.carp(-1,-1),1)
    def test_div(self):
        self.assertEqual(calc.böl(10,5),2)
        self.assertEqual(calc.böl(-1,1),-1)
        self.assertEqual(calc.böl(5,2),2.5)

        #self.assertRaises(ValueError,calc.böl,10,0)
        with self.assertRaises(ValueError):
            calc.böl(10,0)
            

if __name__ == '__main__':
    unittest.main()