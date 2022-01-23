from collections import defaultdict
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from treelib import Node, Tree

graph=defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges=[]
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

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

for i in range(len(fn)):
    if fn[n]==n:
        print(addEdge(fn, fn[n], n))

print(generate_edges(fn))

#Generate graph edges DataFrame.
index=pd.MultiIndex.from_tuples(generate_edges(fn))
df=pd.MultiIndex.from_tuples(generate_edges(fn))
df=pd.DataFrame(generate_edges(fn), index=index)
print(df)
    
G=nx.Graph()
G=nx.from_pandas_edgelist(df, 0, 1)
nx.draw_shell(G, with_labels=True)
plt.show()