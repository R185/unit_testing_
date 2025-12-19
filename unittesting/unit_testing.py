import unittest
import sys
sys.path.append('./')
import triangle
import circle
import rectangle


class CirleTestCase(unittest.TestCase):
    def test_zer(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = circle.area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_perimeter(self):
        res = circle.perimeter(1)
        self.assertEqual(res, 6.283185307179586)

class TriangleTestCase(unittest.TestCase):
    def test_zer(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = triangle.area(10, 2)
        self.assertEqual(res, 10)

    def test_perimeter(self):
        res = triangle.perimeter(10, 10, 10)
        self.assertEqual(res, 30)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_mul(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

if __name__ == "__main__":
    unittest.main()

