import os
import sys
import utils


def main():
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    option = 0;
    while option != 3:
        option = main_menu()
        
        if option == '1':
            parser = utils.init_args_parser()
            parser.print_help()
            print("\ninput the parameters wanted separated with spaces: ")
            parameters = input()
            create_graph = 'python3 '+ dir_path + '/create_graph.py ' + parameters
            os.system(create_graph)
        
        elif option == '2':
            tgff_dir = "~/Documents/PI/TGFF/tgff-3.6/tgff "

            print("name of the tgffopt file: ")
            tgffopt_file_name = input()
            tgffopt_file = dir_path + '/'+ tgffopt_file_name
            
            tgffopt_to_tgff = tgff_dir + tgffopt_file
            os.system(tgffopt_to_tgff)
            utils.clear()
            print(tgffopt_file_name +".tgff created")
            
        elif option == '3':
            tgff_to_dot_parser = 'python3 '+ dir_path + '/tgff_to_dot_parser.py '
            os.system(tgff_to_dot_parser)
        
        else:
            print("Wrong option selection. Pls choose a valid option.")
    
      
def main_menu():       
    print ("\n" + 30 * "-" , "MENU" , 30 * "-")
    print ("1. Create TGFFOPT file")
    print ("2. Create TGFF file from TGFFOPT file")
    print ("3. Create DOT file from TGFF file")
    print ("4. Exit")
    print (67 * "-" )
    option = input("Enter your choice [1-4]: ")
    utils.clear()
    if option == '4':
        print("Pipeline Closed")
        sys.exit(1)
    return option
    


  
main()
     