import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()    #Define the Turtle Screen
wn.bgcolor("#FFFFFF")
wn.title("Breadth First Search Visualiser")
wn.setup(1400,780)#Height,Width


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


# This class is used for path tracing in the Path Finding Visualiser
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square") # Shape of the Turtle
        self.color("green")  # Color of the Turtle Node
        self.penup() # Lift up the Pen so it does not leave a Trail
        self.speed(0)

# Sets a reference block in the entire Path Finding Visualiser
""" class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0) """


# Sets the Start Node for the Path Finding Visualiser
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

# Sets a reference block in the entire Path Finding Visualiser for Backtracking
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


# grid = [
# "+++++++++++++++",
# "+s+       + +e+",
# "+ +++++ +++ + +",
# "+ + +       + +",
# "+ +   +++ + + +",
# "+ + + +   + + +",
# "+   + +   + + +",
# "+++++ +   + + +",
# "+     +   +   +",
# "+++++++++++++++",
# ]
#
# grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]
#
# grid = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]

print("PATH FINDING VISUALISER")
grid_num = turtle.numinput("Grid Number", "Enter your Grid Number:", 1, minval=1, maxval=5)
if (grid_num == 1):
    grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    ]

elif (grid_num == 2):
    grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+    +++++++++++++  +++++++  ++++++++++++++++++++++",
    "+s          +                 +               ++  +",
    "+  ++++++++++++++++++++++++++++++++++++++++++++++++",
    "+  +     +  +           +  +                 +++  +",
    "+        +  +  ++++  +  +  +++++++++++++  +++  ++++",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++++++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +++++++++++++++++++++++++++++++     +++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+  e                     +  +  +              ++  +",
    "+ +++++++++++++++++++++++++++++++++++++++        ++",
    "+ ++++++ +++++++++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ ++++++++++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    ]

elif (grid_num == 3):
    grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +s                                +",
    "+    +++++++++++++  +++++++  ++++          ++++++++",
    "+          +                 +               ++  +",
    "+  ++++++++++++++                      +++++++++++",
    "+  +     +  +           +  +                 +++  +",
    "+        +  +  ++++  +  +  +++++++++++++  +++  ++++",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ +++++  +++++++++         ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++++++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +++++++++++++++++++++++++++++++     +++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                        +  +  +              ++  +",
    "+ +++++++++++++++++++++++++++++++++++++++        ++",
    "+ ++++++ +++++++++++++++    ++ ++   ++++++++++e  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ ++++++++++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    ]

elif (grid_num == 4):
    grid = [
    "+++++++++++++++",
    "+             +",
    "+             +",
    "+             +",
    "+     e       +",
    "+             +",
    "+             +",
    "+             +",
    "+ s           +",
    "+++++++++++++++",
    ]
elif (grid_num == 5):
    grid = [
    "+++++++++++++++",
    "+             +",
    "+      +++    +",
    "+      +e+    +",
    "+        +    +",
    "+      +++    +",
    "+s            +",
    "+++++++++++++++",
    ]


# Define Function Setup Maze to create the maze
# start_x, start_y, end_x, end_y are global variables to keep track of the locations of each cell
def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):                 # Read the Entire Grid line by line
        for x in range(len(grid[y])):          # Read each cell in a single line
            character = grid[y][x]             # Assign the varaible character the the x and y location od the grid
            screen_x = -588 + (x * 24)         # Move to the x location on the screen staring at -588 (pixel loc)
            screen_y = 288 - (y * 24)          # Move to the y location of the screen starting at 288 (pixel loc)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                 # add coordinate to walls list
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                # add node 'e' to the screen
                path.append((screen_x, screen_y))

            if character == "e":
                #green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("#00BFFF")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


# Function to end the Program
def endProgram():
    wn.exitonclick()
    sys.exit()


def BreadthFirstSearch(x, y):
    queue.append((x, y))
    solution[x,y] = x,y

    # The loop exits when len(queue) = 0
    while len(queue) > 0:
        time.sleep(0)
        # Pop entry in the queue queue an assign to x and y location in the maze
        x, y = queue.popleft()

        # Checking the Cells on Left Directions
        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            queue.append(cell)   # Add cell to queue list
            visited.add((x - 24, y))  # Add cell to visited list

        # Checking the Cells in Downward Direction
        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            queue.append(cell)
            visited.add((x, y - 24))
            print(solution)

        # Checking the Cells in Right Directions
        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x + 24, y))

        # Checking the Cells in Upward Directions
        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            queue.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    # Stop loop when current cells == start cell
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        # Key Value becomes the new key
        x, y = solution[x, y]

# set up classes for generation of the Path Finding Visualiser
maze = Maze() # Sets up the Maze
red = Red()   # Sets up the Start Node in the Maze
#blue = Blue()
green = Green() # Sets up the Tracing Nodes in the Maze
yellow = Yellow() # Sets up the Node for Backtracking

# setup lists
walls = []
path = []
visited = set()
queue = deque()
solution = {}


setup_maze(grid)
BreadthFirstSearch(start_x,start_y)
backRoute(end_x, end_y)
wn.exitonclick()
