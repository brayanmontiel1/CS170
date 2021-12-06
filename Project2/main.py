import copy
import time
import csv

def menu():
    print('Project 2: CS170 Feature Classification - Brayan Montiel\n')
    #test data - change when testing assigned small-19 and large-13: 
    testSmall = 'CS170/Project2/testdata/Ver_2_CS170_Fall_2021_Small_data__86.txt'
    testLarge = 'CS170/Project2/testdata/Ver_2_CS170_Fall_2021_LARGE_data__27.txt'

    #choose which algorithm - assuming no incorrect user input
    filePick = input('\nPlease select a dataset to run: \n'
                     '1) Small dataset: Ver_2_CS170_Fall_2021_Small_data__86.txt \n'
                     '2) Large dataset: Ver_2_CS170_Fall_2021_LARGE_data__27.txt \n'
                     'Enter choice: ')
    filePick = int(filePick)

    if(filePick == 1):
        try:
            data = open(testSmall, 'r')
        except:
            print('File ' + testLarge + ' not found.')
    else:
        try:
            data = open(testLarge, 'r')
        except:
            print('File ' + testLarge + ' not found.')

    
    dataInstances = sum(1 for i in data)                #amount of rows in dataset 
    data.seek(0)                                        #reset data
    dataFeatures = len(data.readline().split()) - 1     #columns - 1
    #print message 
    print('This dataset has ', dataFeatures,
        ' features (not including the class attribute), with ', dataInstances, '.')

#MAIN DRIVER#
if __name__ == "__main__":
    menu()