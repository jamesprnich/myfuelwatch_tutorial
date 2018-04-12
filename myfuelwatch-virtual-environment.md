# myFuelwatch - Virtual Environment

Here we are going to create a virtual environment on your computer that will be used when creating your myFuelwatch app.

### 1. C**reate virtualenv**

{% code-tabs %}
{% code-tabs-item title="Terminal " %}
```text
% create virtualenv.....sdfsdfdsf
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 2. Activate the virtualenv 

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
????
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 3. Update pip

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
(virtuenv)% update pip
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 4. Install dependencies

We will use other software to make it quick and easy for us to complete certain tasks. 

* We use a python module called `requests` to connect to the FuelWatch API.
* We use a python module called `lxml` to parse/read the XML file that the FuelWatch API sends to us.

**Next Up:   
**Connect to the Fuelwatch API and display the raw data it gives us.

