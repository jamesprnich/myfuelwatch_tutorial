# myFuelwatch v3 - Using functions \(part1\)

In this section we add the following functionality:

* ability to specify multiple fuel types and regions and generate the Fuelwatch API calls required.

**How does this help us?** The code we have written so far can only handle a single call to the Fuelwatch API but what if we want to query more than one fuel type or region at the same time? The Fuelwatch API does not allow you to specify multiple fuel types or regions, so you must call their API once for each combination of data you want. 

### **1. Modify your python code**

{% code-tabs %}
{% code-tabs-item title="fuelwatch\_tutorial.py" %}
```python
import itertools

def gen_fuelwatch_urls(fueltypes, regions):
    fuelwatch_urls = [
        "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}".format(*i)
        for i in itertools.product(fueltypes, regions)
    ]
    print("# of URLs to process: " + str(len(fuelwatch_urls)))
    return fuelwatch_urls

# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4, ]  # 11 = Brand Diesel, Diesel
regions = [2, ]  # 2 = Broome

fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)
print(fuelwatch_urls)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now we are ready to execute the code and see what happens.

### **2. Run your python code**

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
# of URLs to process: 2
['http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=11&Region=2', 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4&Region=2']
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 3. **So what actually happened here?**

> Only new, changed code is explained below. See earlier tutorial steps for other code explanations.

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch\_tutorial.py" %}
```python
import itertools
```
{% endcode-tabs-item %}
{% endcode-tabs %}

1. Import a library that we are going to use in one of our functions. This is a built in python library, so you do not need to install anything extra.

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch.tutorial.py" %}
```python
def gen_fuelwatch_urls(fueltypes, regions):
    fuelwatch_urls = [
        "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}".format(*i)
        for i in itertools.product(fueltypes, regions)
    ]
    print("# of URLs to process: " + str(len(fuelwatch_urls)))
    return fuelwatch_urls
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> NOTE: Both the [_**itertools.product**_](python-itertools.product.md) and [_**.format\(\*i\)**_](python-.format.md) are explained in detail in previous sections of this tutorial.

This is a function which returns a list of Fuelwatch API URLs. 

1. Define the function and the variables which must be passed to it `def gen_fuelwatch_urls(fueltypes, regions):`
2. Using '`itertools.product`' and '`.format(*i)`' we create a URL for every possible combination of the `fueltypes` and `regions` we passed to the function.
3. Print the number of URL's that were generated `print("# of URLs to process: " + str(len(fuelwatch_urls)))`

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch.tutorial.py" %}
```python
# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4, ]  # 11 = Brand Diesel, Diesel
regions = [2, ]  # 2 = Broome

fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)
print(fuelwatch_urls)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

1. Here we define what data we want to get from the Fuelwatch API `fueltypes = [11, 4,]`and `regions = [2,]` 
2. We call the function we created earlier and pass it the fueltypes and regions we want `fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)` The function returns its results and they are stored in the `fuelwatch_urls` variable.
3. Print the `fuelwatch_urls` list.

**Next Up:   
**Getting the Fuelwatch data for all the URLs generated

