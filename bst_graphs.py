import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *
import time


TREES_PER_RUN : int = 10000

## generate BinarySearchTree with n random floats in [0,]
def random_tree(n : int) -> BinarySearchTree:
    bst = BinarySearchTree(comes_before, None)
    for _ in range(n):
        val = random.random()
        bst = insert(bst, val)
    return bst

## helper code to find height of BST
def bst_height(bst: BinarySearchTree) -> Any:
    if bst.tree is None:
        return None
    else:
        L_height = bst_height(bst.tree.left)
        R_height = bst_height(bst.tree.right)
        return 1 + max(L_height, R_height)


## find n_max that is 1.5-2.5 seconds
'''
start_ranndom_tree = time.perf_counter()

result_random_tree = random_tree(1200)

stop_random_tree = time.perf_counter()

time_range = print("rt for random tree func= ", stop_random_tree - start_ranndom_tree)
'''
## loop this
def pcounter_exp(n : int):
    start_ranndom_tree = time.perf_counter()
    for _ in range(TREES_PER_RUN):
        random_tree(n)
    stop_random_tree = time.perf_counter()
    time_range = stop_random_tree - start_ranndom_tree
    print("time elapsed = ", time_range)

pcounter_exp(50)

## below is graphing example
'''
def example_graph_creation() -> None:
    pass # Return log-base-2 of 'x' + 5.
    def f_to_graph (x : float) -> float:
        return math.log2( x ) + 5.0
    # here we're using "list comprehensions": more of Python's  
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]


    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )


    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()


 
if (__name__ == '__main__'):
    example_graph_creation()
'''