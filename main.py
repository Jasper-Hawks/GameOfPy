# Jasper's Game of Py is based on Conway's Game of Life
# Learn more about Conway's Game of life here (https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
# 
# Rules:
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Import modules
import time # Used to pace the program 

#Instantiates Grid Array
gridArr = [list(range(10)) for y in range (10)] # Instantiate a 2D array globally for use throughout the program
gen = 1 # Instantiate the Generation tracker

# We initally fill the array with x's those x's being the dead cells
for rows in range(len(gridArr)):
    for cols in range(len(gridArr)):

        gridArr[rows][cols] = "x" 

def drawGrid(modX, modY): # Function to draw the grid to the screen each time it is modified

    if modX == -1 and modY == -1: # -1 is the value used on startup to print the initial grid this value can not be entered by the user
        for x in range(len(gridArr)):
                for y in range(len(gridArr)):
                    print(gridArr[x][y], end=" ")
                print("\n")
        
    else: # If any other value is entered we modify the cell accordingly 
        for x in range(len(gridArr)):
            for y in range(len(gridArr)): 
                if modX == y and modY == x: 
                    # If the coordinates entered line up with the coordinates we are currently on
                    # As we loop through the array then we invert the current letter in the array 
                    # And redraw the grid to the screen
                    if gridArr[x][y] == "x":
                        gridArr[x][y] = "o"
                        drawGrid(-1,-1)
                    elif gridArr[x][y] == "o":
                        gridArr[x][y] = "x"
                        drawGrid(-1,-1)

def interGrid(): #Function interGrid is the method that allows the user to interact with the grid
    
    print("Enter x value (0-9): ") # Prompt the user to enter a x value
    try:
        x = int(input()) # Cast the input to an int
    except ValueError: # If the value can not be cast to int
        x = 10 # Then x to a value that will have the program throw the invalid prompt

    print("Enter y value (0-9): ") # Prompt the user to enter a y value 
    try:
        y = int(input()) # Cast the input to an int
    except ValueError: # If the value can not be cast to int
        y = 10 # Then change y to a value that will have the program throw the invalid prompt

    if x > 9 or x <= -1: # Check that we have a correct value for x (should be between 0-9)
       # If not print this text and call the function again
       print("Invalid X value, please try again: ")
       interGrid() 
    
    elif y > 9 or y <= -1: # Check that we have a correct value for y (should be between 0-9)
        # If not print this text and call the function again
        print("Invalid Y value, please try again: ")
        interGrid()

    drawGrid(x,y) # Then draw the grid with the modified coordinates
    answering = True # Set answering to true so the user can continue entering coordinates or 

    while answering is True:
        print("Would you like to run the Game of Py? (Yes or No)") # Prompt the user to enter whether they would like to start the Game of Py
        ans = input() # Store the users input (we don't need to cast it since input is always a string)
        if ans == "Yes" or ans == "yes": # Check whether the answer was yes
            
            logic() # Run the logic function to get the Game of Py underway
        
        elif ans == "No" or ans == "no": # Check whether the answer was no
         
            interGrid() # Run the interGrid function to keep interacting with the grid
        
        else: # Otherwise the answer was incorrect type it again
        
            print("Invalid answer try again.")
              
def logic(): # This function handles the logic and rules of CGOL the user does not interact with this function
    global gen
    neighbours = [] # Holds the neighbours of the current cell
    currentCells = [] # Holds the current cell that we use to look for neighbours

    #global gridArr # Specify the variable as global so Python won't throw a fit

    # These for loops iterate through the entire array and find the neighbours and 
    # current cell in the entire grid. Then appends them to the neighbours array
    for x in range(len(gridArr)): 
        for y in range(len(gridArr)):
                
            # Finding neighbours on the x axis is straightforward
            # But since this is a 2D array and not a 2D grid going
            # down on the Y axis in a 2D array is the same as going 
            # up in a 2D grid. Since 0 is the top row and 9 is the bottom
            try:
                nw = gridArr[x - 1][y - 1] # Find the value of the neighbour
                neighbours.append(nw) # Append it to the array
            except IndexError: # If the neighbour is out of bounds
                nw = " " # Leave it empty
                neighbours.append(nw) # And append it to the array

            try:
                n = gridArr[x][y - 1]
                neighbours.append(n)
            except IndexError: 
                n = " "
                neighbours.append(n)

            try:
                ne = gridArr[x + 1][y - 1]
                neighbours.append(ne)
            except IndexError: 
                ne = " "
                neighbours.append(ne)

            try:
                w = gridArr[x - 1][y]
                neighbours.append(w)
            except IndexError: 
                w = " "
                neighbours.append(w)

            try:
                e = gridArr[x + 1][y]
                neighbours.append(e)
            except IndexError: 
                e = " "
                neighbours.append(e)

            try:
                sw = gridArr[x - 1][y + 1]
                neighbours.append(sw)
            except IndexError: 
                sw = " "
                neighbours.append(sw)

            try:
                s = gridArr[x][y + 1]
                neighbours.append(s)
            except IndexError: 
                s = " "
                neighbours.append(s)

            try:
                se = gridArr[x + 1][y + 1]
                neighbours.append(se)
            except IndexError: 
                se = " "
                neighbours.append(se)
            
            # We also store the current cell since I didn't want to make two for
            # loops that do almost the same thing
            c = gridArr[x][y] 
            neighbours.append(c) # And we append them as the 9th item 

    # Then we iterate through the neighbour array to compile a list of all
    # the current cells in the array

    for i in range(len(neighbours)): 
        try:
            currentCells.append(neighbours[((i * 9) - 1)])# Find every 9th item in the array
        except IndexError: # Since the length of the array is 900 we don't need to go past 100
            break # So once we reach the point where there are no more cells to append we break

    del currentCells[0] # Deletes left over cell from multiplying by 0

    for i in range(len(currentCells)): # Now we iterate trhough all of the current cells

        cellsNeighbours = neighbours[i*9:((i+1)*9)] # Find a list of 9 items from the neighbours array
        cellsNeighbours = cellsNeighbours[:-1]# Store it in the cellsNeighbours array and remove the last item
        if currentCells[i] == "o":# If the current cell is alive 

            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if cellsNeighbours.count("o") < 2: # .count counts the number of o's and returns an int that we can compare

                currentCells[i] = "x"

            # Any live cell with two or three live neighbours lives on to the next generation.
            elif cellsNeighbours.count("o") == 2 or cellsNeighbours.count("o") == 3:

                currentCells[i] = "o"
                pass

            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            elif cellsNeighbours.count("o") > 3:

                currentCells[i] = "x"

        elif currentCells[i] == "x": # If the current cell is dead
            
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if cellsNeighbours.count("o") == 3:

                currentCells[i] = "o" 
                
    print("Generation " + str(gen) + ". To stop press CTRL-C on your keyboard.") # Generation prompt

    for x in range(len(currentCells)): # Then we reprint the cells
            print(currentCells[x], end=" ")
            if (x + 1) % 10 == 0: # Skip lines every ten characters
                print("\n") 
            if (x + 1) % 100 == 0:
                print("\n\n") # Skip lines at the end of the pattern
    
    time.sleep(1) # Wait between printing patterns

    for i in range(len(gridArr)): # If the above is not the case then redefine every item in the 2D
        for j in range(len(gridArr)): # gridArr
            gridArr[i][j] = currentCells[int(str(i) + str(j))]

    # Clear out these arrays since we append values to them earlier in the function
    neighbours.clear()
    currentCells.clear()
    gen += 1 # Increment the generation counter
    #Then start the function again
    logic() 

interGrid()

