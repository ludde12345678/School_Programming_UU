from random import random
from turtle import *;
import TurtleHelper;



class tPong:
    heading = 0;
    sizex = 400;
    sizey=200;
    boost = False;
    paddle1 = {"x":0, "y":0};
    paddle2 = {"x":0, "y":0};
    def __init__(self, background, speed):
        self.background = background;
        self.speed = speed;
        self.ball = Turtle();
        self.ball.screen.setup(width=self.sizex,height=self.sizey)
        self.screen = self.ball.screen
        self.initScreen();
        self.initTurtle();
    def initScreen(self):
        #self.screen.bgcolor("black");
        
        self.drawArena(self.ball,-self.sizex,-self.sizey,self.sizex*2, self.sizey*2)
    def initTurtle(self):
        TurtleHelper.jump(self.ball, 0,0);
        self.heading = 100;
        self.ball.penup();
        self.ball.speed(0);
    def drawArena(self, t, x, y, width, height):
        TurtleHelper.jump(t, x, y);
        for x in range(0,2):
            for li in [width, height]:
                t.forward(li);
                t.left(90);
            
    def tick(self):
        self.ball.setheading(self.heading)
        if self.boost:
            self.ball.forward(self.speed+1);
            self.boost = False;
        else:
            self.ball.forward(self.speed);  
        self.checkCollision();
        
    def checkCollision(self):
        h = self.ball.heading();
        x = self.ball.xcor();
        y = self.ball.ycor();
        if x >= self.sizex:
            if self.heading > 0 and self.heading < 90:
                self.heading = 180 - h; # check
            else:
                self.heading = 180 - h; # check
            self.boost = True;

        elif y >= self.sizey:
            if self.heading > 0 and self.heading < 90:
                self.heading = 0 - h;
            else:
                self.heading = 270 - (h-90); #TODO fix error here
            self.boost = True;
        elif x <= -self.sizex:
             if self.heading > 90 and self.heading < 180:
                self.heading = 180 - h;
             else:
                self.heading = 180 - h; 
             self.boost = True;
        elif y <= -self.sizey:
             if self.heading > 180 and self.heading < 270:
                self.heading = 180-(h-180);
             else:
                self.heading = 90 - (h-270); 
             self.boost = True;
