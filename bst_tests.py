import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *
from math import sqrt
from bst_graphs import bst_height

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
        bst = BinarySearchTree(comes_before, Node(3, 
                                                  Node(2, None, None),
                                                  None))
        self.assertFalse(is_empty(bst))
    def test_insert(self):
        bst = BinarySearchTree(comes_before, Node(3, 
                                                  Node(2, None, None),
                                                  None))
        v = 5
        bst_result = BinarySearchTree(comes_before, Node(3,
                                                         Node(2, None, None),
                                                         Node(5, None, None)))
        self.assertEqual(insert(bst, v), bst_result)
    def test_insert2(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3,
                                                       Node(1, None, None),
                                                       Node(2, None, None)),
                                                  Node(15,
                                                       Node(12, None, None),
                                                       Node(16, None, None))))
        v = 4
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3,
                                                              Node(1, None, None),
                                                              Node(2, 
                                                                   None,
                                                                   Node(4, None, None))),
                                                         Node(15,
                                                              Node(12, None, None),
                                                              Node(16, None, None))))
        self.assertEqual(insert(bst, v), bst_result)
    def test_lookup(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                    Node(3,
                                                        Node(1, None, None),
                                                        Node(2, 
                                                            None,
                                                            Node(4, None, None))),
                                                    Node(15,
                                                        Node(12, None, None),
                                                        Node(16, None, None))))
        v = 12
        self.assertTrue(lookup(bst,v))
    def test_lookup2(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                    Node(3,
                                                        Node(1, None, None),
                                                        Node(2, 
                                                            None,
                                                            Node(4, None, None))),
                                                    Node(15,
                                                        Node(12, None, None),
                                                        Node(16, None, None))))
        v = 22
        self.assertFalse(lookup(bst,v))
    '''     
    def test_delete(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                    Node(3,
                                                        Node(1, None, None),
                                                        Node(2, 
                                                            None,
                                                            Node(4, None, None))),
                                                    Node(15,
                                                        Node(12, None, None),
                                                        Node(16, None, None))))
        v = 2
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3,
                                                              Node(1, None, None),
                                                              Node(4, None, None)),
                                                         Node(15,
                                                              Node(12, None, None),
                                                              Node(16, None, None))))
        self.assertEqual(delete(bst, v), bst_result)
    '''
    def test_delete_none(self):
        bst : BinTree = None
        v = 3
        self.assertEqual(delete(bst,v), None)
    def test_delete_r_no_childre(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(15, None, None)))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3, None, None),
                                                         None))
        v = 15
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_l_no_childre(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(15, None, None)))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         None,
                                                         Node(15, None, None)))
        v = 3
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_two_children(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(15, None, None)))
        bst_result = BinarySearchTree(comes_before, Node(15,
                                                         Node(3, None, None),
                                                         None))
        v = 10
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_two_children2(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(15, 
                                                       Node(14, None, None), 
                                                       Node(16, None, None))))
        bst_result = BinarySearchTree(comes_before, Node(14,
                                                         Node(3, None, None),
                                                         Node(15,
                                                              None,
                                                              Node(16, None, None))))
        v = 10
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_two_children3(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(15, 
                                                       Node(14, None, None), 
                                                       Node(16, None, None))))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3, None, None),
                                                         Node(16,
                                                              Node(14, None, None),
                                                              None)))
        v = 15
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_one_child(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                    Node(3, None, None),
                                                    Node(16,
                                                        Node(14, None, None),
                                                        None)))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3, None, None),
                                                         Node(14, None, None)))
        v = 16
        self.assertEqual(delete(bst, v), bst_result)
    def test_delete_one_child2(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3, None, None),
                                                  Node(16,
                                                       None,
                                                       Node(14, None, None))))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3, None, None),
                                                         Node(14, None, None)))
        v = 16
        self.assertEqual(delete(bst, v), bst_result)
        
    def test_delete_one_child3(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                  Node(3,
                                                       Node(1, None, None),
                                                       Node(4,
                                                            None,
                                                            Node(5, None, None))),
                                                  Node(15,
                                                       Node(12, None, None),
                                                       Node(16, None, None))))
        bst_result = BinarySearchTree(comes_before, Node(10,
                                                         Node(3,
                                                              Node(1, None, None),
                                                              Node(5, None, None)),
                                                         Node(15,
                                                              Node(12, None, None),
                                                              Node(16, None, None))))
        v = 4
        #dtree = delete(bst, v)

       #print(bst_result, '\n\n')

        #print(dtree)
        self.assertEqual(delete(bst, v), bst_result)

    def test_bst_height(self):
        bst = BinarySearchTree(comes_before, Node(10,
                                                    Node(3,
                                                        Node(1, None, None),
                                                        Node(2, 
                                                            None,
                                                            Node(4, None, None))),
                                                    Node(15,
                                                        Node(12, None, None),
                                                        Node(16, None, None))))
        self.assertEqual(bst_height(bst), 4)


    


if (__name__ == '__main__'):
   unittest.main() 
