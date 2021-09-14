import unittest
from BalancedAB import BalancedAB
class TestBalancedAP(unittest.TestCase):
    def test_1(self):
        self.assertEqual(BalancedAB("AAZZBB"),True)
    def test_2(self):
        self.assertEqual(BalancedAB("AAAXXXXYB"),True)
    def test_3(self):
        self.assertEqual(BalancedAB("BBYYYXXXAXX"),False)
    def test_4(self):
        self.assertEqual(BalancedAB(""),True)
    def test_5(self):
        self.assertEqual(BalancedAB("XXXXXYYYYZZZZB"),True)
    def test_6(self):
        self.assertEqual(BalancedAB(" XXXXXYYYYZZZZ"),True)
    def test_7(self):
        self.assertEqual(BalancedAB("XXXX  XYYYY  ZZZZB"),True)
    def test_8(self):
        self.assertEqual(BalancedAB("YYYBABYYYXXXAXX"),False)
    def test_9(self):
        self.assertEqual(BalancedAB("ABABABA"),False)






if __name__ == '__main__':
    unittest.main()