## Repeating characters in strings
```python
f("hello",3)    #-> "hhheeellllllooo"
f("techlab",2)  #-> "tteecchhllaabb"
```

### Challenge, make it ignore spaces
```python
f("foo bar baz",3)  #-> "fffoooooo bbbaaarrr bbbaaazzz"
```

## nth prime number
```python
"""
  1 2 3 4 5  6  7  8  9  10 11 12 13 14
  2 3 5 7 11 13 17 19 23 29 31 37 41 43
"""
f(3)            #-> 5
f(13)           #-> 41
```

## repetitions in a list

```python
def in_a_row(array, number, repeats):
	grouped = zip(*[array[i:] for i in range(repeats)])
	do_have_number = [list(x) for x in grouped if number in x]
	all_same = [x for x in do_have_number if len(set(x)) < 2]
	return len(all_same) > 0

print in_a_row([1,4,3,3,3,3,3,3,8,8],8,3)
#>>> False
print in_a_row([1,4,3,3,3,3,3,3,8,8,8],8,3)
#>>> True
```
