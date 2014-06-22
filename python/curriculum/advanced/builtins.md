# Useful Builtin Functions

## separator.join(iterable)
* create a string with every item in `iterable` separated by the `separator` string
* eg:
```python
x = ["hello","foo","bar"]
print "@#".join(x)
# "hello@#foo@#bar"
```
* the separator can be an empty string `""` if you want to remove the space between each item.

## str.split(separator)

* create a list of every item in `str` separated by `separator`
* the separator argument is optional, and if left out the separator defaults to a space (" ")
* eg:
```python
x = "this is a sentence"
print(x.split(" "))
# ['this','is','a','sentence']
```

## map(function,iterable)
* apply `function`, which can only take one argument, to every item in `iterable`
* actually returns a `map` object, which can be converted to a list
* the original iterable is not modified
* eg:
```python
def double(x):
    return x*2

x = map(increment,range(4))

print(list(x))
# [0,2,4,6]
```

## filter(function,iterable)
* return a copy of `iterable` for which all elements return `True` when passed to `function`
* eg:
```python
# function for our filter statement
def is_even(x):
    # it must return a boolean
    return x%2==0

an_iter = [1,2,3,4,5,6,7]
print(filter(is_even,an_iter))
# [2,4,6]
```

## reduce(function,iterable)
* reduce `iterable` to a single value by applying the function `function` to the next value and the current accumulated value
* the function `function` must take two parameters
* eg:
```python
def multiply(x,y):
    return x*y

an_iter = range(1,5)
print(reduce(multiply,an_iter))
# 24
# reduce(multiply,[1,2,3,4]) -> (((1*2)*3)*4)
