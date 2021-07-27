
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10570926
#    Student name: Le Hoang Minh Do (Jaymin)
#
#  NB: Files submitted without a completed copy of this statem`ent
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [91023PT]
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  PATCHWORK QUILT
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "patchwork".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped blocks, using data
#  stored in a list to determine which blocks to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  You are to submit your final solution as a single Python 3 file.
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# must not use any other modules for your solution.

from turtle import *
from math import *
from random import *


# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100 # pixels (default is 100)
grid_width = 10 # squares (default is 10)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal') # font for the coords
big_font = ('Arial', 24, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True, mark_legend = True):
    
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    #Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, -25)
        write('Put your\nlegend here', align = 'right', font = big_font)    
        # Right side
        goto((grid_width * cell_size) // 2 + 75, -25)
        write('Put your\nlegend here', align = 'left', font = big_font)    
        
    #put the legends
    pu()
    speed('fastest')
    goto(-700,-150)
    pd()
    one_onepixel()
    pu()
    goto(-600,-300) 
    write('Snowflake', align = 'right', font =('Arial',15,'bold'))
    goto(-650, 200)
    pd()
    one_twopixels() 
    pu()
    goto(-600,50)
    write('Snowman', align = 'right', font =('Arial',15,'bold'))
    goto(650, 200)
    pd()
    two_onepixels()
    pu()
    goto(720,100)
    write('Christmas cake', align = 'right', font =('Arial',15,'bold'))
    goto(550, -50)
    pd()
    two_twopixels()
    pu()
    goto(710, -300)
    write('Christmas tree', align = 'right', font =('Arial',15,'bold'))
    
    
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "patchwork" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying where
# to place a particular block.  There may be one, two or four squares
# listed in the instruction.  This tells us which grid squares must be
# filled by this particular block.  This information also tells
# us which shape of block to produce.  A "big" block will occupy
# four grid squares, a "small" block will occupy one square, a
# "wide" block will occupy two squares in the same row, and a
# "tall" block will occupy two squares in the same column.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single block in the grid, in one of the corners.

# Small block
fixed_pattern_0 = [['A1']] 
fixed_pattern_1 = [['J7']]

# Wide block
fixed_pattern_2 = [['A7', 'B7']] 
fixed_pattern_3 = [['I1', 'J1']]

# Tall block
fixed_pattern_4 = [['A1', 'A2']] 
fixed_pattern_5 = [['J6', 'J7']]

# Big block
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7']] 
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2']]

# Each of these patterns puts multiple copies of the same
# type of block in the grid.

# Small blocks
fixed_pattern_8 = [['E1'],
                   ['J4'],
                   ['C5'],
                   ['B1'],
                   ['I1']] 
fixed_pattern_9 = [['C6'],
                   ['I4'],
                   ['D6'],
                   ['J5'],
                   ['F6'],
                   ['F7']]

# Wide blocks
fixed_pattern_10 = [['A4', 'B4'],
                    ['C1', 'D1'],
                    ['C7', 'D7'],
                    ['A7', 'B7'],
                    ['D4', 'E4']] 
fixed_pattern_11 = [['D7', 'E7'],
                    ['G7', 'H7'],
                    ['H5', 'I5'],
                    ['B3', 'C3']]

# Tall blocks
fixed_pattern_12 = [['J2', 'J3'],
                    ['E5', 'E6'],
                    ['I1', 'I2'],
                    ['E1', 'E2'],
                    ['D3', 'D4']] 
fixed_pattern_13 = [['H4', 'H5'],
                    ['F1', 'F2'],
                    ['E2', 'E3'],
                    ['C4', 'C5']]

# Big blocks
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6'],
                    ['I5', 'J5', 'I6', 'J6'],
                    ['C2', 'D2', 'C3', 'D3'],
                    ['H2', 'I2', 'H3', 'I3'],
                    ['A3', 'B3', 'A4', 'B4']] 
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3'],
                    ['E5', 'F5', 'E6', 'F6'],
                    ['E3', 'F3', 'E4', 'F4'],
                    ['B3', 'C3', 'B4', 'C4']]

# Each of these patterns puts one instance of each type
# of block in the grid.
fixed_pattern_16 = [['I5'],
                    ['E1', 'F1', 'E2', 'F2'],
                    ['J5', 'J6'],
                    ['G7', 'H7']]
fixed_pattern_17 = [['G7', 'H7'],
                    ['B7'],
                    ['A5', 'B5', 'A6', 'B6'],
                    ['D2', 'D3']]

# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with blocks.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# patchwork to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "patchwork"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place blocks using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# blocks and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger blocks placed.  In the worst case, only one big
# block will be placed in the grid (but this is very unlikely)!
#
def random_pattern(print_pattern = True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 blocks as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the block there, provided the spaces are all free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there) and \
           (not [column + 1, row] in been_there) and \
           (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the block's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2)])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 blocks as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the block there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the block's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2)])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Attempt to place as many 2x1 blocks as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the block there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the block's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1)])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Fill all remaining spaces with 1x1 blocks
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the block's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1)])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the blocks in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the patchwork pattern
    return pattern

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "patchwork" function.
#

# Fill the grid with blocks as per the provided dataset
rows = 'ABCDEFGHIJ' #create string to get the number value
def location(x,y):
    temp = rows.index(x) #get numbervalue for string
    penup()
    goto(-500 + (int(temp)*100), -350 + int(y)*100) #go to left bottom side and move on depend on the number value of alphabetic
    pd()
    setheading(0)

def patchwork(pattern):
    for i in pattern:
        if len(i) == 1: #check if it has 1 block
            location(i[0][0],i[0][1])
            one_onepixel()
        elif len(i)==2: #check if it has 2 blocks
            if i[0][0] == i[1][0]: #if it has same alphabetic (100x200)
                location(i[0][0],i[0][1])
                pu()
                seth(0)
                fd(50)
                seth(0)
                one_twopixels()
            else:
                location(i[0][0],i[0][1]) # if it has same bumber (200x100)
                seth(-90)
                fd(50)
                seth(0)
                fd(100)
                two_onepixels()
        else:
            location(i[0][0],i[0][1]) # it has 4 blocks (200x200)
            seth(90)
            fd(100)
            seth(0)
            two_twopixels()
          
            
    


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#
def one_onepixel(): 
        color('black')
        fillcolor('deep sky blue')
        #draw frame'
        width(3)
        pu()
        setheading(0)
        pd()
        begin_fill()
        fd(100)
        right(90)
        fd(100)
        right(90)
        fd(100)
        right(90)
        fd(100)
        end_fill()
        penup()
        setheading(0)
        fd(55)
        setheading(-90)
        fd(45)
        width(1)
        pd()
        #draw a hexagon in middle
        fillcolor('navy')
        begin_fill()
        for i in range(6):
                forward(5) 
                right(60)
        end_fill()
        fillcolor('blue')
        
        def square():
            pendown()
            begin_fill()
            left(100)  
            forward(7)
            right(90)
            forward(7)
            right(90)
            forward(7)
            right(90)
            forward(7)
            end_fill()
            penup()
        
        #draw 5 square
        fd(5)
        square()
        pu()
        setheading(180)
        fd(11)
        left(90)
        fd(2)
        square()
        fd(2)
        left(90)
        fd(4)
        right(180)
        square()
        setheading(25)
        fd(8)
        setheading(90)
        fd(2)
        setheading(0)
        square()
        setheading(-10)
        fd(9)
        square()

        fillcolor('dodger blue')
        def triangle():
            pd()
            begin_fill()
            forward(10) 
            left(120)
            forward(10)
            left(120)
            forward(10)
            end_fill()
            penup()

        #draw 6 triangle
        setheading(30)
        fd(18)
        setheading(130)
        triangle()
        backward(43)
        triangle()
        setheading(-30)
        fd(42)
        setheading(50)
        triangle()
        setheading(163)
        fd(15)
        triangle()
        setheading(85)
        fd(34)
        setheading(190)
        triangle()

        fillcolor('light sky blue')
        def draw_rhombus():
            penup()
            for i in range(1, 3):
                pendown()
                begin_fill()
                forward(10)
                left(180 - 50)
                forward(10)
                left(50)
                end_fill()
                pu()

         #draw 6 rhombus
        setheading(90)
        fd(7)
        setheading(130)
        fd(3)
        draw_rhombus()
        setheading(-30)
        fd(26)
        setheading(0)
        fd(3)
        setheading(70)
        draw_rhombus()
        setheading(-110)
        fd(40)
        setheading(-18)
        fd(10)
        draw_rhombus()
        setheading(180)
        fd(37)
        seth(-80)
        draw_rhombus()
        seth(100)
        fd(39)
        left(85)
        fd(7)
        draw_rhombus()
       

        #exit and done
        hideturtle()
        update()
def one_twopixels():
    color('black')
    #draw a frame
    fillcolor('deep sky blue')
    #draw frame'
    width(3)
    pu()
    setheading(180)
    fd(50)
    setheading(90)
    pd()
    begin_fill()
    fd(100)
    right(90)
    fd(100)
    right(90)
    fd(200)
    right(90)
    fd(100)
    right(90)
    fd(100)
    end_fill()
    width(1)
    seth(0)
    pu()
    fd(88)

    def draw_circle(color, radius):
        penup()
        fillcolor(color)
        pendown()
        begin_fill()
        circle(radius)
        end_fill()  
    #draw a body
    seth(90)
    fd(-43)
    draw_circle('dark gray', 41)
    seth(180)
    fd(1)
    seth(90)
    fd(1)
    draw_circle('white', 40)
    pu()
    setheading(180)
    fd(5)
    seth(90)
    fd(49)
    draw_circle('dark gray', 33)
    seth(90)
    fd(2)
    draw_circle('white', 33,)
    pu()
    seth(180)
    fd(8)
    seth(90)
    fd(35)
    draw_circle('dark gray', 25)
    seth(90)
    fd(2)
    draw_circle('white', 25)
    #draw face
    pu()
    seth(150)
    fd(15)
    draw_circle("black", 2) #Drawing left eye
    seth(180)
    pu()
    fd(20)
    draw_circle("black", 2) #Drawing right eye
    #Drawing nose
    penup()
    seth(0)
    fd(10)
    seth(-90)
    fd(13)
    seth(0)
    fillcolor('dark orange')
    pendown()
    begin_fill()
    left(15)
    forward(15)
    right(150)
    forward(20)
    right(130)
    forward(10)
    end_fill()
    #Below three statements for drawing buttons
    seth(-90)
    pu()
    fd(35)
    draw_circle("firebrick", 2)
    seth(-90)
    pu()
    fd(8)
    draw_circle("firebrick", 2)
    #Code for drawing hat
    #penup()
    seth(90)
    pu()
    fd(65)
    seth(180)
    pd()
    fd(-35)
    color("black")
    pendown()
    fillcolor("black")
    begin_fill()
    seth(90)
    fd(3)
    left(90)
    fd(70)
    left(90)
    fd(3)
    left(90)
    fd(60)
    end_fill()
    begin_fill()
    left(90)
    fd(35)
    left(90)
    fd(50)
    left(90)
    fd(35)
    end_fill()
    penup()
    fd(50)
    seth(180)
    fd(5)
    seth(-90)
    #code for drawing hand
    #right side
    width(3)
    pd()
    right(130)
    forward(9)
    left(60)
    forward(10)
    backward(10)
    right(60)
    forward(5)
    right(60)
    forward(9)
    backward(9)
    left(60)
    forward(8)
    penup()
    #left side
    seth(0)
    fd(75)
    seth(160)
    pd()
    right(100)
    forward(5)
    right(60)
    forward(10)
    backward(10)
    left(60)
    forward(5)
    left(60)
    forward(9)
    backward(9)
    right(60)
    forward(8)
    right(40)

    #exit and done
    hideturtle()
    update()

def two_onepixels():
    #draw a frame
    fillcolor('deep sky blue')
    #draw frame'
    width(3)
    pu()
    setheading(180)
    fd(100)
    setheading(90)
    pd()
    begin_fill()
    fd(50)
    right(90)
    fd(200)
    right(90)
    fd(100)
    right(90)
    fd(200)
    right(90)
    fd(100)
    end_fill()
    def draw_circle(colour, radius):
            penup()
            color(colour)
            fillcolor(colour)
            #pendown()
            begin_fill()
            circle(radius)
            end_fill()
    pu()
    seth(0)
    fd(20)
    seth(-90)
    fd(88)
    seth(0)
    for i in range(15):
        draw_circle('#FFFFFF', 5)
        fd(10)
    pu()
    seth(70)
    fd(2)
    setheading(70)
    for i in range(7):
            draw_circle('white', 5)
            fd(10)
    seth(180)
    pu()
    fd(7)
    for i in range(15):
        draw_circle('white',5)
        fd(10)
    seth(250)
    pu()
    fd(4)
    for i in range(6):
            draw_circle('white', 5)
            fd(10)
    pd()
    seth(0)
    fd(2)
    seth(230)
    backward(5)
    pu()
    seth(80)
    fd(45)
    seth(0)
    fd(15)
    seth(250)
    color('red')
    pd()
    fillcolor('red')
    begin_fill()
    for i in range(2):
       fd(48)
       seth(0)
       fd(43)
    left(68)
    fd(50)
    seth(180)
    fd(130)
    end_fill()
    color('yellow')
    pu()
    seth(0)
    fd(25)
    seth(-90)
    fd(21)
    write('Merry' ,move = False, align='center', font=('Arial',10,'bold'))
    seth(0)
    fd(50)
    seth(-90)
    fd(16)
    write('Christmas' ,move = False, align='center', font=('Arial',10,'bold'))
    color('black')
    hideturtle()      
def two_twopixels():
    fillcolor('deep sky blue')
    #draw frame'
    width(3)
    pu()
    setheading(0)
    pd()
    begin_fill()
    fd(200)
    right(90)
    fd(200)
    right(90)
    fd(200)
    right(90)
    fd(200)
    end_fill()
    penup()
    setheading(0)
    fd(55)
    setheading(-90)
    fd(100)
    width(1)
    pu()
    fd(50)
    pd()
   
    setheading(182)
    #draw body of tree
    fillcolor('forest green')
    begin_fill()
    for i in range(3):
        right(7)
        fd(5)
        right(7)
        fd(5)
        right(30)
        fd(5)
        right(95)
        fd(45)
        left(140)
    for i in range(3):
        left(130)
        fd(45)
        right(95)
        fd(5)
        right(30)
        fd(5)
        right(7)
        fd(5)
    for i in range(8):
        fd(7)
        left(7)
        fd(6)
        right(8)
    end_fill()
    fd(3)
    #draw a star
    pu()
    color('yellow')
    seth(0)
    fd(50)
    seth(90)
    fd(97)
    seth(100)
    right(30)
    begin_fill()
    pd()
    for i in range(5):
        fd(20)
        right(144)
    end_fill()
    pu()
    #Draw ornament balls
    color('crimson')
    seth(-90)
    fd(44)
    seth(0)
    fd(20)
    dot(12)
    seth(-90)
    fd(40)
    seth(0)
    fd(15)
    dot(12)
    seth(180)
    fd(60)
    seth(90)
    fd(3)
    dot(12)
    fd(30)
    seth(0)
    fd(10)
    dot(12)
    seth(90)
    fd(30)
    seth(0)
    fd(10)
    dot(12)

    #draw the trunk of tree
    color('black')
    width(3)
    fillcolor('sienna')
    seth(-90)
    fd(79)
    seth(180)
    fd(10)
    seth(-90)
    begin_fill()
    pd()
    fd(20)
    left(10)
    fd(8)
    left(20)
    fd(4)
    left(60)
    fd(28)
    left(60)
    fd(4)
    left(20)
    fd(8)
    left(10)
    fd(19)
    left(90)
    fd(33)
    end_fill()
    left(181)
    hideturtle()
    #draw a moon
    penup()
    seth(90)
    fd(150)
    seth(180)
    fd(57)
    color('orange')
    begin_fill()
    circle(20)
    end_fill()
    color('deep sky blue')
    begin_fill()
    seth(180)
    fd(9)
    seth(-90)
    fd(17)
    circle(20)
    end_fill()
    color('black')
    
    hideturtle()

    
# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True, mark_legend = False)


# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('slow')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its blocks
title("Put a description of your theme and blocks here")

### Call the student's function to follow the path
### ***** While developing your program you can call the patchwork
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your patchwork function must work for any data
### ***** set that can be returned by the random_pattern function.
#patchwork (fixed_pattern_0) # <-- used for code development only, not marking
patchwork(random_pattern()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
