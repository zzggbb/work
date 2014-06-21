## Lists

* A list is a datatype which is written as comma separated items between square brackets
* items are accessed by their `index`
	* the first item has index `0`, the `nth` item has index `n-1`

```python
x = [1,2,3,4,5]
# equivalent to
y = range(1,5)
print x[0]
#>>> 1
print range(1,5)[0]
#>>> 1
```

#### List Methods

* list.**append**(x)
	* add item `x` to the end of the list

```python
x = [1,2,3]
x.append("hello")
print x
#>>> [1,2,3,"hello"]
```

* list.**extend**(x)
	* takes a list `x` as a parameter, adds all the items in `x` to the end of the list

```python
x = range(4)
y = [1,3,5,"abc"]
x.extend(y)
print x
#>>> [0,1,2,3,1,3,5,"abc"]
```

* list.**insert**(position, x)
	* insert item `x` in the list before `position`

```python
x = range(5)
x.insert(1,"hello")
print x
#>>> [0,"hello",1,2,3,4]
```

* list.**remove**(x)
	* remove the item `x` from the list, if it exists. If it does not exist, an error is raised

```python
x = range(5)
x.remove(3)
print x
#>>> [0,1,2,4]
```

* list.**pop**(position)
	* removes an item at `position` from the list, and returns it. the position can be omitted, and it will default to the last position

```python
x = ['a','b','c','d']
last = x.pop()
first = x.pop(0)
print first
print x
print last
#>>> 'a'
#>>> ['b','c']
#>>> 'd'
```

* list.**index**(x)
	* returns the index of the item `x`

```python
x = ['a','b','c','d','e']
print x.index('c')
#>>> 2
```

* list.**count**(x)
	* count the amount of times that `x` appears in the list

```python
x = [1,2,3,4,1,2]
y = x.count(1)
print y
#>>> 2
```
* list.**sort**(comparison,key,reverse)
	*  sort the list in place. all arguments are optional
	*  `comparison` can be a function which specifies how to compare each value
	*  `key` is applied to each item in the list before sorting
	*  `reverse` is a boolean that specifies if the list should be reversed

* list.**reverse**()
	* reverse a list

## Dictionaries
* Otherwise known as "associative arrays"
* Dictionaries have no order, their values are referenced by a key, rather than
their position, with the same square-brace notation as used with lists and
strings
* written as a sequence of key:value pairs between curly-braces
    * keys can be strings or numbers
    ```python
    some_dict = {1:'hello',2:'hello again!'}
    print(some_dict[2])
    # 'hello again!'
    ```

#### Dictionary Methods

* **len**(dict)
    * len will return the number of key-value pairs when used on a dictionary
    ```python
    x = {'a':6,'b':8}
    print(len(x))
    # 2
    ```

* dict.**keys**()
    * a list of all the `keys` in the dictionary
    ```python
    x = {'eggs':2, 'bacon':5}
    print(list(x.keys()))
    # ['eggs','bacon']
    ```

* dict.**values()
    * a list of all the `values` in the dictionary
    ```python
    x = {'dave':33, 'zane':17, 'morgan':24}
    print(list(x.values()))
    # [33,17,24]
    print sum(list(x.values()))
    # 74
    ```

* dict.**items**()
    * a list of the dictionaries key-value pairs 
        * each pair is a tuple
    ```python
    l,w,h = 70,40,150
    x = { 'length':l, 'width':w, 'height':h }
    print(list(x.items()))
    # [('h',150),('w':40),('l':70)]

## Tuples
* comma separated ordered sequence of items surrounded by parenthesis
* items in a tuple are accessed by their index, as with lists
* tuples are very similar to lists, however tuples cannot be modified.
    * for example:
    ```python
    t = (1,2,3,4,5) # note, the parens are not needed in this case, but they are good to have
    print(t)
    # (1, 2, 3, 4, 5)
    t[0] = 300
    # this is illegal
    ```

## Sets
* sequence of unordered items that cannot contain duplicate items
* items in a set cannot be accessed with the same `[`*key*`]` or `[`index`]` syntax of dictionaries and lists 
* can be created with `{`*items*`}` or `set(`*list_of_items*`)`

```python
my_stuff = {'desk','chair','table','table','lamp','lamp','chair','desk'}
print(my_stuff)
# {'desk','chair','table','lamp'}
```

#### Set Operations

* thing ***in*** set
    * test if `thing` is an item in `set`
    ```python
    x = {1,2,3,4,5}
    print(5 in x)
    # True
    print(8 in x)
    # False
    ```

* a ***-*** b
    * items in `a` but not in `b`
    ```python
    a = {'a','b','c','d'}
    b = {'c','d','e','f'}
    print(a-b)
    # {'a','b'}
    print(b-a)
    # {'e','f'}
    ```

* a ***|*** b
    * or: items in `a` or `b`

* a ***&*** b
    * and: items in `a` and `b`

* a ***^*** b
    * xor: items in `a` or `b` but not both
