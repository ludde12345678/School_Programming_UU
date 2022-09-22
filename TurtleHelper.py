import turtle;
import math;





#

def jump(t:turtle.Turtle,x,y):
    t.penup();
    t.goto(x,y);
    t.pendown();

def make_turtle(x, y):
    t = turtle.Turtle();
    t.hideturtle();
    jump(t, x, y);
    return t;

def rectangle(x, y, width, height, color):
    t = make_turtle(x, y);
    jump(t, x, y);
    t.hideturtle();
    t.color("black", color);
    t.begin_fill();
    for x in range(0,2):
        for li in [width, height]:
            t.forward(li);
            t.left(90);
    t.end_fill();
            
def tricolore(x, y, h):
    colorlist = ["blue", "white", "red"];
    for key, value in enumerate(colorlist):
        rectangle(x+(key*(h*(1/2))), y, (h*(1/2)), h, value);        
            
def pentagram(x, y, side, color):
    t = make_turtle(x,y);
    t.color("black", color);
    t.begin_fill();  
    t.right(90-18);
    t.forward(side);
    for i in range(4):
        t.right(180-36);
        t.forward(side);
    t.end_fill();
    
def pentagramRows(x, y, h, d):
        magicvar =  h/2;
        side = h/2;
        for i in range(5):
            for val in [y- d, d +y + h +(side*math.cos(math.pi/10))]:
                pentagram(x + i*side - magicvar/2  ,val, side, "green");  
      
def TriPentagrams(x,y, h):
    
    tricolore(x, y, h);
    pentagramRows(x, y , h, 50);
        
    
    
    
   