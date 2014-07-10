# Tic tac toe

In this lesson, students learn about functions and how they can use them to write easily readable programs.

## Getting started

Have the students print out a tic tac toe board.

```python
print "   |   |   "
print "---+---+---"
print "   |   |   "
print "---+---+---"
print "   |   |   "
```

If you want to place pieces on the board, or have something change about what prints out, you'll have to use a variable to store whatever needs to be in a certain gap.

In this particular case, the gap is just one character long. First, make a `gap` variable:
```python
gap = "X"
```

Then, hook in the gap to the board. In this case, I'm going to hook it into the center of the board.

First, I break apart the text being printed out into two pieces that are being joined back together.
```python
print "   | " + "  |   "
```

Then, I add in the variable `gap`, and adjust the spaces to compensate for the additional character being joined in.
```python
print "   | " + gap + " |   "
```

Now, whenever you change the `gap` variable, the tic tac toe board will change.

```python
print "   |   |   "
print "---+---+---"
print "   | " + gap + " |   "
print "---+---+---"
print "   |   |   "
```

> How many variables will we need to store all of the empty squares of tic tac toe?

# Making more variables

Talk to students about using some naming scheme to remember what goes where.
```python
topLeft = " "
top = " "
topRight = " "
left = " "
center = " "
right = " "
bottomLeft = " "
bottom = " "
bottomRight = " "
```

Although a much more intelligent way to name these would be
```python
row1col1 = " "
row1col2 = " "
...
```

Once they hook them in, they will have something like this:

```python
print " " + topLeft + " | " + top + " | " + topRight
print "---+---+---"
print " " + left + " | " + center + " | " + right
print "---+---+---"
print " " + bottomLeft + " | " + bottom + " | " + bottomRight
```

## Getting user input

Let's ask the user where they want to place a piece.
```python
where = input("Where do you want to put a piece?")
```

We can now use an `if` condition to check the variable `where`.

```python
if where == "center":
	center = "X"
```

However, if you want to see any changes, you'll have to print out your board again.
```python
topLeft = " "
top = " "
topRight = " "
left = " "
center = " "
right = " "
bottomLeft = " "
bottom = " "
bottomRight = " "

print " " + topLeft + " | " + top + " | " + topRight
print "---+---+---"
print " " + left + " | " + center + " | " + right
print "---+---+---"
print " " + bottomLeft + " | " + bottom + " | " + bottomRight

where = input("Where do you want to put a piece?")

if where == "center":
	center = "X"

print " " + topLeft + " | " + top + " | " + topRight
print "---+---+---"
print " " + left + " | " + center + " | " + right
print "---+---+---"
print " " + bottomLeft + " | " + bottom + " | " + bottomRight
```

And if you actually wanted to play a game of tic tac toe, you'd have to copy and paste that again 7 times. It's definitely doable, but not the smartest way to go about programming something.

## Using a loop

> What have we used in the past to do some lines of code repeatedly? (a loop)

Let's first write out in English what exactly it is that we'll be repeating. For now, let's say that 9 times, I want to print out the board, ask the user where they want to place a piece, and put a piece wherever that user says to.

In *pseudocode*, that is
```
for 9 times:
	print out the board
	ask the user where they want to place a piece
	place a piece at that square
```

Now, have the students transform this into real code. Check out the `print ":clear"` statement at the top of the loop - this clears out the terminal so you can keep typing.

```python
roundNumbers = range(0, 9)
for round in roundNumbers:
	print ":clear"
	print " " + topLeft + " | " + top + " | " + topRight
	print "---+---+---"
	print " " + left + " | " + center + " | " + right
	print "---+---+---"
	print " " + bottomLeft + " | " + bottom + " | " + bottomRight
	
	where = input("Where do you want to put a piece?")
	if where == "center":
		center = "X"
	if where == "top left":
		topLeft = "X"
	if where == "top":
		top = "X"
	if where == "topRight":
		topRight = "X"
	if where == "left":
		left = "X"
	if where == "right":
		right = "X"
	if where == "bottom left":
		bottomLeft = "X"
	if where == "bottom":
		bottom = "X"
	if where == "bottom right":
		bottomRight = "X"
```
**It is very important that students are indenting this statement correctly, and that any blank lines they leave between statements are also indented properly.**



















