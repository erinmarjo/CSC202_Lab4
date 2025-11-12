import sys
import unittest
from typing import *
from typing import Any, Callable
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 



############### Data Definitons ###################

BinTree : TypeAlias = Union["Node", None]

@dataclass(frozen = True)
class Node:
    value: Any
    left: BinTree
    right : BinTree

@dataclass(frozen = True)
class BinarySearchTree:
    fun : Callable[[Any,Any], bool]
    tree : BinTree

################ Functions ######################

#### COMES BEFORE ####

## determine if one value comes before another
def comes_before(prim: Any, sec: Any) -> bool:
    if prim < sec:
        return True
    else:
        return False

#### IS EMPTY ####

## determine if BST is empty or not
def is_empty(bst: BinarySearchTree) -> bool:
    match bst:
        case BinarySearchTree(_, tree):
            '''return tree is None''' # another way of writing the next four lines
            if tree is None:
                return True
            else:
                return False
        


#### INSERT ####

## insert helper function
def insert_helper(t: BinTree, val: Any, lt: Callable[[Any, Any], bool]) -> BinTree:
    if t is None:
        return Node(val, None, None)
    elif lt(val, t.value):
        return Node(t.value, insert_helper(t.left, val, lt), t.right)
    else:
        return Node(t.value, t.left, insert_helper(t.right, val, lt))

## insert value into BinarySearchTree
def insert(bst: BinarySearchTree, val : Any) -> BinarySearchTree:
    return BinarySearchTree(bst.fun, insert_helper(bst.tree, val, bst.fun))


#### LOOKUP ####

## lookup helper function

def is_equal(a: Any, b: Any, lt: Callable[[Any, Any], bool]) -> bool:
    return (not lt(a,b)) and (not lt(b, a))

def lookup_helper(t: BinTree, val: Any, lt: Callable[[Any, Any], bool]) -> bool:
    if t is None:
        return False
    elif is_equal(val, t.value, lt):
        return True
    elif lt(val, t.value):
        return lookup_helper(t.left, val, lt)
    else:
        return lookup_helper(t.right, val, lt)

## determine if value is stored in a BinarySearchTree
def lookup(bst: BinarySearchTree, val: Any) -> bool:
    return lookup_helper(bst.tree, val, bst.fun)


#### DELETE ####

## delete helper function
def delete_helper(t: BinTree, val : Any, lt: Callable[[Any, Any], bool]) -> BinTree:
    if t is None:
        return None
    elif (not lt(val, t.value)) and (not lt(t.value, val)):
        
        if t.left is None and t.right is None: # no children
            return None
        elif t.left is None:                   # R child
            return t.right
        elif t.right is None:                  # L child
            return t.left
        
        smallest_node = t.right                # two children
        
        while smallest_node.left is not None:
            smallest_node = smallest_node.left
        
        current_right = delete_helper(t.right, smallest_node.value, lt)
        
        return Node(smallest_node.value, t.left, current_right)
    
    elif lt(val, t.value):
        return Node(t.value, delete_helper(t.left, val, lt), t.right)
    else:
        return Node(t.value, t.left, delete_helper(t.right, val, lt))

## remove value from BinarySearchTree; keep BST properties

def delete(bst: Optional[BinarySearchTree], val: Any) -> Optional[BinarySearchTree]:
    if bst is None:
        return None
    return BinarySearchTree(bst.fun, delete_helper(bst.tree, val, bst.fun))


########### TESTS ##########
## tests for `bst.py` are located in `bst_tests.py`