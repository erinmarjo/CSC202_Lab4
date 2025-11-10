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
def bst_height(bst:BinarySearchTree) -> int:
    def node_height(node: BinTree) -> int:
        if node is None:
            return 0
        return 1 + max(node_height(node.left), node_height(node.right))
    return node_height(bst.tree)

## helper code to find average tree height for n
def avg_height(n):
    total = 0
    for _ in range(TREES_PER_RUN):
        bst = random_tree(n)
        total += bst_height(bst)
    return total/TREES_PER_RUN

## find n_max that is 1.5-2.5 seconds

## loop this
def pcounter_exp(n : int):
    start_ranndom_tree = time.perf_counter()
    for _ in range(TREES_PER_RUN):
        random_tree(n)
    stop_random_tree = time.perf_counter()
    time_range = stop_random_tree - start_ranndom_tree
    print("time elapsed = ", time_range)

pcounter_exp(60) ## n = 50 runs in about 1.7-1.8 second each time

########### AVERAGE HEIGHT OF TREE GRAPH ################

def avg_tree_height_graph(n_max: int) -> None:
    x_coords : List[int] = [int(x) for x in np.linspace(0, n_max, 50)]
    y_coords : List[float] = [avg_height(n) for n in x_coords]
    x_numpy : np.ndarray = np.array(x_coords)
    y_numpy : np.ndarray = np.array(y_coords)

    plt.plot(x_numpy, y_numpy, label = "Average Tree Height")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graph of Average BST Tree Heights")
    plt.grid(True)
    plt.legend()
    plt.show()

if (__name__ == '__main__'):
    avg_tree_height_graph(50)
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