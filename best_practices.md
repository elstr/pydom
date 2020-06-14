# best practices

* Function names should be lowercase, with words separated by underscores as necessary to improve readability.

* Variable names follow the same convention as function names.

## Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

### range
```py
 x = range(1, cant)  # primer arg es donde empieza, el 2do arg es donde termina, y opcional un tercero que es el step
 for n in x:

```
    
### while
```py
while t > 0:
```    

### multiples condiciones
```py
while t > 0 and xxx:
while t > 0 or xxx:
```