import random
from networkx.algorithms import approximation as approx
import networkx as nx
import os
import graphviz
import matplotlib.pyplot as plt
import math
import itertools
import numpy as np




def main():
    print("name of the dot file: ")
    file_name = input()
    dot_file = file_name + ".dot"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    graphviz.Source.from_file(dot_file)
    
    G = nx.drawing.nx_pydot.read_dot(dir_path+"/"+dot_file)
    #nx.draw_networkx(G, with_labels=False)
    #plt.show()
    
    #print(G.nodes.data())
    #for node in G.nodes:
        #print("\nNode name: " + node)
        #print("Hardware time: " + G.nodes[node]['Hardware'])
        #print("Software time: " + G.nodes[node]['Software'])
    
    #print(G.edges.data())
    
    #for source, target in G.edges():
        #print("\nEdge name: " + G[source][target][0]['name'])
        #G[source][target][0]['weight'] = random.randint(0, 1000) 
        #print("Edge weight: " + str(G[source][target][0]['weight']))
        
    list = generate(G.number_of_nodes())


    plotCosts(G,list)
    
        
    
    
def plotCosts(G,list):
    costList = []
    for i in range(0,len(list)):
        cost = getCost(G,list[i])
        costList.append(cost)
        

    x = np.arange(0, len(list)) 
    y = np.array(costList)

    plt.plot(x,y) 
    plt.show()
    
    return costList

def generate(lenght):
    list = []
    for combinations in itertools.product([0, 1], repeat=lenght):
        list.append(combinations)

    return list
    
    
def getCost(graph,state):
    
    #for value in state:
    count = -1
    sum = 0
    for node in graph.nodes:
        count = count + 1
        if(state[count] == 0):
            #print("Software time: " + graph.nodes[node]['Software'])
            sum = sum + float(graph.nodes[node]['Software'])
        else:
            #print("Hardware time: " + graph.nodes[node]['Hardware'])
            sum = sum + float(graph.nodes[node]['Hardware'])
            
        
        
    return sum
    
main()
    
    
#https://dev.to/cesarwbr/how-to-implement-simulated-annealing-algorithm-in-python-4gid