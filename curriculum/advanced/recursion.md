## Exploring Recursion through...

### ... The fibonacci sequence

```
nth term : 1  1  2  3  5  8  13 21 34 55  89  144 233
n        : 1  2  3  4  5  6  7  8  9  10  11  12  13
```

* The `nth` term is the sum of the previous two terms
* `fib(10) = fib(9) + fib(8) = 34 + 55 = 89`

```python
def fib(n):
  if n < 3:   # the 1st and 2nd factorials are 1
    return 1
  else:
    return fib(n-2) + fib(n-1)
```
```python    
print fib(11)
>>> 89
```

### ... Through exponents

```
5**3 = 5 * 5 * 5 = 5**1 * 5**2
5**2 = 5 * 5 = 5**1 * 5**1
5**1 = 5 * 1 = 5 * 5**0
5**0 = 1
```

* any exponent (`5**3` for example) is the base (`5`) multiplied by the base to one less than the power (`5**2`) 

```python
def power(base,exponent):
  if exponent == 0: #anything to the 0 power is 1
    return 1
  else:
    return base * power(base,exponent-1)
```
### ...Through factorial

* 5 factorial (written as `5!`) = `5 * 4 * 3 * 2 * 1 = 120`
* `4! = 4 * 3 * 2 * 1 = 24`
* `n` factorial = `n * (n-1)!`
* So how do we code this in python!

```python
def factorial(n):
  if n == 0:    # 0! = 1
    return 1
  else:
    return n * (n-1)
