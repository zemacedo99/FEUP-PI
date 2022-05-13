import networkx as nx
import os
import graphviz
import matplotlib.pyplot as plt







def main():
    print("name of the dot file: ")
    file_name = input()
    dot_file = file_name + ".dot"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    graphviz.Source.from_file(dot_file)
    
    G = nx.drawing.nx_pydot.read_dot(dir_path+"/"+dot_file)
    nx.draw_networkx(G, with_labels=False)
    plt.show()
    
    
    
    
     
main()