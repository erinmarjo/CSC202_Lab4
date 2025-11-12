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

## find n_max that is 1.5-2.5 seconds for `random_tree()` and for `insert()`

## find nmax for random_tree
def pcounter_exp(n : int):
    start_ranndom_tree = time.perf_counter()
    for _ in range(TREES_PER_RUN):
        random_tree(n)
    stop_random_tree = time.perf_counter()
    time_range = stop_random_tree - start_ranndom_tree
    print("time elapsed = ", time_range)

## probably some way to to write a function to find this, but for now
## trial and error here. Start with 25
#pcounter_exp(60) ## n = 50 runs in about 1.7-1.8 second each time


## find average time to insert something into bst in seconds
def avg_time_insert(n: int) -> float:
    total_time = 0.0
    for _ in range(TREES_PER_RUN):
        bst = random_tree(n)
        val = random.random()
        start = time.perf_counter()
        insert(bst, val)
        end = time.perf_counter()
        total_time +=(end-start)
    return total_time/TREES_PER_RUN

## find nmax for insert
def n_max_insert() -> int:
    n = 10
    while True:
        start = time.perf_counter()
        for _ in range(TREES_PER_RUN):
            bst = random_tree(n)
            val = random.random()
            insert(bst, val)
        elapsed = time.perf_counter() - start
        print(f"n={n}, time = {elapsed:.2f}s")
        if 1.5 <= elapsed <= 2.5:
            print(f"max = {n}")
            return n
        n +=10

#n_max_insert() # n = 50 is between 1.5 and 2.5

########### AVERAGE HEIGHT OF TREE GRAPH ################
''' take out comment to make graphs
def avg_tree_height_graph(n_max: int) -> None:
    x_coords : List[int] = [int(x) for x in np.linspace(0, n_max, 50)]
    y_coords : List[float] = [avg_height(n) for n in x_coords]
    x_numpy : np.ndarray = np.array(x_coords)
    y_numpy : np.ndarray = np.array(y_coords)

    plt.plot(x_numpy, y_numpy, label = "Average Tree Height")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Tree Height")
    plt.title("Graph of Average BST Tree Heights")
    plt.grid(True)
    plt.legend()
    plt.show()

def avg_time_insert_graph(n_max: int) -> None:
    x_coords : List[int] = [int(x) for x in np.linspace(0, n_max, 50)]
    y_coords : List[float] = [avg_time_insert(n) for n in x_coords]

    x_numpy : np.ndarray = np.array(x_coords)
    y_numpy : np.ndarray = np.array(y_coords)

    plt.plot(x_numpy, y_numpy, label = "Average Time to Insert")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time to Insert Random Value (s)")
    plt.title("Average Insert Time")
    plt.grid(True)
    plt.legend()
    plt.show()

if (__name__ == '__main__'):
    avg_tree_height_graph(50)
    avg_time_insert_graph(50)

'''