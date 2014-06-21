# Prime numbers

In this lesson, students will use Python to find prime numbers, and make conclusions about the density of the prime numbers.
Students should have prior knowledge of the modulus function.

## Getting started

How do you test if a number `n` is prime?

Let's put n in a variable.
```python
n = 5077
print n
```

Ask students to take a guess on whether n is prime or not. This will get them to write the `print` instruction that they will modify after later steps.

> Is n prime? Take a guess.

```python
n = 5077
print n
print "I think n is prime."
```

Next, ask them to consider what makes a prime number prime.

> If n is prime, then what numbers can it not be divisible by?


Talk about the modulus, and how for a factor the modulus evaluates to 0.

```python
n = 5077
print n

notDivisibleBy = range(2, 5076)

for number in notDivisibleBy:
	if n % number == 0:
		print "Not prime, has a factor:"
		print number

print "I think n is prime."
```

> It's printing out a bunch of stuff, I just want one final answer - is it prime or not?

Clean up the code.
```python
n = 5077
notDivisibleBy = range(2, n)
```

Possibly add in an `int` and `input` statement:
```python
n = int(input("Give me a number"))
```

Add in the boolean, make an assumption and then try to find a counterexample. Look up one-way flag
```python
isPrime = True
for number in notDivisibleBy:
	if n % number == 0:
		isPrime = False
```

At the end, use the `isPrime` variable to determine which print statement you do

```python
if isPrime:
	print "The number is prime."
else:
	print "The number is not prime."
```

Print out all the prime numbers between 1 and 1000.

```python
for n in range(2, 1000):
	isPrime = True
	for number in notDivisibleBy:
		if n % number == 0:
			isPrime = False
```

- How many prime numbers are there (add in the `total` variable, `total = total + 1`)
- Sum of the prime numbers (modify the `total = ` statement)
- Distance between the prime numbers (add in the `lastPrime` variable, and keep updating it)
- Average distance between primes
- Twin primes (17 and 19 and 41 and 43), how many are there between 1 and 1000? Count 17 and 19 as 1 pair of twin primes.
- Distance between the twin primes.

```python
numbers = range(3, 1000)
lastPrime = 2
total = 0
distances = 0
twins = 0

for n in numbers:
	tests = range(2, n - 1)
	prime = True
	
	for test in tests:
		if n % test == 0:
			prime = False
	
	if prime:
		#print n
		if (n - lastPrime) == 2:
			twins = twins + 1
		total = total + (n - lastPrime)
		distances = distances + 1
		lastPrime = n
		
print float(total) / distances
print str(twins) + " twin primes"
```
