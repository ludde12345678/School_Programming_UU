import math
from turtle import *;
import random;
import TurtleHelper;


# Function to move t1 and t2 in a random direction and distance
def move_random(t1:Turtle,t2:Turtle, centerx, centery, size):
    for t in [t1, t2]:
        t.setheading(t.heading()+random.randint(-45,45));
        if not math.floor(t.xcor()) in range(math.floor(centerx-(size/2)), math.floor(centerx+(size/2))):
            t.setheading(t.towards(0,0))
            #print("outside x")
        if not math.floor(t.ycor()) in range(math.floor(centery-(size/2)), math.floor(centery+(size/2))):
            t.setheading(t.towards(0,0))
            #print("outside y")
        t.forward(random.randint(0,45))
        

def checkClose(t1:Turtle, t2:Turtle):
    if t1.distance(t2.xcor(), t2.ycor()) < 50 :
        t1.write("close!");
        return True;
    else:
        return False;

closeCounter = 0;
#Create arena and turtles
TurtleHelper.rectangle(-250,-250,500,500,"lightblue");
t1 = Turtle();
t1.color("green");
t2 = Turtle();
t2.color("red");

# Jump turtles to random location
TurtleHelper.jump(t1,random.randint(-250, 250), random.randint(-250,250));
TurtleHelper.jump(t2,random.randint(-250, 250), random.randint(-250,250));
# moverandom 500 times and count close 
for i in range(500):
    move_random(t1,t2, 0, 0, 500);
    if checkClose(t1, t2):
        closeCounter +=1;
#print number of close encounters        
print(closeCounter);