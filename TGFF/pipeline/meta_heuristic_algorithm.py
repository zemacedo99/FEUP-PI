import random
import time
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

    start_time = time.time()
    solution,history = simulated_annealing(G,list)
    end_time = time.time()
    
    indexOfSolution = list.index(solution)
    print('Time Elapsed:', end_time-start_time)
    print("Solution "+str(solution))
    print("Index of Solution: " + str(indexOfSolution))
    print("Time of Solution: " + str(getCost(G,list[indexOfSolution])))

    plt.scatter(indexOfSolution,getCost(G,list[indexOfSolution]),marker='X',s=200,color = '#000000')
    plotCosts(G,list)
    plotHistory(G,list,history)
    plt.show()
    
    
    
def plotCosts(G,list):
    costList = []
    for i in range(0,len(list)):
        cost = getCost(G,list[i])
        costList.append(cost)
        

    x = np.arange(0, len(list)) 
    y = np.array(costList)

    plt.plot(x,y,alpha=0.8) 
    return costList

def plotHistory(G,list,history):
    historyCost = []
    for i in range(0,len(history)):
        cost = getCost(G,list[history[i]])
        historyCost.append(cost)
        

    xHistory= np.array(history)
    yHistory = np.array(historyCost)
    
    plt.plot(xHistory,yHistory,alpha=0.5)
    
    return historyCost

def generate(lenght):
    list = []
    for combinations in itertools.product([0, 1], repeat=lenght):
        list.append(combinations)

    return list
    
    
def getCost(graph,state):
    
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

def getNeighbors(list,current_state):
    
    neighbors = []
    
    
    index = list.index(current_state)

    
    if(index != 0):
        neighbors.append(list[index-1])
    else:
        neighbors.append(list[index])
        
    if(index != len(list)):
        neighbors.append(list[index+1])
    else:
        neighbors.append(list[index])
    
            
    return neighbors



def simulated_annealing(graph,list):
    """Peforms simulated annealing to find a solution"""
    current_temp = 1000
    final_temp = 0.1
    alpha = 0.9


    # Start by initializing the current state with the initial state
    current_state = random.choice(list)
    solution = current_state
    history = [list.index(current_state)]

    while current_temp > final_temp:

        #neighbor = random.choice(getNeighbors(list,current_state))
        neighbor = random.choice(list)

        # Check if neighbor is best so far
        current_value = getCost(graph,current_state)
        neighbor_value = getCost(graph,neighbor)
        cost_diff = current_value - neighbor_value

        # if the new solution is better, accept it
        if cost_diff > 0:
            solution = neighbor
            
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            n_random = np.random.rand()
            E = -abs(neighbor_value-current_value) # E<0
            p_accept = np.exp(E/current_temp)
            
            if n_random < p_accept: #if random.uniform(0, 1) < math.exp(cost_diff / current_temp):
                solution = neighbor
                
            # else: do nothing, keep iterating
           
        # decrement the temperature
        current_temp *= alpha
        history.append(list.index(solution))
        
        

    return solution,history



main()
    
    
#https://dev.to/cesarwbr/how-to-implement-simulated-annealing-algorithm-in-python-4gid