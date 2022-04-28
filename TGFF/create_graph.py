import argparse

# TODO : ErrorHandling
# TODO: Parameters Type Checking

def main():
     
     parser = argparse.ArgumentParser(description='Help')
     parser.add_argument('-basic',action='store_true', dest='basic_command', help='Basic commands')
     parser.add_argument('-task', action='store_true', dest='task_graph_generation', help='Task graph generation')

     args = parser.parse_args()
     print("Basic commads: "+ str(args.basic_command))
     print("Task graph generation commads: " + str(args.task_graph_generation))


     f = open("demofile.tgffopt", "w")
     
     if(args.basic_command):
          print("Give the seed for the pseudo-random number generator")
          seed = input()
          f.write("seed " + seed)
          f.write("\n")
          
     if(args.task_graph_generation):
          print("Give the number of task graphs to generate")
          tg_cnt = input()
          
          print("Give the (case dependent) label used for task graphs.")
          tg_label = input()
          
          print("(default 0) Give the start index for named task graph.")
          tg_offset = input()
          
          print("Give the minimum number of tasks per task graph (average, multiplier).")
          task_cnt = input()
          
          print("Give the number of possible transmit types")
          trans_type_cnt = input()
          
          print("Give the multipliers for periods in multi-rate systems.")
          period_mul = input()
          
          print("(default 1.0) Give the probability that a graph is periodic.")
          prob_periodic = input()
          
          print("(default 0.0) Give the probability that a graph has more than one start node.")
          prob_multi_start_nodes = input()
          
          print("Give the number of start nodes for graphs which have multiple start nodes (average,multiplier).")
          start_node = input()
          
          f.write("tg_cnt " + tg_cnt)
          f.write("\n")
          f.write("tg_label " + tg_label)
          f.write("\n")
          f.write("tg_offset " + tg_offset)
          f.write("\n")
          f.write("task_cnt " + task_cnt)
          f.write("\n")
          f.write("trans_type_cnt " + trans_type_cnt)
          f.write("\n")
          f.write("period_mul " + period_mul)
          f.write("\n")
          f.write("prob_periodic " + prob_periodic)
          f.write("\n")
          f.write("prob_multi_start_nodes " + prob_multi_start_nodes)
          f.write("\n")
          f.write("start_node " + start_node)
          f.write("\n")
     

     f.close()

     #open and read the file
     f = open("demofile.tgffopt", "r")
     print(f.read())
     
     
main()
     