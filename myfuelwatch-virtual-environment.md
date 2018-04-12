# myFuelwatch - Virtual Environment

Here we are going to create a virtual environment on your computer that will be used when creating your myFuelwatch app.

**create virtualenv**

update pip

#### Install dependencies using PIP

We will use other software to make it quick and easy for us to complete certain tasks.

* We use a python module called '`requests`' to connect to the FuelWatch API.
* We use a python module called '`lxml`' to parse/read the XML file that the FuelWatch API sends to us.

Terminal:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual environment\]" %}
```text
%(venv) pip install requests
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Result/Output:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual environment\] \(output\)" %}
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

Terminal:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual environment\]" %}
```text
%(venv) pip install lxml
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Result/Output:

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual environment\] \(output\)" %}
```text
  Downloading lxml-4.2.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (8.7MB)
    100% |████████████████████████████████| 8.7MB 101kB/s 
Installing collected packages: lxml
Successfully installed lxml-4.2.1
```
{% endcode-tabs-item %}
{% endcode-tabs %}

