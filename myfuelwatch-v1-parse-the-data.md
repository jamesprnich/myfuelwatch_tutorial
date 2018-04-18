# myFuelwatch v1 - Parse the data

In previous steps we were able to get the data from the Fuelwatch API in in XML format and now we want to parse \(read\) that data into an easier format so we can manipulate it easily. We do that with the use of the `objectify` which is part of the `lxml` Python module.

### **1. Modify your python code**

{% code-tabs %}
{% code-tabs-item title="fuelwatch\_tutorial.py" %}
```python
import requests
from lxml import objectify

api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"

fuelprice_data = requests.get(api_url)

root = objectify.fromstring(fuelprice_data.content)

for each_item in root.channel.item:
    print(each_item.title)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> We added an import from the lxml python module but you may not have already installed it into your virtual environment.

### 2. Install the `lxml` module using PIP

* Load a terminal window and [activate](myfuelwatch-virtual-environment.md#2.-activate-the-virtualenv) the myFuelwatch virtual environment \(or continue in the same Terminal window if you already have it open from the previous step\)
* Install lxml using PIP

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
(myfuelwatch_venv)% pip install lxml
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
  Downloading lxml-4.2.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (8.7MB)
    100% |████████████████████████████████| 8.7MB 101kB/s 
Installing collected packages: lxml
Successfully installed lxml-4.2.1
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now we are ready to execute the code and see what happens.

### 3**. Run your python code**

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
124.7: United Kewdale
139.9: BP Redcliffe
149.9: Caltex StarMart Belmont
149.9: Coles Express Cloverdale
149.9: Caltex StarMart Kewdale
149.9: Coles Express Kewdale
149.9: BP Kewdale
149.9: Caltex StarMart Rivervale
151.9: Puma Belmont
151.9: Puma Kewdale
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 4**. So what actually happened here?**

1. Get the fuel price data from the Fuelwatch API: `fuelprice_data = requests.get(api_url)`
2. Convert the XML string \(fuel price data\) into a python object: `root = objectify.fromstring(fuelprice_data.content)`
3. Loop through the `root` object: `for each_item in root.channel.item:`
4. Print each items \(Fuel price\) title:`print(each_item.title)`

**Next Up:   
**Python Lists

