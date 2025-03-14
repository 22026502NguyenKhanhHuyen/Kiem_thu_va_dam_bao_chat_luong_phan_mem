import unittest
from tinh_gia_ve import tinh_gia_ve

class TestTinhGiaVe(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(tinh_gia_ve(5, True, True), 0)
    
    def test_case_2(self):
        self.assertEqual(tinh_gia_ve(7, False, False), 50000)
    
    def test_case_3(self):
        self.assertEqual(tinh_gia_ve(15, False, False), 100000)

if __name__ == "__main__":
    unittest.main()
