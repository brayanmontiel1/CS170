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

    
    if userOpt == 1:           #custom puzzle
        print('Lets create your puzzle. Enter one 0 for missing piece. (Program assumes no incorrect input)')
        temp1 = input('Enter the first row: ')
        temp1 = temp1.split(' ')
        temp2 = input('Enter the second row: ')
        temp2 = temp2.split(' ')
        temp3 = input('Enter the third row: ')
        temp3 = temp3.split(' ')
        print('\n')
        arr = temp1, temp2, temp3 #append rows to make puzzle 3x3
        print(arr)            
    elif userOpt == 1:           #preset puzzle
        arr = (['1', '0', '3'], 
               ['4', '2', '6'], 
               ['7', '5', '8'])
        print(arr)

    #choose which algorithm
    userOpt = input('\nChoose an algorithm to solve puzzle: \n' 
                 '1) Uniform Cost Search \n'
                 '2) A* with the Misplaced Tile heuristic. \n' 
                 '3) A* with the Manhattan Distance heuristic. \n'
                    'Enter choice: ')
    userOpt = int(userOpt)
    #
    #print(generalsearch(arr, userOpt))

if __name__ == "__main__":
    main()