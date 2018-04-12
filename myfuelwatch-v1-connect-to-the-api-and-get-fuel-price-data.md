# myFuelwatch v1 - Connect to the API and get fuel price data

In this section we add the following functionality:

* connect to the fuelwatch API
* get the returned fuel data
* print the fuel data 

**How does this help us?** It gets us the fuel data we want, which is the foundation of our app.

### **1. Create a python file & write some python code**

Because we haven't yet written any code we have to first create a file called `fuelwatch_tutorial.py` 

Now enter the code shown below.

{% code-tabs %}
{% code-tabs-item title="fuelwatch\_tutorial.py" %}
```python
import requests

api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"

fuelprice_data = requests.get(api_url)
print(fuelprice_data.content)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 2. Install the `requests` module using PIP

* Load a terminal window and activate the myFuelwatch virtual environment.

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% source bin/activate
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
(myfuelwatch_venv)% 
```
{% endcode-tabs-item %}
{% endcode-tabs %}

* Install requests using PIP

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
(myfuelwatch_venv)% pip install requests
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
Collecting requests
  Using cached requests-2.18.4-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests)
  Using cached idna-2.6-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2018.1.18-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3<1.23,>=1.21.1 (from requests)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Installing collected packages: idna, certifi, chardet, urllib3, requests
Successfully installed certifi-2018.1.18 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now we are ready to execute the code and see what happens.

### 3**. Run your python code**

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
b'<?xml version="1.0" encoding="UTF-8"?>\r\n<rss version="2.0"><channel><title>FuelWatch Prices For Cloverdale</title><ttl>720</ttl><link>http://www.fuelwatch.wa.gov.au</link><description>27/03/2018 - Cloverdale</description><language>en-us</language><copyright>Copyright 2005 FuelWatch. All Rights Reserved.</copyright><lastBuildDate>Tue Mar 27 15:40:57 WST 2018Tu
```
{% endcode-tabs-item %}
{% endcode-tabs %}

You can see above an small part of what was returned. This contains the fuel pricing data for the API query we sent to theFuelwatch.gov.au server. The data returned by the API is in XML format.

### 4. **So what actually happened here?**

1. Import the `requests` module so we can use it to connect to the Fuelwatch API
2. Specify the URL we want to use for the Fuelwatch API and assign it to a variable `api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"`
3. Get the fuel price data returned from the Fuelwatch API: `fuelprice_data = requests.get(api_url)`
4. Print the data returned by the Fuelwatch API:`print(fuelprice_data.content)`

**Next Up:   
**Making the returned fuelwatch data more readable

