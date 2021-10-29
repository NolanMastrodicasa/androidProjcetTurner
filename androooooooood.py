import turtle as trtl
import random
import playsound
import time
screen_h = 400
screen_w = 420

wn = trtl.Screen() # makes turtle cell phone symbol
wn.setup(width=screen_w, height=screen_h)
turtle_image = "call2.gif"
wn.addshape(turtle_image)
phone = trtl.Turtle(shape=turtle_image)

android_color = str(input("Pick a color for your brand new galaxy note 7!: "))

# Code to draw the phone
colors = ["red", "green", "blue", "purple", "black", "salmon", "yellow"]# creates random color list 
phone.color(android_color)
phone.speed(10)
phone.penup()
phone.right(90)
phone.forward(100)  
phone.right(90)
phone.forward(100)
phone.right(180)
phone.pendown()
phone.pensize(2)
for i in range(2):
    phone.forward(150)
    phone.left(90)
    phone.forward(225)
    phone.left(90)
phone.pensize(1)
phone.penup()
phone.forward(75)
phone.left(90)
phone.forward(25)
phone.left(90)
phone.pendown()
phone.forward(75)
phone.backward(150)
phone.penup()
phone.right(90)
phone.forward(25)
phone.left(90)
phone.pendown()

for i in range(3):
    phone.color(random.choice(colors))
    phone.penup()
    phone.forward(37)
    phone.pendown()
    phone.begin_fill()
    phone.circle(10)
    phone.end_fill()
phone.color("black")
phone.penup()
phone.right(90)
phone.forward(25)
phone.right(90)
phone.pendown()
phone.color(random.choice(colors))
phone.begin_fill()
phone.circle(10)
phone.end_fill()
phone.penup()
phone.forward(37)
phone.pendown()
phone.color(random.choice(colors))
phone.begin_fill()
phone.circle(10)
phone.end_fill()
phone.penup()
phone.forward(37)
phone.pendown()
phone.color(random.choice(colors))
phone.begin_fill()
phone.circle(10)
phone.end_fill()
phone.penup()
phone.forward(37)
phone.color(android_color)
phone.left(90)
phone.pendown()
phone.forward(135)
phone.left(90)
phone.forward(150)
phone.penup()
phone.right(90)
phone.forward(5)
phone.right(90)
phone.forward(75)
phone.pendown()
phone.circle(3)

phone.penup()
phone.right(90)
phone.forward(50)
phone.left(90)
phone.backward(35)
phone.pensize(5)
phone.color("black")
phone.write("Sugmin Is Calling!")
phone.pensize(1)
phone.goto(-22,25)

Answer = str(input("Do you pick up?")) # asks user if they answer or not
if Answer == "yes":

    for i in range(500): # loops sound and movement
        time.sleep(0.5)
        from playsound import playsound
        playsound('My_audio.mp3')

        for i in range(30):
            phone.penup()
            movement = random.randint(5,10)
            phone.forward(movement)
            movement = random.randint(5,10)
            phone.backward(movement)
            phone.goto(-22,25)

else:
    print("good choice")
      
wn = trtl.Screen()
wn.mainloop()
