#Lets greet the user
print("Welcome User to the best NPC Pathfinder created by Khalid Huseyn.\n")

#First we import random we will use it later in the code
import random

#First we create the dimension of our grid
#I will ask the user what they want it to be 

Row_X_Column = int(input("Enter the size of your square grid (e.g., 6 for 6x6): "))
grid=[]

#Now lets create the 2D Grid map according to the Rows and Columns
#make empty rows and colums

rows=[]
for i in range(Row_X_Column):
    row=["."]* Row_X_Column
    grid.append(row)

#create empty spaces for easier readability
for row in grid:
    print(" ".join(row))
    

#create a function for our empty positions in the grid
def get_empty_positions():
    #first we define an empty list
    empty_list=[]
    #run through the range so from 0-9
    for row in range(Row_X_Column):
        #run through the column from 0-9
        for column in range(Row_X_Column):
            #check if the x and y coordinate is a dot
            if grid[row][column]==".":
                #if it is a dot it will add that . to the empty list
                empty_list.append((row,column))
    #returns the empty list
    return empty_list

#now we define the function for placing the obstacles we want the Object ( rock or wall )
#and we want to know how many times to place it randomly

def place_items(Object,count):
# for i in range of how many times to place it randomly
    for i in range(count):
        #empty positions will equal to the empty positions functions which will replace that empty spot
        empty_positions=get_empty_positions()
        if not empty_positions:
            break # we do this because if there is a already a rock or wall there to not relace it again
        # this will give a random coordinate from the list of empty positions
        row,column=random.choice(empty_positions) # we write it as row and column to make it a tuple and into 2 variables
        grid[row][column]=Object #this will go that position and replace the "." with the Object

#now we let the user input his coordinates and check to see if they are valid and then will update the grid
#give the user a prompt
def get_valid_position(prompt):
    #if the prompt is valid then we..
    while True:
        print(f"\n{prompt}")
        #let the user type in the row and column I added the Row_Column-1 to allow for the map to be either bigger or smaller
        row= int(input("Enter your row number !(0-->" + str(Row_X_Column-1)+ "): "))
        column= int(input("Enter your column number !(0-->" + str(Row_X_Column-1)+ "): "))
    #now we make a condition to check if the input the inputted is true
        #so this check to see if the row and column values are inside of the given range
        if 0<=row< Row_X_Column and 0<=column<Row_X_Column:

            #now we will check to see if it is an empty cell inside of the grid
            if grid[row][column] == ".":
                return (row,column) #returns the row and column that have a valid position
            else:
                # if the position is not valid inside of this if condition that means its blocked by an obstacle
                print("❌ ERROR ❌ \nThat cell is blocked by a (🧱 or 🪨).\nTry a different one.")
    
        else:# if the position is not valid insode of this while condition then that means the user has inputted the wrong number
            print("❌ ERROR ❌ \nOut of bounds.\nTry numbers between 0 and "+str(Row_X_Column-1))

#here is the BFS algorithm that I made on our last assignment
#but with some tweaks to make my current program work


def BFS():
    # our BFS setup
    unvisited=[[initial_point]] # we start unvisited with one path being initial point
    visited=[] # create an empty list for the nodes we are going to add that have been visited
    path= None # we don't know the shortest path so lets just make it None that has no value
    
    #we can only move down up left right so we create a direction variable 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #Begin the BFS loop
    while len(unvisited)>0: # this will make it keep going while there are paths in unvisited
        current_path=unvisited[0] # we take in the first path from unvisited
        unvisited=unvisited[1: ] # remove that path from unvisited or queue 
        node=current_path[-1] # and look at the last node in the current path, ill get to why

        #if we havent visited this node yet
        if node not in visited:
            visited.append(node) # mark that node as visited

            if node==ending_point: #check to see if we reached ending_point
                path=current_path #store the path that we found
                break #stop the search

            # if not add all of the neighbours of this node to the unvisited

            # Generate the neighbour positions (up, down, left, right)
            row, column = node
            # make a loop to shift the coordinates 
            for change_in_row, change_in_column in directions: #([(-1, 0), (1, 0), (0, -1), (0, 1)])
                #create the new row coordinate
                new_row = row + change_in_row
                #create the new column coordinate
                new_column =column+change_in_column
                
                if ( # make if statements and see if they are valid
                    0<= new_row < Row_X_Column and # if the row is in range
                    0<= new_column < Row_X_Column and # if the column is in range
                    grid[new_row][new_column] in [".","🏁","🥷"] #If the new row and new column is an empty space or at the end "E"
                ):
                    new_node= (new_row, new_column) #Define New Node
                    if new_node not in visited: # If the new node is not visited
                        new_path=current_path+[new_node] # then the new path will be the current path and the new node
                        unvisited.append(new_path) # It will add the unvisited path to the visited one
        #Draw path and print result
    if path:
        print("\n ✅ Path found! ")
        #if every condition has been met then that means the path has been found
        for r,c in path[1:-1]: # loops through each point in row and column but skips initial and ending point
            if grid[r][c]==".": # this checks if the current grid is empty
                grid[r][c]="*" # this will show the shortest path whilst avoiding obstacles
        for row in grid: # now it will loop through ecah row in the grid to update it
            print(" ".join (row)) #and this will join the cell with a space to make it look nicer
        
        print("\nSteps:", len(path) - 1) # The steps taken for the shortest path
        print("Path:", path) #this will print the path whcih is very cool
    else:
        print(print("\n❌ No path found.")) #If there is no path then thats mean no path was found


# Calculate the total cells that we will cover so thats Total Rows * Total Columns
total_cells = Row_X_Column * Row_X_Column
obstacle_count = total_cells // 20 # Divide it by num so the obstacles and walls covers about of the grid map

# Place the obstacles onto the grid map
place_items("🧱", obstacle_count) # This code will place the walls
place_items("🪨", obstacle_count) # This code will place the rocks


# This will ask the user for the Starting point and Ending point
initial_point = get_valid_position("Choose your Initial point")
ending_point = get_valid_position("Choose your Ending point")

grid[initial_point[0]][initial_point[1]] = "🥷" # This will show the starting point as a ninja
grid[ending_point[0]][ending_point[1]] = "🏁" # This will show the ending point as a finishing flag

# AND THIS WILL FINALLY RUN THE PROGRAMM YESSSSS
BFS()
