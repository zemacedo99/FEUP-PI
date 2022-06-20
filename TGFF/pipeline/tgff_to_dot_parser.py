import utils
import pydot
import networkx
import os

graph = None

def add_task(task_details):
    task_dets=task_details.split()
    #print(task_dets)
    #my_node = pydot.Node(task_dets[0],type = int(task_dets[2]),host = int(task_dets[4]))
    #create a new task with      :name       ,type          ,host
    #my_node = pydot.Node(task_dets[0],type = int(task_dets[2]))
    my_node = pydot.Node(task_dets[0], Hardware = float(task_dets[4]),Software = float(task_dets[6]))
    graph.add_node(my_node)
def add_arc(arc_details):
    arc_dets=arc_details.split()
    #print(arc_dets)
    my_edge = pydot.Edge(src=arc_dets[2],dst=arc_dets[4],name= arc_dets[0],type=arc_dets[6])
    #create a new arc with    :name       ,pe_from    ,pe_to      ,type
    #my_edge = pydot.Edge(src=arc_dets[2],dst=arc_dets[4],weight=arc_dets[6])

    graph.add_edge(my_edge)

def add_row(row):
    #print(row)
    row_values=[]
    for i in row.split():
        row_values.append(float(i))
    print(row_values)
        
def get_blocks(input_file):
    buf=[]
    for line in input_file:
        if line and line.strip() and line.startswith("@"):
            buf =[]
            buf.append(line.strip())
            if not line.strip().endswith("{"):
                yield buf
                buf = []
        elif line and line.strip() and line.startswith("}"):
            yield buf
        elif line and line.strip():
            buf.append(line.strip())


def process_block(block):
    global graph

    tg_name = None
    period = None
    
    if "HYPERPERIOD" in block[0]:
        hyperperiod= float(block[0].strip('@HYPERPERIOD '))
    
    elif "PE" in block[0]:
        #TODO: Parse tables
        core_name = None
        i = 0
        core_name= block[0].strip('@').strip('{')
        #print(core_name)
        #print(block[1].strip('#'))
        #print(block[2].strip('#'))
        #print(block[4].strip('#'))
        #create table
        for i in range(5, len(block)):
            if not block[i].startswith('#'):
                #add_row to table
                tablerow = block[i]
                add_row(tablerow)
                
    else:
        #Parse Tasks
        for line in block:
            if line.startswith("@"):
                tg_name = line.strip('@').strip('{')
                graph = pydot.Dot(tg_name, graph_type='graph')
                #print(tg_name)
            elif line.startswith("PERIOD"):
                period = float(line.strip(' PERIOD'))
                print(period)
                break
        for line in block:
            if line.startswith("TASK"):
                task = line.strip('TASK ')
                add_task(task)
            elif line.startswith("ARC"):
                arc = line.strip('ARC ')
                add_arc(arc)
            elif line.startswith("SOFT_DEADLINE"):
                temp = line.strip('SOFT_DEADLINE ')
                print(temp)
            elif line.startswith("HARD_DEADLINE"):
                temp = line.strip('HARD_DEADLINE ')
                print(temp)




def main():
    print("name of the tgff file to convert to dot: ")
    file_name = input()
    tgff_file = file_name + ".tgff"
    dot_file = file_name + ".dot"
    png_file = file_name + ".png"
    utils.clear()
    #print(tgff_file)
    
    
    global graph
    
    
    
    with open(tgff_file) as input_file:
        for block in get_blocks(input_file):
            process_block(block)
            
     
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