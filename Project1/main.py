import copy
from functools import total_ordering
import heapq 

goal_state = [[1,2,3],[4,5,6],[7,8,0]]  # setting our goal/finished state

def menu():
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
        print('Enter the 3x3 puzzle: [example:1 2 3(enter)..etc')
        for x in range(3):
            arr.append([int(y) for y in input().split()])
        print('\nYour puzzle:')
        printArray(arr)
    elif userOpt == 2:              #preset puzzle
        arr = (['1', '0', '3'],
               ['4', '2', '6'],
               ['7', '5', '8'])
        printArray(arr)
    #choose which algorithm
    algoPick = input('\nChoose an algorithm to solve puzzle: \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Manhattan Distance heuristic. \n'
                    'Enter choice: ')
    algoPick = int(algoPick)
    generalSearch(arr,algoPick)     #pass in to algo method

#formats the array nicely#
def printArray(arr = []): 
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in arr]))

#checks if the array is at goal state#
def goalCheck(arr):
    if goal_state == arr:
        return True
    else:
        return False

#Returns the ROW/COL of zero in the puzzle#
def getZero(arr = []):
    for i in range(3):
	    for j in range(3):
		    if arr[i][j] == 0:
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
def misplacedTiles(arr=[]):
    misplacedTiles = 0
    for i in range(3):
        for j in range(3):          #check if not at 0 and not at goal state
            if arr[i][j] != 0 and arr[i][j] != goal_state[i][j]:
                misplacedTiles += 1
    return misplacedTiles       

#Move 0 up#
def up(rowZero, colZero, depth, arr = [], working_nodes = []):
    temp = copy.deepcopy(arr)                           #copy of current node
    temp[rowZero][colZero] = temp[rowZero-1][colZero]   #swap the zero up in puzzle
    temp[rowZero-1][colZero] = 0
    newNode = Node(temp,0,depth)            #update new node 
    working_nodes.append(newNode)           #add to node list

#Move 0 down#
def down(rowZero, colZero, depth, arr = [], working_nodes = []):
    temp = copy.deepcopy(arr)                           #copy of current node
    temp[rowZero][colZero] = temp[rowZero+1][colZero]   #swap the zero down in puzzle
    temp[rowZero+1][colZero] = 0
    newNode = Node(temp,0,depth)            #update new node 
    working_nodes.append(newNode)           #add to node list

#Move 0 right#
def right(rowZero, colZero, depth, arr = [], working_nodes = []):
    temp = copy.deepcopy(arr)                           #copy of current node
    temp[rowZero][colZero] = temp[rowZero][colZero+1]   #swap the zero right in puzzle
    temp[rowZero][colZero+1] = 0
    newNode = Node(temp,0,depth)            #update new node 
    working_nodes.append(newNode)           #add to node list

#Move 0 left#
def left(rowZero, colZero, depth, arr = [], working_nodes = []):
    temp = copy.deepcopy(arr)                           #copy of current node
    temp[rowZero][colZero] = temp[rowZero][colZero-1]   #swap the zero left in puzzle
    temp[rowZero][colZero-1] = 0
    newNode = Node(temp,0,depth)            #update new node 
    working_nodes.append(newNode)           #add to node list

def updateQueue(choice, working_nodes =[], working_q =[]):
    #loop through list to update cost of node in list
    for i in range(len(working_nodes)):
        if choice == 2:         #update cost for Misplaced Tile Search
            heuristic = misplacedTiles(working_nodes[i].currState)
            working_nodes[i].heuristic = heuristic
            working_nodes[i].cost = working_nodes[i].heuristic + working_nodes[i].depth

        elif choice == 3:         #update cost for Manhattan Search
            heuristic = misplacedTiles(working_nodes[i].currState)
            working_nodes[i].heuristic = heuristic
            working_nodes[i].cost = working_nodes[i].heuristic + working_nodes[i].depth
        
        #update working queue
        #working_q.append(working_nodes[i])
        heapq.heappush(working_q, working_nodes[i])

#General-Search method#
def generalSearch(arr, choice):
    heuristic = 0           #init heuristic, max queue, and expanded nodes
    expanded_nodes = 0
    maximum_q = 0    
    working_q =[]           #init queue
    working_nodes =[]       #tracking expanded nodes

    #figure out heauristics. 
    if choice == 1:     # Uniform Cost Search - hard coded to 0
        heuristic = 0
    if choice == 2:     # A* Misplaced Tile heuristic
        heuristic = misplacedTiles(arr) 
    if choice == 3:     # A* Manhattan Distance heuristic
        heuristic = manhattanDistance(arr) 

    node = Node(arr, heuristic, 0)      #initialize node
    #working_q.append(node)
    heapq.heappush(working_q, node)

    continueSearch = True                   #will be while loop variable
    while continueSearch:
        #Base case - no solution - FAILURE
        if len(working_q) == 0:                
            print('Algorithm could not solve puzzle. Please try again.')
            continueSearch = False 
        
        #sort queue by herusitc/depth if Misplaced Tile or Manhattan Distance
        #if choice == 2 or choice ==3: 
        #    working_q = sorted(working_q, key = lambda node: (node.cost))

        heapq.heapify(working_q)
        currNode = heapq.heappop(working_q)
        #currNode = working_q.pop(0)             #remove front node
        
        if currNode.currState == goal_state:    #goal test
            print('\n\nPUZZLE SOLVED!')
            printArray(currNode.currState)
            print('\nSolution depth was: ', currNode.depth)
            print('Number of nodes expanded: ', expanded_nodes)
            print('Max queue size: ', maximum_q)
            continueSearch = False

        #continue search
        else:
            #print current node state being expanded
            print('The best state to expand with a g(n) = ', currNode.depth, 'and h(n) = ', currNode.heuristic, ' :')
            printArray(currNode.currState)
            depth = currNode.depth + 1                        #add to depth
            rowZero,colZero = getZero(currNode.currState)     #returns both row,col of 0 in array   
            
            #check for position to swap
            if rowZero != 0:   #up
                expanded_nodes += 1
                up(rowZero, colZero, depth, currNode.currState, working_nodes)

            if rowZero != 2:   #down
                expanded_nodes += 1
                down(rowZero, colZero, depth, currNode.currState, working_nodes)

            if colZero != 0:   #left
                expanded_nodes += 1
                left(rowZero, colZero, depth, currNode.currState, working_nodes)

            if colZero != 2:   #right
                expanded_nodes += 1
                right(rowZero, colZero, depth, currNode.currState, working_nodes)

            #add new nodes to the queue 
            updateQueue(choice, working_nodes, working_q)

            #update max queue size
            if maximum_q <= len(working_q):
                maximum_q = len(working_q)

            #continue loop
            continueSearch = True


####### Node Class ########
class Node:
    def __init__(self, arr, heuristic, depth):
        self.currState = arr            # basically points to array
        self.heuristic = heuristic      # will need for A*
        self.depth = depth              # depth for calc
        self.cost = heuristic + depth   # cost = depth g(n) + heuristic h(n)
    
    #need to import these functions in order for heapq to work
    def __eq__(self, other):
        return ((self.cost) == (other.cost))

    def __ne__(self, other):
        return ((self.cost) != (other.cost))

    def __lt__(self, other):
        return ((self.cost) < (other.cost))

    def __le__(self, other):
        return ((self.cost) <= (other.cost))

    def __gt__(self, other):
        return ((self.cost) > (other.cost))

    def __ge__(self, other):
        return ((self.cost) >= (other.cost))
    
#MAIN DRIVER#
if __name__ == "__main__":
    menu()