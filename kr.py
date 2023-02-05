#!/bin/python3
import heapq
from heapq import heappush

import matplotlib.pyplot as plt
import networkx as nx

filepath = './lin01.stp'

'''
lists for getting info from Stp File
'''

list_f= list()
list_t= list()
list_P= list()

'heap for sorting'
my_heap = []

'list of the terminal node==> for KMP Implementation'
terminx=[]

'#node'
nodes=set()

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   i=0

   while line:
      # if line is Empty:
      if not line.strip():
        line = fp.readline()
      else:
      
         #print("Line {}: {}".format(cnt, line.strip()))
         #l=line.strip()
         info=line.split()

#getting the edges


         if(info[0]=='E'):
           #print("ouii")

           list_f.insert(i,int(info[1]))
           list_t.insert(i,int(info[2]))
           list_P.insert(i,int(info[3]))
           heappush(my_heap, (int(info[3]), int(info[1]), int(info[2]))) # push to the heap
           #a = int(info[3])

           #addling node to the set
           nodes.add(int(info[1]))
           nodes.add(int(info[2]))
           
           #heappush(my_heap2,a )
           #print(list_t[i])
           #print("from {} to {} pides= {}".format(list_f[i],list_t[i],list_P[i]))
           i=i+1


#getting the terminals
       
         if(info[0]=='T'):
           terminx.append(info[1])
           

         line = fp.readline()
        



print("------------------------------------------------^ heap sort------------------------------------ ")

print("the terminal== ",terminx)
print("theheap==",my_heap)



#####################
##################
#Kruskal



parent = {}
# perform MakeSet operation
def makeSet(universe):
        # create `n` disjoint sets (one for each item)
        for i in universe:
            parent[i] = i

    # Find the root of the set in which element `k` belongs
def Find(k):
        # if `k` is root
        if parent[k] == k:
            return k

        #      recur for the parent until we find the root
        return Find(parent[k])

    # Perform Union of two subsets
def Union(a, b):
        # find the root of the sets in which elements
        #
        x = Find(a)
        y = Find(b)

        parent[x] = y
########### going t --> kruskalll

def node():
 return nodes
G = nx.Graph()
def mkr():
    print('kruskal main')
    #dis=DisjointSet()
    makeSet(node())

    i=0
    for _ in range(len(my_heap)):

         popp=list()
         popp=heapq.heappop(my_heap)
         

         if Find(popp[1])!=Find(popp[2]):
         	#print('not have the same parent')
         	Union(popp[1],popp[2])
                   
         	G.add_node(popp[1])
         	G.add_node(popp[2])
         	G.add_edge(popp[1], popp[2], weight=popp[0])
         	i+=1

   
   
### drwaing the graph



    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 10]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 10]
    pos = nx.spring_layout(G, seed=7)
    nx.draw_networkx_nodes(G, pos, node_size=700,)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    print(list(nx.connected_components(G)))
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


mkr()








