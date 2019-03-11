"""
    **  Recursive Pyang Dependencies **
    Created by: Rodrigo S. Tessinari
                {rodrigostange@gmail.com}
                11/03/2019
"""

import sys
from os import path
import subprocess

if __name__ == "__main__":
    root_folder = ''
    file_lst = []
    explored_lst = []
    result_dict = {}
    unexplored_lst = []

    if (len(sys.argv) < 3):
        # root_folder = path.join('/','home','sdn','yang','models','allModels')
        print("You are not doing this right. argv[1] == path to model, argv[2:] .yang list.")
        sys.exit()
    else:
        root_folder = sys.argv[1]
        file_lst = sys.argv[2:]

    unexplored_lst = file_lst.copy()

    print('input file list:',file_lst)
    while len(unexplored_lst) != 0:
        print('explored files:',explored_lst)
        print('dependency list:',unexplored_lst)
        
        command_lst = unexplored_lst.copy()
        command = 'pyang -f depend {} | cut -d : -f 2'.format(str.join(' ',command_lst))
        # print(command)
        print()

        result = str(subprocess.check_output(command, cwd=root_folder, shell=True),'utf-8')
        result_lst = result.split('\n')
        explored_lst = explored_lst + unexplored_lst[:]
        unexplored_lst.clear()
        
        for i in range(0,len(command_lst)):
            aux = result_lst[i].split(' ')
            for j in aux:
                if j != '' and j != ' ':
                    yang_file = j+".yang"
                    if yang_file not in explored_lst and yang_file not in unexplored_lst:
                        unexplored_lst.append(yang_file)
                    if command_lst[i] not in result_dict:
                        result_dict[command_lst[i]] = []
                    result_dict[command_lst[i]].append(yang_file)
        # sys.exit()

    print('Results:')
    print('input file list:',file_lst)

    print('Dependency list:')
    for key in result_dict.keys():
        print('  {}: {}'.format(key,result_dict[key]))
    print('Files needed:',explored_lst)