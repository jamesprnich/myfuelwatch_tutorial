# myFuelwatch - Virtual Environment

Here we are going to create a [virtual environment](the-basics.md#virtual-environments) on your computer that will be used when creating your myFuelwatch app.

### 1. C**reate virtualenv**

In the folder you wish to create the virtual environment, run the command below

{% code-tabs %}
{% code-tabs-item title="Terminal " %}
```text
JP-MacBook-Pro% virtualenv -p python3 myfuelwatch_venv
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> NOTE: For the remainder of this tutorial the computer name is not included in the examples for simplicity. In the above example the computer name is `JP-MacBook-Pro` . On your computer it will be whatever your computers name is.

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/james/webdev/myfuelwatch_venv/bin/python3.6
Also creating executable in /Users/james/webdev/myfuelwatch_venv/bin/python
Installing setuptools, pip, wheel...done.
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 2. Activate the virtualenv 

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% source myfuelwatch_venv/bin/activate
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Notice, how the prompt within the Terminal changes and now has `(myfuelwatch_venv)` in front of the `%`

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\] \(output\)" %}
```text
(myfuelwatch_venv)% 
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 3. Upgrade pip

We want to make sure you are running the latest version of pip, so we run a command to upgrade it.

{% code-tabs %}
{% code-tabs-item title="Terminal \[virtual env activated\]" %}
```text
(myfuelwatch_venv)% pip install --upgrade pip
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**Next Up:   
**Connect to the Fuelwatch API and display the raw data it gives us.

