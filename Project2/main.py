import time
import numpy as panda
from operator import itemgetter
from collections import Counter

def menu():
    print('Project 2: CS170 Feature Classification - Brayan Montiel\n')

    #shortcut paths for assigned files 
    small19 = './Ver_2_CS170_Fall_2021_Small_data__19.txt'
    large13 = './Ver_2_CS170_Fall_2021_LARGE_data__13.txt'

    #choose which dataset to run - assuming no incorrect user input
    fileName = input('\nType in the name of the file to test : ')
    
    data = panda.genfromtxt(fileName)
    print('You entered: ' + fileName + ' \n')

    algoPick = input('Pick the algorithm you want to run.\n' +
                        '1) Forward Selection\n' +
                        '2) Backward Elimination\n')    #assumes no wrong input from user
    
    algoPick = int(algoPick)
    dataFeatures = data.shape[1]-1
    dataInstances = data.shape[0]
    print('This dataset has', dataFeatures ,' features (not including the class attribute), with ', dataInstances ,' instances.\n')

    if(algoPick == 1):           #run forward selection
        print('Okay lets run Forward Selection')        
        accuracy = leave_one_out_x_valid(data)
        print('Running nearest neighbor with all ', dataFeatures ,' features, using \"leaving-one-out\" evaluation, I get an accuracy of ',round(accuracy,2),'%.\n')
        print('Beginning search.')
        start = time.time()
        forwardSelection(data)
        finish = time.time()
        print('Total run Forward Selection runtime: ', (finish-start))

    elif(algoPick == 2):        #run backward elimination
        print('Okay lets run Backward Elimination')       
        accuracy = leave_one_out_x_valid(data)
        print('Running nearest neighbor with all ', dataFeatures ,' features, using \"leaving-one-out\" evaluation, I get an accuracy of ',round(accuracy,2),'%.\n')
        start = time.time()
        backwardElimination(data)
        finish = time.time()
        print('Total run Backward Elimination runtime: ', (finish-start))


def leave_one_out_x_valid(data):            #performs leave out out validation, gets accuracy
    val = []        #values from nearest neighbors
    classType = [i[0] for i in data]    #puts classifier in array 
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

    accResutls = accuracy(val, classType)   #get accuracy of results
    return accResutls


def accuracy(val, classType):        #calculates accuracy of leave one out
    count = 0
    for i,j in zip(val, classType):
        if(i == j):
            count +=1
    result = (count/len(classType)) * 100
    return result

def nearestNeighbor(data, current_set, classType):    #returns nearest neighbors list
    nearest = []    #nearest neighbor arr
    k_dist = nearestNeighborHelper(data,current_set,classType)
    counter = list(Counter(k_dist).keys())
    nearest.append(counter[0])
    return nearest

def nearestNeighborHelper(data,current_set,classType):
    distance = []   #distance arr
    count = 0
    for i in current_set:               #loop through current_set
        totalDist = dist(i,data)              
        distance.append((totalDist,classType[count]))
        count +=1  
    distance = sorted(distance, key=itemgetter(0))
    k_dist = [l[1] for l in distance[:1]]           #k distance for every element in distance arr :1
    return k_dist

def dist(i,data):
    total = 0
    for j,k in zip(i,data):         #loop , zip can make it easier to go through and find k distance 
        num = (abs(j-k)**2)     #calculate distance
        total += num
    return (total**(1/2))       

def backwardElimination(data):          #backwards logic of forward selection
    dataFeatures = data.shape[1]        #get num of features
    featBest = list(range(1,dataFeatures))      #arr with best features   
    current_set = list(range(1,dataFeatures))   #current set alr contains dataFeatures
    accuracyMax = 0                     #maximum acc to return 

    for i in range(1,dataFeatures):
        tempMax = 0
        featList = []
        for j in range(1, dataFeatures):
            if j not in current_set:            #skip if j is still not in the current set
                continue
            tempFeatures = [i for i in current_set if i != j]
            tempAccuracy = leave_one_out_x_valid(data[:,[0]+ tempFeatures])
            print('\tUsing feature(s) ', tempFeatures ,' accuracy is ', round(tempAccuracy,2), '%.' )

            if(tempMax < tempAccuracy):
                featList = j
                tempMax = tempAccuracy      #assign max to current max accuracy 

        if featList:    #if not 0
            current_set = [k for k in current_set if k != featList]
            if(accuracyMax < tempMax):  #check max btw tempMax and overall accuracy 
                accuracyMax = tempMax
                featBest[:] = current_set
                print('Feature set ', current_set,' was best, accuracy is ', round(tempMax,2), '%.' )
            else:
                print('Feature set ', current_set,' was best, accuracy is ', round(tempMax,2), '%.' )
    print('\nFinished search! The best feature subset is ', featBest,', which has an accuracy of ', round(accuracyMax,2), '%.')

def forwardSelection(data):
    dataFeatures = data.shape[1]        #get num of features
    featBest = []                   #arr with best features   
    current_set = []                    #arr with current set in data
    accuracyMax = 0                     #maximum acc to return 
    for i in range(1,dataFeatures):     #outer loop for i in dataFeatures
        tempMax = 0
        featList = []
        for j in range(i, dataFeatures):    #innter loop for i in dataFeatures
            if j in current_set:            #skip j in current set
                continue
            tempFeatures = [0] + current_set + [j]
            tempAccuracy = leave_one_out_x_valid(data[:,tempFeatures])
            print('\tUsing feature(s) ',current_set+[j] ,' accuracy is ', round(tempAccuracy,2), '%.' )

            if(tempMax < tempAccuracy):
                featList = j
                tempMax = tempAccuracy      #assign max to current max accuracy 

        if featList:    #if not 0
            current_set.append(featList)
            if(accuracyMax < tempMax):  #check max btw tempMax and overall accuracy 
                accuracyMax = tempMax
                featBest[:] = current_set
                print('Feature set ', current_set,' was best, accuracy is ', round(tempMax,2), '%.' )
            else:
                print('Feature set ', current_set,' was best, accuracy is ', round(tempMax,2), '%.' )
    print('\nFinished search! The best feature subset is ', featBest,', which has an accuracy of ', round(accuracyMax,2), '%.')
    
if __name__ == "__main__":
    menu()