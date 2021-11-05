import copy

goal_state = [[1,2,3], # setting our goal/finished state 
			  [4,5,6],
			  [7,8,0]]

def main():
    print('Project 1: CS170 8 Puzzle - Brayan Montiel\n')
    print('Please choose an option below: ')
    # cin which option user wants to choose.
    userOpt = input('1. Enter a custom 3x3 puzzle. \n'
                    '2. Choose puzzle for me. \n'
                    'Enter choice: ')
    userOpt = int(userOpt)
    arr = []
    if userOpt == 1:  # custom puzzle
        print('Lets create your puzzle. Enter one 0 for missing piece. (Program assumes no incorrect input)\n')
        #size = int(input()) 
        print('Enter the 3x3 puzzle:')
        for x in range(3):
            arr.append([int(y) for y in input().split()])
        print('/nYour puzzle:')
        printPuzzle(arr)
    elif userOpt == 2:  # preset puzzle
        arr = (['1', '0', '3'],
               ['4', '2', '6'],
               ['7', '5', '8'])
        printPuzzle(arr)
    #choose which algorithm
    userOpt = input('\nChoose an algorithm to solve puzzle: \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Manhattan Distance heuristic. \n'
                    'Enter choice: ')
    userOpt = int(userOpt)
    #print(algo(arr, userOpt))
    #if goalCheck(arr) == True: //used to see if goalCheck works

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

if __name__ == "__main__":
    main()