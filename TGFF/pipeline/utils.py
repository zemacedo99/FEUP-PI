import os
import argparse

def clear():
    os.system('cls')
    os.system('clear')
    
def init_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-basic',action='store_true', dest='basic_command', help='Basic commands')
    parser.add_argument('-task', action='store_true', dest='task_graph_generation', help='Task graph generation')
        
    return parser