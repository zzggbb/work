# Comprehensions

### List

* List comprehensions are also written inbetween `[` and `]`
* They follow the syntax `[do_something for var in list]`
* eg:
    ```python
    doubles = [x*2 for x in range(10)]
    print(doubles)
    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    def f(x):
        return x[0]

    funkified = [f(x) for x in ['hello','python','techlab','foo']
    print(funkified)
    # ['h','p','t','f']
    ```

### Dictionary
* dictionary comprehensions are also written in the same style as their non-comprehension counterpart, between `{` and `}`
* eg:

    ```python
    len_dict = {x:len(x) for x in ['hello','python','techlab','foo']}
    print(len_dict)
    # {'hello': 5, 'python': 6, 'techlab': 7, 'foo': 3} 
    ```

### Set
* written in a similar fashion to dict and list comprehensions
    ```python
    word = "abracadabra"
    unique_letters = {x for x in word}
    print(unique_letters)
    # {'c','d','r','a','b'}
    ```

* comprehensions can be chained, eg:
    ```python
    # a list ofall possible rgb values
    [[r,g,b] for r in range(256) for g in range(256) for b in range(256)]
    # this is a very long list (16,777,216 or 256**3 elements long)
    # here is a small bit of it
    # [[0,0,0],[0,0,1],[0,0,2],...,[255,255,253],[255,255,254],[255,255,255]]
    ```

    * comprehensions can be chained for dicts and sets as well
        * not sure when this is useful? 
