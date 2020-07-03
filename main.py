import turtle
import math
t = turtle.Turtle()
def base(width, height, color):
  t.down()
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  t.up()
def roof(hh, width, height, color):
  leg = width / 2
  hyp = (leg ** 2 + height ** 2) ** .5
  a = height ** 2 + hyp ** 2 - leg ** 2
  b = 2 * height * hyp
  angle1 = math.degrees(math.acos(a/b))
  c = leg ** 2 + hyp ** 2 - height ** 2
  d = 2 * leg * hyp
  angle2 = 90-angle1
  angle1 *= 2
  t.left(90)
  t.forward(hh)
  t.fillcolor(color)
  t.begin_fill()
  t.right(90)
  t.forward(width)
  t.right(angle2)
  t.down()
  t.backward(hyp)
  t.right(angle1)
  t.forward(hyp)
  t.end_fill()
  t.up()
  t.right(180)
  t.right(angle2)
  t.right(90)
  t.forward(hh)
  t.left(90)
def door(hw, width, height, color):
  distance = (hw - width) / 2
  t.up()
  t.forward(distance)
  t.left(90)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  t.forward(height)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.up()
  t.right(90)
  t.forward(width)
  t.end_fill()
  t.forward(distance)
  t.right(180)
def chimney(hh, rh, leg, width, height1, color):
  a = width * rh / leg
  height2 = height1 - a
  t.up()
  t.left(90)
  t.forward(hh)
  t.down()
  t.fillcolor(color)
  t.begin_fill()
  t.forward(height1)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(height2)
  t.end_fill()
  t.up()
  t.backward(height2)
  t.right(90)
  t.forward(width)
  t.left(90)
  t.forward(height1)
  t.forward(hh)
  t.left(90)
def circle(hh, ):

def house():
  number = int(input("# of Houses: "))
  i = 0
  t.up()
  while i < number:
    #Here goes the program
    #Getting house parts.
    chimne = input("Chimney (y/n): ")
    circl = input("Attic Window (y/n): ")
    squar = input("House Window (y/n): ")
    lan = input("Front Land (y/n): ")
    #Getting Variables
    width = int(input("House Width: "))
    height = int(input("House Height: "))
    color = input("House Color: ")
    rheight = int(input("Roof Height: "))
    rcolor = input("Roof Color: ")
    dwidth = int(input("Door Width: "))
    dheight = int(input("Door Height: "))
    dcolor = input("Door Color: ")
    if chimne == "y":
      cwidth = int(input("Chimney Width: "))
      cheight = int(input("Chimney Height: "))
      ccolor = input("Chimney Color: ")
    if circl == "y":
      wradius = int(input("Window Radius: "))
      wcolor = input("Window Color: ")
    if squar == "y":
      sside = int(input("Window Side: "))
      scolor = input("Window Color: ")
    if lan == "y":
      ldistance = int(input("Land Distance: "))
      lcolor = input("Land Color: ")
    t.backward(290)
    t.right(90)
    t.forward(150)
    t.left(90)
    #Running the programs
    base(width, height, color)
    roof(height, width, rheight, rcolor)
    door(width, dwidth, dheight, dcolor)
    if chimne == "y":
      chimney(height, rheight, width/2, cwidth, cheight, ccolor)
    #This is the end
    i += 1
house()