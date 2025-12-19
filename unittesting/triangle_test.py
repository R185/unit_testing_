import unittest
import sys
sys.path.append('../')
from triangle import *


class CirleTestCase(unittest.TestCase):
   def test_zer(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_area(self):
       res = area(10, 2)
       self.assertEqual(res, 10)

   def test_perimeter(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)


if __name__ == "__main__":
    unittest.main()