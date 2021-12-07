import copy
import time
import csv
import numpy as np

def menu():
    print('Project 2: CS170 Feature Classification - Brayan Montiel\n')

    #test data - change when testing assigned small-19 and large-13: 
    testSmall = 'CS170/Project2/testdata/Ver_2_CS170_Fall_2021_Small_data__86.txt'
    testLarge = 'CS170/Project2/testdata/Ver_2_CS170_Fall_2021_LARGE_data__27.txt'

    #choose which dataset to run - assuming no incorrect user input
    filePick = input('\nPlease select a dataset to run: \n'
                     '1) Small dataset: Ver_2_CS170_Fall_2021_Small_data__86.txt \n'
                     '2) Large dataset: Ver_2_CS170_Fall_2021_LARGE_data__27.txt \n'
                     'Enter choice: ')
    filePick = int(filePick)

    if(filePick == 1):      #small dataset
        try:
            data = np.genfromtxt(testSmall)
            print('You picked: ' + testSmall + ' \n')
        except:
            print('File ' + testLarge + ' not found.')
    else:                   #large dataset
        try:
            data = np.genfromtxt(testLarge)
            print('You picked: ' + testLarge + ' \n')
        except:
            print('File ' + testLarge + ' not found.')
    dataFeatures = data.shape[1]-1
    dataInstances = data.shape[0]
    print('This dataset has', dataFeatures ,' features (not including the class attribute), with ', dataInstances ,' instances.\n')

    algoPick = input('Type the number of the algorithm you want to run.\n' +
                        '1) Forward Selection\n' +
                        '2) Backward Elimination\n')
    algoPick = int(algoPick)
    print(algoPick)
#MAIN DRIVER#
if __name__ == "__main__":
    menu()