# myFuelwatch v2 - Sorting lists

In this section we add the following functionality:

* add the fuel prices to a list
* sort the list
* print the data

**How does this help us?** So we can show the cheapest fuel first if we want to!

**1. Modify your python code**

{% code-tabs %}
{% code-tabs-item title="fuelwatch\_tutorial.py" %}
```python
from lxml import objectify
import requests

api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"

fuelprice_data = requests.get(api_url)

root = objectify.fromstring(fuelprice_data.content)

list_of_prices = []
for each_item in root.channel.item:
    list_of_prices.append(each_item.price)
    
list_of_prices.sort(key=int, reverse=False)
print("List Sorted: " + str(list_of_prices))

list_of_prices.sort(key=int, reverse=True)
print("List Sorted (reversed): " + str(list_of_prices))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now we are ready to execute the code and see what happens.

**2. Run your python code**

 Run your python code by typing the following command into your terminal window.

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
(myfuelwatch_venv)% python fuelwatch_tutorial.py
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Output/result:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
List Sorted: [127.5, 139.9, 146.9, 146.9, 146.9, 146.9, 146.9, 146.9, 149.9, 149.9]
List Sorted (reversed): [149.9, 149.9, 146.9, 146.9, 146.9, 146.9, 146.9, 146.9, 139.9, 127.5]
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**So what actually happened here?**

> Only new, changed code is explained below. See earlier tutorial steps for other code explanations.

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch\_tutorial.py" %}
```python
list_of_prices = []
for each_item in root.channel.item:
    list_of_prices.append(each_item.price)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

1. Create an empty list variable to store the price data `list_of_prices = []`
2. Loop through the `root` object: `for each_item in root.channel.item:`
3. Append each price to the list variable: `list_of_prices.append(each_item.price)`

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch.tutorial.py" %}
```python
list_of_prices.sort(key=int, reverse=False)
print("List Sorted: " + str(list_of_prices))

list_of_prices.sort(key=int, reverse=True)
print("List Sorted (reversed): " + str(list_of_prices))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Sort the price data using the `sort` method. We pass the parameters `key=int` as we are passing it an integer \(price in this case\) to sort on. 

**Next Up:   
**Sorting python dictionaries

