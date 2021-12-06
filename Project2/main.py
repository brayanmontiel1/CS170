import copy
import time

def menu():
    print('Project 2: CS170 Feature Classification - Brayan Montiel\n')
    fileSmall = ''
    fileLarge = ''
    # cin which option user wants to choose.
    
    #choose which algorithm
    algoPick = input('\nChoose an algorithm to solve puzzle: \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Manhattan Distance heuristic. \n'
                    'Enter choice: ')
    algoPick = int(algoPick)

#formats the array nicely#
def printArray(arr = []):       #https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python#
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in arr]))

    
#MAIN DRIVER#
if __name__ == "__main__":
    menu()