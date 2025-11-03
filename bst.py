import sys
import unittest
from typing import *
from typing import Any, Callables
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 



############### Data Definitons ###################

BinTree : TypeAlias = Union["Node", None]

@dataclass(frozen = True)
class Node:
    first: Any
    rest: BinTree

@dataclass(frozen = True)
class BinarySearchTree:
    fun : "comes_before"
    tree : BinTree

############ Functions ######################


## determine if one value comes before another
def comes_before(prim: int, sec: int) -> bool:
    pass