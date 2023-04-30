from karel.stanfordkarel import *

# this code draw a square spiral in 21x21 world.
# karel start the drawing from bottom left corner, finish in the center.

def main():
 
# draw the first 3 lines on the outside of the spiral    
    for i in range(3):
        draw_outer_line()
        turn_left()

# draw inner lines of the spiral    
    for i in range(18):
        draw_inner_line()
        turn_left()
    
    put_beeper()
    turn_right()

# use front_is_clear() condition to draw first 3 outer lines
def draw_outer_line():
    while front_is_clear():
        put_beeper()
        move()

# use no_beepers_present() condition to draw lines inside spiral
def draw_inner_line():
    while no_beepers_present():
        put_beeper()
        move()
    turn_around()
    move()
    pick_beeper()
    move()
    pick_beeper()
    turn_around()

def turn_around():
    turn_left()
    turn_left()
 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
