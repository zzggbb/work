## Intro
* a boolean can only be 1 of 2 values: True or False
* booleans are written with the first letter uppercased when written literally
```python
x = True # not written as `true`, as it is in languages like java
x = true # error
```

##Boolean Expressions
* not
  * gives reverse of the given boolean
  * a unary operator, it only takes one input
  ```python
  print not True
  # False
  print not False
  # True
  ```
* or
 * binary operator, goes between two other boolean expressions
 * If at least one of the boolean expressions are True, gives True
 ```python
 True or False
 # True
 True or True
 # True
 False or False
 # False
 ```

* and
 * also a binary operator, goes between two other boolean expressions
 * both expressions must be True to give True
 ```python
 True and False
 # False
 True and True
 # True
 False and False
 # False
 ```

##Logic tables
* and

...|True|False
---|---|---
True|True|False
False|False|False

* or

...|True|False
---|---|---
True|True|True
False|True|False

##Comparisons

operator|meaning
---|---
<|less than
<=|less than or equal to
>|greather than
>=|greater than or equal to
==|equal
!=|not equal
is|identity
is not| reverse identity

```python
5 < 6
#True
7 <= 7
#True
8 > 23
# False
9 >= 3
# True
7==3
# False
7!=3
#True
"cat" is "dog"
# False
"bird" is not "fish"
#True

```
