# Arman Rafian
# Section 7

import unittest
from ordered_list import *

class test_ordered_list(unittest.TestCase):
    def test_add(self):
        list1 = OrderedList()
        self.assertTrue(list1.is_empty)
        self.assertEqual(list1.size(), 0)
        self.assertEqual(list1.index(1), -1)
        self.assertEqual(list1.remove(16), -1)
        list1.add(5)
        list1.add(-13.57)
        self.assertFalse(list1.search_forward(-13.5))
        list1.add(8.0)
        self.assertTrue(list1.search_backward(5))
        self.assertEqual(list1.remove(-13.57), 0)
        # only two values should be left
        self.assertEqual(repr(list1), '[5, 8.0]')
        # test add
        list1.add(0)
        list1.add(10223)
        list1.add(-0.05)
        list1.add(-64)
        list1.add(45)
        list1.add(207656.9)
        # test searches
        self.assertEqual(repr(list1), '[-64, -0.05, 0, 5, 8.0, 45, 10223, 207656.9]')
        self.assertTrue(list1.search_forward(10223))
        self.assertTrue(list1.search_forward(-64))
        self.assertFalse(list1.search_forward(36))
        self.assertTrue(list1.search_backward(-64))
        self.assertTrue(list1.search_backward(0))
        self.assertEqual(list1.size(), 8)
        self.assertEqual(list1.index(10223), 6)
        self.assertEqual(list1.index(207656.9), 7)
        self.assertEqual(list1.index(-64), 0)
        self.assertEqual(list1.index(50), -1)
        self.assertFalse(list1.is_empty())
        # testing removes, begin, middle, and end
        self.assertEqual(list1.remove(5), 3)
        self.assertEqual(list1.remove(-64), 0)
        self.assertEqual(list1.remove(207656.9), 5)
        # testing both types of pop, beginning, middle, and end
        self.assertEqual(repr(list1), '[-0.05, 0, 8.0, 45, 10223]')
        self.assertEqual(list1.pop(4), 10223)
        self.assertEqual(list1.pop(), 45)
        self.assertEqual(list1.pop(1), 0)
        self.assertEqual(list1.pop(0), -0.05)
        # testing error catching
        with self.assertRaises(IndexError):
           list1.pop(5)
        with self.assertRaises(IndexError):
            list1.pop(-2)
        # testing is_empty
        self.assertFalse(list1.is_empty())
        self.assertEqual(list1.pop(), 8.0)
        self.assertTrue(list1.is_empty())
        with self.assertRaises(IndexError):
            list1.pop()
        
if __name__ == '__main__':
    unittest.main()