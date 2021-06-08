import time

# Conways Game of Life
# Rules:
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#Instantiates Grid Array
global gridArr
gridArr = [list(range(10)) for y in range (10)] # Instantiate a 2D array 
currentCells = []

for rows in range(len(gridArr)):
    for cols in range(len(gridArr)):

        gridArr[rows][cols] = "x" 

def drawGrid(modX, modY):

    if modX == -1 and modY == -1: 
        y = 0
        while y != 10:
            for x in range(len(gridArr)):
                for y in range(len(gridArr)):
                    print(gridArr[x][y], end=" ")
                print("\n")
            y += 1

    else:
        for x in range(len(gridArr)):
            for y in range(len(gridArr)):
                if modX == y and modY == x: 
                    if gridArr[modX][modY] == "x":
                        gridArr[x][y] = "o"
                        drawGrid(-1,-1)
                    elif gridArr[modX][modY] == "o":
                        gridArr[x][y] = "x"
                        drawGrid(-1,-1)

def interGrid(): #Function interGrid is the method that allows the user to interact with the grid
    
    print("Enter x value (0-9): ")
    x = int(input())
    print("Enter y value (0-9): ")
    y = int(input())

    if x > 9:
       print("Invalid X value, please try again: ")
       interGrid()
    
    elif y > 9:
        print("Invalid Y value, please try again: ")
        interGrid()

    drawGrid(x,y)
    answering = True

    while answering is True:
        print("Would you like to run the Game of Py?")
        ans = input()
        if ans == "Yes" or ans == "yes":
            
            logic()
        
        elif ans == "No" or ans == "no":
         
            interGrid()
        
        else: 
        
            print("Invalid answer try again")
              
def logic():
    
    neighbours = []

    # These for loops iterate through the entire array and find the neighbours of 
    # the current cells
    for x in range(len(gridArr)):
            for y in range(len(gridArr)):
                    
                try:
                    nw = gridArr[x - 1][y - 1]
                    neighbours.append(nw)
                except IndexError: 
                    nw = " "
                    neighbours.append(nw)

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

                c = gridArr[x][y]
                neighbours.append(c)

    for i in range(len(neighbours)):

        # Differentiate between an alive and a dead cell
        # Then it should be a case of determing how many os there are
        # And changing cells accordingly
        
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        try:
            currentCells.append(neighbours[((i * 9) - 1)]) 
        except IndexError:
            break         


    del currentCells[0]
    #print(currentCells)

    for i in range(len(currentCells)):

        cellsNeighbours = neighbours[i*9:((i+1)*9)]
        cellsNeighbours = cellsNeighbours[:-1]
        if currentCells[i] == "o":

            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if cellsNeighbours.count("o") < 2:

                currentCells[i] = "x"

            # Any live cell with two or three live neighbours lives on to the next generation.
            elif cellsNeighbours.count("o") == 2 or cellsNeighbours.count("o") == 3:

                currentCells[i] = "o"

            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            elif cellsNeighbours.count("o") > 3:

                currentCells[i] = "x"

        else:

            if cellsNeighbours.count("o") == 3:

                currentCells[i] = "o" 

    for x in range(len(currentCells)):
        print(currentCells[x], end=" ")
        if (x + 1) % 10 == 0:
            print("\n")
    print("\n\n")
    time.sleep(1)
    
    if(currentCells.count("x") == 100):

        print("The Game of Py is over")
        exit()

    else:
        logic() 

    #gridArr = currentCells[:]
    #print(neighbours)
   #print(gridArr)
    print("\n\n\n")
   # print(cellsNeighbours)
    print("\n\n")
    #drawGrid(-2,-2)
            


    

interGrid()

