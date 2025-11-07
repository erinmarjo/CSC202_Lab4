import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *
from math import sqrt

@dataclass(frozen = True)
class Point2:
    x : float
    y : float

## euclidean distance helper function
def euclidean(p1: Point2, p2: Point2) -> float:
    return sqrt((p2.x - p1.x)*2 + (p2.y-p1.y)*2)


class BSTTests(unittest.TestCase):
    def test_comes_before_int(self):
        self.assertTrue(comes_before(2, 7))
    def test_comes_before_int2(self):
        self.assertFalse(comes_before(3, 0))
    def test_comes_before_str(self):
        self.assertTrue(comes_before("a", "bad"))
    def test_comes_before_str2(self):
        self.assertFalse(comes_before("c", "b"))
    def test_comes_before_point(self):
        self.assertTrue(comes_before(euclidean(Point2(0,0), Point2(1,1)), euclidean(Point2(0,0), Point2(4,5))))
    def test_comes_before_point2(self):
        self.assertFalse(comes_before(euclidean(Point2(0,0), Point2(6,6)), euclidean(Point2(0,0), Point2(2,3))))
    def test_is_empty(self):
        bst = BinarySearchTree(comes_before, None)
        self.assertTrue(is_empty(bst))
    def test_is_empty2(self):
        pass


    


if (__name__ == '__main__'):
   unittest.main() 
