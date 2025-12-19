import unittest
import sys
sys.path.append('./')
from circle import *


class CirleTestCase(unittest.TestCase):
   def test_zer(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_area(self):
       res = area(1)
       self.assertEqual(res, 3.141592653589793)

   def test_perimeter(self):
       res = perimeter(1)
       self.assertEqual(res, 6.283185307179586)


if __name__ == "__main__":
    unittest.main()