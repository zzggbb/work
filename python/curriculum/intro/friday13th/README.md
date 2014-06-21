# Friday the 13ths

> Is the 13th of the month more likely to be a Friday than any other day of the week?

## Objectives
This lesson is designed to address [foo](../../roadmap.md#variables)

## Prerequisites
In order to do this lesson, students need to be able to
  * 

## Counting

Start by asking a simpler question, like how many years have passed since January 1st, 1900. The answer is obvious (just subtract 1900 from the current year), but for the sake of the problem we'll solve this by counting.

Start by making a list of years. Then, for every year in that list, print it out.
```python
years = range(1900, 2015)
for year in years:
	print year
```

Now you need to count each year. *Whenever you want to count something, you have to make a variable to store the count*. 
```python
total = 0
years = range(1900, 2015)
for year in years:
	print year
```

Every time I print out a year, I want to increase my total by 1, to indicate that I've counted one more year. *Whenever you want to increase the count variable, you need to calculate it's new value, and assign that new value back to the variable.*

Whatever ```total``` may be, it's new value needs to be ```total + 1```. For example, in the beginning, the first time I print out the year, ```total``` is 0. It's next value needs to be ```total + 1```, or ```0 + 1```, or ```1```. So I could just write ```total + 1``` everywhere that I want the count to increase by 1, like this:

```python
total = 0
years = range(1900, 2015)
for year in years:
	print year
	total + 1
```

The problem here is that total never changes (the only way to change what's in a variable is to use the ```=``` operator). If we want ```total``` to be updated with the new value, we have to set its value to ```total + 1```, like this:
```python
total = total + 1
```
