import copy
import time
import os
import numpy as panda
from operator import itemgetter
from collections import Counter

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
            data = panda.genfromtxt(testSmall)
            print('You picked: ' + testSmall + ' \n')
        except:
            print('File ' + testLarge + ' not found.')
    else:                   #large dataset
        try:
            data = panda.genfromtxt(testLarge)
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
    print('Okay lets run option #',algoPick)
    accuracy = leave_one_out_x_valid(data)
    print('Running nearest neighbor with all ', dataFeatures ,' features, using \"leaving-one-out\" evalutation, I get an accuracy of ',accuracy,'.\n')
   

def leave_one_out_x_valid(data):            #performs leave out out validation, gets accuracy
    val = []        #values from nearest neighbors
    for i in range(len(data)):          #loop through data to clean exp
        tempData = []
        data_arr = data[i]              
        data_arr = data_arr[1:]
        #normalize dataset
        if(i == 0):                 
            tempData = data[1:]
        elif(i == (len(data)-1)):   
            tempData =  data[:i]
        else:
            tempData = panda.concatenate((data[:i],data[i+1:]), axis=0)
        classTemp = [i[0] for i in tempData]
        tempData = panda.delete(tempData, 0, axis=1) # 0 out column 
        results = nearestNeighbor(data_arr, tempData, classTemp) ##data, current set, feature to add
        val.append(results)             #put results in val[]
    classType = [i[0] for i in data]    #puts classifier in array 
    accResutls = accuracy(val, classType)   #get accuracy of results
    return accResutls


def accuracy(values, classType):        #calculates accuracy of leave one out
    count = 0
    for i,j in zip(values, classType):
        if(i == j):
            count +=1
    result = (count/len(classType)) * 100
    return result


def nearestNeighbor(data, current_set, classifications):    #returns nearest neighbors list
    nearest = []    #nearest neighbor arr
    distance = []   #distance arr
    count = 0
    total = 0
    for i in current_set:               #loop through current_set
        for j,k in zip(i,data):         #loop , zip can make it easier to go through and find k distance 
            countDist = abs(j-k)**2     #calculate distance
            total += countDist
        total**(1/2)                          
        distance.append((total,classifications[count]))
        count +=1  
    distance = sorted(distance, key=itemgetter(0))
    k_dist = [a[1] for a in distance[:1]]           #get first column 

    k_dist = list(Counter(k_dist).keys())
    nearest.append(k_dist[0])
    return nearest

if __name__ == "__main__":
    menu()