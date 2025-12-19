import unittest
import sys
sys.path.append('./')
from rectangle import *


class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_perimeter_mul(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)

   def test_perimeter_mul_str(self):
       res = perimeter("10", "30")
       self.assertEqual(res, 40)

if __name__ == "__main__":
    unittest.main()
