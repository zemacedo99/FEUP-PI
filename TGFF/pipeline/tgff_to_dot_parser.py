import utils
import pydot
import networkx
import os


def main():
    print("name of the tgff file to convert to dot: ")
    file_name = input()
    tgff_file = file_name + ".tgff"
    dot_file = file_name + ".dot"
    png_file = file_name + ".png"
    utils.clear()
    print(tgff_file)
    

    ### INPUT
    graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='yellow')

    # Add nodes
    my_node = pydot.Node('a', label='Foo')
    graph.add_node(my_node)

    # Add edges
    my_edge = pydot.Edge('a', 'b', color='blue')
    graph.add_edge(my_edge)
    
    ### OUTPUT
    
    # As a string:
    output_raw_dot = graph.to_string()
    print(output_raw_dot)
    
    # Save it as a DOT-file:
    graph.write_raw(dot_file)
    
    # Convert to a NetworkX graph:
    my_networkx_graph = networkx.drawing.nx_pydot.from_pydot(graph)
    
    dot_to_png = 'dot -Tpng ' + dot_file +' -o ' + png_file
    os.system(dot_to_png)
    
     
main()
     