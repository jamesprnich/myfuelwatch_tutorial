# myFuelwatch v3 - Using functions \(part2\)

In this section we add the following functionality:

* ability to combine data from multiple Fuelwatch API calls

**How does this help us?** We call the Fuelwatch API multiple times now for multiple fuel types and we need combine all the results together.

**1. Modify your python code**

{% code-tabs %}
{% code-tabs-item title="fuelwatch\_tutorial.py" %}
```python
from lxml import objectify
import requests
import itertools

def gen_fuelwatch_urls(fueltypes, regions):
    fuelwatch_urls = [
        "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}".format(*i)
        for i in itertools.product(fueltypes, regions)
    ]
    print("# of URLs to process: " + str(len(fuelwatch_urls)))
    return fuelwatch_urls

def get_fueldata(fueltypes, regions):
    fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)

    list_of_dicts = []
    for each_url in fuelwatch_urls:
        fuelprice_data = requests.get(each_url)

        root = objectify.fromstring(fuelprice_data.content)

        if hasattr(root.channel, 'item'):
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
    return list_of_dicts

# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4,]  # 11 = Brand Diesel
regions = [2, ]  # 2 = Broome

# Call the function to get fuel data
list_of_dicts = get_fueldata(fueltypes, regions)

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
{% code-tabs-item title="Terminal" %}
```text
% python fuelwatch_tutorial.py
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Output/result:

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
# of URLs to process: 2
Dict Sorted: [{'Price': '149.9', 'Location': 'BROOME', 'Address': '49 Reid Rd', 'Phone': '(08) 9192 8181', 'Brand': 'United', 'Date': '2018-04-04'}, {'Price': '153.9', 'Location': 'BROOME', 'Address': 'Broome Boulevard Shopping Centre', 'Phone': '(08) 9192 7909', 'Brand': 'Caltex Woolworths', 'Date': '2018-04-04'}, {'Price': '153.9', 'Location': 'BROOME', 'Address': 'Cnr Hamersley St & Napier Tce', 'Phone': '(08) 9192 1702', 'Brand': 'Coles Express', 'Date': '2018-04-04'}, {'Price': '155.9', 'Location': 'BROOME', 'Address': 'Lot 345 Mavis St', 'Phone': '(08) 9192 1574', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '158.5', 'Location': 'BROOME', 'Address': '1 Guy St', 'Phone': '(08) 9193 7833', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '159.9', 'Location': 'BROOME', 'Address': 'Cnr Frederick St & Coghlan St', 'Phone': '(08) 9193 5517', 'Brand': 'BP', 'Date': '2018-04-04'}]
Dict Sorted (reversed): [{'Price': '159.9', 'Location': 'BROOME', 'Address': 'Cnr Frederick St & Coghlan St', 'Phone': '(08) 9193 5517', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '158.5', 'Location': 'BROOME', 'Address': '1 Guy St', 'Phone': '(08) 9193 7833', 'Brand': 'BP', 'Date': '2018-04-04'}, {'Price': '155.9', 'Location': 'BROOME', 'Address': 'Lot 345 Mavis St', 'Phone': '(08) 9192 1574', 'Brand': 'Caltex', 'Date': '2018-04-04'}, {'Price': '153.9', 'Location': 'BROOME', 'Address': 'Broome Boulevard Shopping Centre', 'Phone': '(08) 9192 7909', 'Brand': 'Caltex Woolworths', 'Date': '2018-04-04'}, {'Price': '153.9', 'Location': 'BROOME', 'Address': 'Cnr Hamersley St & Napier Tce', 'Phone': '(08) 9192 1702', 'Brand': 'Coles Express', 'Date': '2018-04-04'}, {'Price': '149.9', 'Location': 'BROOME', 'Address': '49 Reid Rd', 'Phone': '(08) 9192 8181', 'Brand': 'United', 'Date': '2018-04-04'}]
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**So what actually happened here?**

> Only new, changed code is explained below. See earlier tutorial steps for other code explanations.

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch\_tutorial.py" %}
```python
def get_fueldata(fueltypes, regions):
    fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)

    list_of_dicts = []
    for each_url in fuelwatch_urls:
        fuelprice_data = requests.get(each_url)

        root = objectify.fromstring(fuelprice_data.content)

        if hasattr(root.channel, 'item'):
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
    return list_of_dicts
```
{% endcode-tabs-item %}
{% endcode-tabs %}

This is a function which returns a list of dictionaries containing fuel data. 

1. Define the function and the variables which must be passed to it `def get_fueldata(fueltypes, regions):`
2. Call the function which will generate a list of the Fuelwatch API URLs to use `fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)`
3. Create an empty list that will contain all our combined fuel data `list_of_dicts = []`
4. We now loop through each of the Fuelwatch API URLs that was returned in the above step. `for each_url in fuelwatch_urls:`
5. The code is now similar to that which we have used previously however there is one key difference if `hasattr(root.channel, 'item'):`
6. The `hasattr` is used to check if any data exists. Sometimes the Fuelwatch API may return no fuel data and without this check, the code would error. 

{% code-tabs %}
{% code-tabs-item title="Excerpt from fuelwatch\_tutorial.py" %}
```python
# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4,]  # 11 = Brand Diesel
regions = [2, ]  # 2 = Broome

# Call the function to get fuel data
list_of_dicts = get_fueldata(fueltypes, regions)

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

1. Here we define what data we want to get from the Fuelwatch API `fueltypes = [11, 4,]`and `regions = [2,]` 
2. We call the function we created earlier and pass it the fuel types and regions we want `list_of_dicts = get_fueldata(fueltypes, regions).` The function returns its results and they are stored in the `list_of_dicts` variable.
3. Sort the price data using the `sorted` method.  **$\#$ Need more explanation added $\#$**
4. Print the results

**Next Up:   
**Outputting the results to HTML

