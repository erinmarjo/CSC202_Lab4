import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *


class BSTTests(unittest.TestCase):
    def test_comes_before(self):
        self.assertTrue(comes_before(2, 7))
    def test_comes_befoe2(self):
        self.assertFalse(comes_before(3, 0))
    def test_is_empty(self):
        bst = BinarySearchTree(comes_before, None)
        self.assertTrue(is_empty(bst))
    def test_is_empty2(self):
        pass


    


if (__name__ == '__main__'):
   unittest.main() 
