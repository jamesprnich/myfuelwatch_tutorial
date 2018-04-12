# Python Itertools.product

The `itertools.product` method is best explained with an example. 

Lets say you have three lists and you want to return a list of all possible combinations of those three lists.

{% code-tabs %}
{% code-tabs-item title="The 3 lists" %}
```python
listone = [1,2,3,4]
listtwo = ['james', 'steven']
listthree = ['blue', 'yellow', 'green']
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Output we want is:" %}
```text
(1, 'James', 'blue')
(1, 'James', 'yellow')
(1, 'James', 'green')
(2, 'James', 'blue')
...and so on
(4, 'steven', 'yellow')
(4, 'steven', 'green')
```
{% endcode-tabs-item %}
{% endcode-tabs %}

You may have already tried to get this result using a lot of for loops and found it quickly overwhelming. The good news is that the `itertools.product` method does this all for us. 

The `itertools.product` method returns an object you can iterate over. For example:

{% code-tabs %}
{% code-tabs-item title="Python Shell" %}
```python
>>> import itertools
>>> animal = ['dog','cat']
>>> number = [5,45,8,9]
>>> color = ['yellow','blue','black']
>>> myproduct = itertools.product(animal, number, color)
>>> for each in myproduct:
...     print(each)
...     
('dog', 5, 'yellow')
('dog', 5, 'blue')
('dog', 5, 'black')
[...we are skipping displaying the middle combinations]
('cat', 9, 'blue')
('cat', 9, 'black')
```
{% endcode-tabs-item %}
{% endcode-tabs %}

There is more to `itertools.product` with documentation available [here](https://docs.python.org/3/library/itertools.html#itertools.product) or just google it :\) 

> The above explanation draws from this post on [Stackoverflow](https://stackoverflow.com/questions/17557223/accessing-elements-of-itertools-product-in-a-for-loop).



