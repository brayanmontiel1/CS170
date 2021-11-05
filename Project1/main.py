import copy

goal_state = [[1,2,3],[4,5,6],[7,8,0]]  # setting our goal/finished state

def main():
    print('Project 1: CS170 8 Puzzle - Brayan Montiel\n')
    print('Please choose an option below: ')
    # cin which option user wants to choose.
    userOpt = input('1. Enter a custom 3x3 puzzle. \n'
                    '2. Choose puzzle for me. \n'
                    'Enter choice: ')
    userOpt = int(userOpt)
    arr = []
    if userOpt == 1:        #custom puzzle
        print('Lets create your puzzle. Enter one 0 for missing piece. (Program assumes no incorrect input)\n')
        print('Enter the 3x3 puzzle:')
        for x in range(3):
            arr.append([int(y) for y in input().split()])
        print('\nYour puzzle:')
        printPuzzle(arr)
    elif userOpt == 2:         #preset puzzle
        arr = (['1', '0', '3'],
               ['4', '2', '6'],
               ['7', '5', '8'])
        printPuzzle(arr)
    #choose which algorithm
    algoPick = input('\nChoose an algorithm to solve puzzle: \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Manhattan Distance heuristic. \n'
                    'Enter choice: ')
    algoPick = int(algoPick)
    algo(arr,algoPick)          #pass in to algo method

#formats the array nicely#
def printPuzzle(arr = []): 
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in arr]))

#checks if the array is at goal state#
def goalCheck(arr):
    if goal_state == arr:
        return True
    else:
        return False

#Returns the ROW/COL of zero in the puzzle#
def getZero(node = []):
    for i in range(3):
	    for j in range(3):
		    if node[i][j] == 0:
			    return i,j          #remember two returns, catch both.

#returns heuristic for A* Manh. Distance#
def manhattanDistance(arr=[]):
    distance = 0
    ROW = 0             #current row/col
    COL = 0
    goalROW = 0         #goalstate row/col
    goalCOL = 0

    for h in range(1,9):            #go thru whole puzzle
        for i in range(3):
            for j in range(3):          #check if not at 0 and not at goal state
                if goal_state[i][j] == h:       #get coordinates goal state
                    goalROW = i
                    goalCOL = j
                if arr[i][j] == h:              #get arr coordinates
                    ROW = i
                    COL = j
            distance += abs(goalROW-ROW) + abs(goalCOL-COL)
    return distance             

#returns heuristic for A* Misplaced Tile#
def misplacedAStar(arr=[]):
    misplacedTiles = 0
    for i in range(3):
        for j in range(3):          #check if not at 0 and not at goal state
            if arr[i][j] != 0 and arr[i][j] != goal_state[i][j]:
                misplacedTiles += 1
    return misplacedTiles        

#algorithm method#
def algo(arr, choice):
    heuristic = 0       #init heauristic
    expanded = 0        # expanded nodes
    queue = 0           # queue
    #figure out heauristics. 
    if choice == 1:     # Uniform Cost Search
        heuristic = 0
    if choice == 2:     # A* Misplaced Tile heuristic
        heuristic = misplacedAStar(arr) 
    if choice == 3:     # A* Manhattan Distance heuristic
        heuristic = manhattanDistance(arr) 

    node = Node(arr, heuristic, 0)      #initialize node
    print(heuristic)
     

####### Node Class ########
class Node:
    def __init__(self, arr, heuristic, depth):
        self.currState = arr            # basically points to array
        self.heuristic = heuristic      # will need for A*
        self.depth = depth              # depth for calc
        self.cost = heuristic + depth   # for decision making

#MAIN DRIVER#
if __name__ == "__main__":
    main()