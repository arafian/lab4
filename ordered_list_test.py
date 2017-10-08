# Arman Rafian
# Section 7

import unittest
from ordered_list import *

class test_ordered_list(unittest.TestCase):
    def test_repr(self):
        list1 = OrderedList()
        list1.add(5)
        list1.add(3)
        list1.add(-22.5)
        self.assertEqual(repr(list1), [4, 3, -22.5])
        n1 = Node(5)
        self.assertEqual(repr(n1), (5, None))
        n2 = Node(-3)
        n1.next = n2
        self.assertEqual(repr(n1), (5, n2))
        
    def test_add(self):
        list1 = OrderedList()
        self.assertTrue(list1.is_empty)
        self.assertEqual(list1.size(), 0)
        with self.assertRaises(IndexError):
            list1.pop()
        self.assertEqual(list1.index(1), -1)
        list1.add(5)
        list1.add(-13.57)
        self.assertFalse(list1.search_forward(-13.5))
        list1.add(8.0)
        self.assertTrue(list1.search_backward(5))
        self.assertEqual(list1.remove(-13.57) 1)
        # only two values should be left
        self.assertEqual(repr(list1), [5, 8.0])
        list1.add(0)
        list1.add(10223)
        iist1.add(-0.05)
        # added 2 + 3 = 5
        self.assertEqual(list1.size(), 5)
        self.assertEqual(list1.index(10223), 4)
        self.assertTrue(list1.search_backward(0))
        self.assertFalse(list1.is_empty())
        # remove from front
        self.assertEqual(list1.remove(5), 0)
        # remove from back updated list
        self.assertEqual(list1.remove(-0.05), 3)
        self.assertEqual(list1.index(8.0), 0)
        self.assertEqual(list1.index(50), -1)
        self.assertEqual(list1.pop(2), 10223)
        self.assertEqual(list1.pop(), 0)
        with self.assertRaises(IndexError):
            list1.pop(3)
        self.assertFalse(list1.is_empty)
        self.assertEqual(list1.pop(), 8.0)
        self.assertTrue(list1.is_empty)