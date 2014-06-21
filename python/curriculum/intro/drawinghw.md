## Easy

Ask the students to re-create the result of the following simple drawing problems. No loops are necessary.

Draw the first letter of your name. Here's how you draw a 'Y':

> Use the turtle.setpos (or set position) function to set the turtle's initial location.

```python
import turtle

t = turtle.Turtle()

t.hideturtle()

t.setpos(0, -100)
t.forward(30)
t.left(90)
t.forward(140)
t.right(35)
t.forward(100)
t.right(55)
t.backward(65)
t.left(55)
t.backward(40)
t.left(70)
t.forward(40)
t.left(55)
t.forward(65)
t.right(55)
t.backward(100)
t.right(35)
t.backward(140)
t.right(90)
t.forward(30)
```

Drawing three offset squares:
```python
import turtle
t = turtle.Turtle()

t.left(20)

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.left(30)

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.left(40)

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
```

rip from [OpenTechSchool](http://opentechschool.github.io/python-beginners/en/simple_drawing.html)

## Medium

Ask the students to re-create the result of the following problems. Encourage the class to manipulate range parameters, length traveled forward and angle turned each loop cycle.

Drawing a star.
```python
import turtle
t = turtle.Turtle()

for i in range(0, 5):
	t.forward(110)
	t.left(216)
```
> How many lines make up the star?

> The star is made of five lines, so the list of numbers is range( 0, 5 ).

> Experiment with the distance and angle parameters within the loop.

Drawing a spiral.
```python
import turtle
t = turtle.Turtle()

for i in range(5, 150):
	t.forward(n)
	t.left(25)
```

> When drawing a spiral, what increases? The length moved, but not the angle.

> We can use a for loop to run through a large range. The parameter n represents the element of the range for that run.

> Do not make your range too large ( > 200 )! Your program may crash.

> The amount alex travels forward gets bigger each run because the value of n gets bigger each run.

Drawing a sea urchin.
```python
import turtle
t = turtle.Turtle()

for i in range(5, 100, 2):
	t.forward(i)
	t.left(i)
```
> What happens if the length moved and the angle turned gets bigger during each run?

> Observe the sea urchin shape, and how it is created.

## Hard

Drawing an expanding square-like pattern.
```python
import turtle
t = turtle.Turtle()

for i in range(0, 350):
	t.forward(i)
	t.right(98)
```
> The square pattern is obtained by setting the angle turned to slightly over 90 degrees.

Drawing a sprite with user-specified number of feet:
```python
import turtle
t = turtle.Turtle()
t.shape("circle")

n = int(input("How many legs will our sprite have?"))
angle = 360 / n

for i in range(0, n):
	# draw a leg
	t.right(angle)
	t.forward(65)
	t.stamp()
	
	# return to the middle and reset
	t.right(180)
	t.forward(65)
	t.right(180)
```
> The stamp function leaves an image of the turtle at its current location.

> Notice that the turtle turns around, returns to the middle and turns a final time to re-orient itself.

rip from [InteractivePython](http://interactivepython.org/runestone/static/thinkcspy/index.html)
