from collections import defaultdict
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from treelib import Node, Tree

S = []
fn={}
N=[]
M=input('Input a bound: ')
M=int(M)
for x in range(1,M+1):
    N.append(x)
    n=x
    fn[n]=N
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            N.append(n)
        elif n % 2 == 1:
            n = 3 * n + 1
            N.append(n)
        i = i + 1
    N=[]
    S.append(i)
    
print('fn=', fn)

sn={}
for n in fn:
    sn[n]=len(fn[n])
print('sn=', sn)
