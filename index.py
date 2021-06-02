# Conways Game of Life
# Rules:
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#Instantiates Grid Array
gridArr = [list(range(10)) for y in range (10)] # Instantiate a 2D array 

for rows in range(len(gridArr)):
    for cols in range(len(gridArr)):

        gridArr[rows][cols] = "x" # 

def drawGrid(modX, modY):

    if modX == 0 and modY == 0: #This IF statment isn't working maybe its because python is insane and doesn't like () or I crapped up somewhere
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
                        drawGrid(0,0)
                    elif gridArr[modX][modY] == "o":
                        gridArr[x][y] = "x"
                        drawGrid(0,0)

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

    coords = []
    
    # These for loops add the coordinates of the os
    for x in range(len(gridArr)):
            for y in range(len(gridArr)):
                if gridArr[x][y] == "o":

                    # Put all of the os in a list 
                    # Then count the amount of os
                     
                    # The problem arises when we have 
                    # to find dead cells with three neighbours
                    
                    ne = gridArr[x - 1][y + 1]
                    n = gridArr[x][y + 1]
                    nw = gridArr[x + 1][y + 1]
                    w = gridArr[x - 1][y]
                    e = gridArr[x + 1][y]
                    se = gridArr[x - 1][y - 1]
                    s = gridArr[x][y - 1]
                    sw = gridArr[x + 1][y - 1]
                    

interGrid()

