"""
    ** Code to TXT **
    Created by: Rodrigo S. Tessinari
                {rodrigostange@gmail.com}
                24/10/2018
"""

import sys
from os import walk

def run(root_folder):
    num_dir = 0
    num_files = 0
    fail_flag = False

    try:
        open('missing_files.txt','w')
    except:
        print('Could not open file... this is odd.')

    with open('result.txt', 'w+') as resultFile:    
        for (dirpath, dirnames, filenames) in walk(root_folder):
            num_dir = num_dir + len(dirnames)
            num_files = num_files + len(filenames)

            resultFile.write('Pasta ' + dirpath + '\n\n')
            for file in filenames:
                try:
                    with open(dirpath+'\\'+file) as data:
                        resultFile.write("Arquivo \'%s\':\n%s\n" % (file,data.read()))
                except:
                    with open('missing_files.txt','a') as missingFiles:
                        missingFiles.write(dirpath+'\\'+file)
                        fail_flag = True

            resultFile.write('\n')
    if fail_flag:
        print('Failed to open the following files:')
        try:
            with open('missing_files.txt','r') as missingFiles:
                print(missingFiles.read())
        except:
            print('Could not open \'missing_files.txt\'... this is odd.')
    else:
        print('All folders read =)')

if __name__ == "__main__":
    root_folder = ''
    if (len(sys.argv) != 2):
        root_folder = 'C:\\Users\\rodri\\Desktop\\elastico\\src'
        print("You did not choose a folder.")
    else:
        root_folder = sys.argv[1]
    print("Using \"%s\" as root folder." % (root_folder))
    
    run(root_folder)
    
    print('Job done.')