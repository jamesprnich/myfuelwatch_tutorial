# myFuelwatch v2 - Sorting dictionaries

In this section we add the following functionality:

* create a dictionary for each bit of fuel data and add it to a list
* sort the list using the data in the dictionaries
* print the sorted data

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

list_of_dicts = []
for each_item in root.channel.item:
    dict_data = {
                'Price': each_item.price.text,
                'Location': each_item.location.text,
                'Address': each_item.address.text,
                'Phone': each_item.phone.text,
                'Brand': each_item.brand.text,
                'Date': each_item.date.text
            }
    list_of_dicts.append(dict_data)

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now we are ready to execute the code and see what happens.

**2. Run your python code**

 Run your python code by typing the following command into your terminal window.

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
% python fuelwatch_tutorial.py
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Output/result:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
List Sorted: [127.5, 139.9, 146.9, 146.9, 146.9, 146.9, 146.9, 146.9, 149.9, 149.9]
List Sorted (reversed): [149.9, 149.9, 146.9, 146.9, 146.9, 146.9, 146.9, 146.9, 139.9, 127.5]
Dict Sorted: [{'Price': '127.5', 'Location': 'KEWDALE', 'Address': '410-412 Orrong Rd', 'Phone': '(08) 9451 6245', 'Brand': 'United', 'Date': '2018-04-04'}, {'Price': '139.9', 'Location': 'REDCLIFFE', 'Address': '419 Great Eastern Hwy', 'Phone': '(08) 9277 9755', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'BELMONT', 'Address': 'Cnr Belvidere St & Keymer St', 'Phone': '(08) 9479 4557', 'Brand': 'Puma', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'BELMONT', 'Address': '303 Great Eastern Hwy', 'Phone': '(08) 9277 2887', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': 'Cnr Kewdale Rd & Fenton St', 'Phone': '(08) 9353 2757', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': '549 Abernethy Rd', 'Phone': '(08) 9353 6945', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': '23 Kewdale Rd', 'Phone': '(08) 9458 8622', 'Brand': 'Puma', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'RIVERVALE', 'Address': '111 Great Eastern Hwy', 'Phone': '(08) 9277 2886', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '149.9', 'Location': 'CLOVERDALE', 'Address': '223 Belmont Ave (Cnr Wright St)', 'Phone': '(08) 9277 1660', 'Brand': 'Coles Express', 'Date': '2018-04-04'}, {'Price': '149.9', 'Location': 'KEWDALE', 'Address': '518 Abernethy Rd (Cnr Kewdale Rd)', 'Phone': '(08) 9353 1455', 'Brand': 'Coles Express', 'Date': '2018-04-04'}]
Dict Sorted (reversed): [{'Price': '149.9', 'Location': 'CLOVERDALE', 'Address': '223 Belmont Ave (Cnr Wright St)', 'Phone': '(08) 9277 1660', 'Brand': 'Coles Express', 'Date': '2018-04-04'}, {'Price': '149.9', 'Location': 'KEWDALE', 'Address': '518 Abernethy Rd (Cnr Kewdale Rd)', 'Phone': '(08) 9353 1455', 'Brand': 'Coles Express', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'BELMONT', 'Address': 'Cnr Belvidere St & Keymer St', 'Phone': '(08) 9479 4557', 'Brand': 'Puma', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'BELMONT', 'Address': '303 Great Eastern Hwy', 'Phone': '(08) 9277 2887', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': 'Cnr Kewdale Rd & Fenton St', 'Phone': '(08) 9353 2757', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': '549 Abernethy Rd', 'Phone': '(08) 9353 6945', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'KEWDALE', 'Address': '23 Kewdale Rd', 'Phone': '(08) 9458 8622', 'Brand': 'Puma', 'Date': '2018-04-04'}, {'Price': '146.9', 'Location': 'RIVERVALE', 'Address': '111 Great Eastern Hwy', 'Phone': '(08) 9277 2886', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '139.9', 'Location': 'REDCLIFFE', 'Address': '419 Great Eastern Hwy', 'Phone': '(08) 9277 9755', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '127.5', 'Location': 'KEWDALE', 'Address': '410-412 Orrong Rd', 'Phone': '(08) 9451 6245', 'Brand': 'United', 'Date': '2018-04-04'}]
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**So what actually happened here?**

> Only new, changed code is explained below. See earlier tutorial steps for other code explanations.

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch\_tutorial.py" %}
```python
list_of_dicts = []
for each_item in root.channel.item:
    dict_data = {
                'Price': each_item.price.text,
                'Location': each_item.location.text,
                'Address': each_item.address.text,
                'Phone': each_item.phone.text,
                'Brand': each_item.brand.text,
                'Date': each_item.date.text
            }
    list_of_dicts.append(dict_data)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

1. Create an empty list variable to store the dictionaries we are about to create`list_of_dicts = []`
2. Loop through the `root` object: `for each_item in root.channel.item:`
3. Create a dictionary for each bit of fuel data
4. Append each dictionary to the list variable: `list_of_dicts.append(dict_data)`

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch.tutorial.py" %}
```python
list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Sort the price data using the `sorted` function.  **$\#$ Need more explanation added $\#$**

**Next Up:   
**Using functions

