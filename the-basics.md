# The Basics

To complete this tutorial you will need to use a variety of different tools and concepts that may be unfamiliar to you. A brief summary of each of these is included below. 

> This may be a lot to take in initially. It is recommended that you read through and complete this before continuing and then refer back to it when needed as you progress through the tutorial.

### What is the Terminal?

The terminal is an application, which provides a way of giving your computer commands to execute using your keyboard. You run/start the Terminal app just like any other application. 

You will use the terminal a lot to complete this tutorial.

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
%
```
{% endcode-tabs-item %}
{% endcode-tabs %}

You can use the terminal to do things such as:

1. Creating, listing, changing folders or files on your computer
2. Running programs like the Python Shell
3. Running your Python code
4. ...much more

#### Terminal Prompt

The terminal prompt on macOS ends with % by default. It is worth noting this as when you run other programs \(like the Python Shell\) the prompt changes which means you cannot

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
%
```
{% endcode-tabs-item %}
{% endcode-tabs %}

#### Common Terminal Commands

* **List folders and files on your computer.**

 Run the following command in your terminal window.

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% ls
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
file.doc
reports.xls	
reports_folder
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> NOTE: The output above will be different on your computer. This is example output only.

* **Create folders on your computer**
* **Change folders on your computer**

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```
% mkdir testfolder
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Note: there is no output for the `mkdir` command. It can look like nothing has happened

The folder `testfolder` has been created, you can now see that folder using the `ls` command

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% ls
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
testfolder
```
{% endcode-tabs-item %}
{% endcode-tabs %}

The folder we created above is now listed. You can now change into that folder.

First, lets show what folder you are currently in by using the `pwd` command

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% pwd
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
/Users/james/Documents/fuelwatch_tutorial
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> NOTE: The folder path you see above will vary depending on your computer.

Second, lets change the current folder using the `cd` command

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% cd testfolder
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Now, run the `pwd` command again

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% pwd
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```
/Users/james/Documents/fuelwatch_tutorial/testfolder
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> NOTE: The folder path you see above will vary depending on your computer.

You can see how the folder path now includes the `testfolder `folder. 

### What is Python?

Python is a programming language. You will be writing python code in this tutorial. More info is available [here](https://www.python.org/about/).

### What is the Python Shell?

The Python shell is an interactive interface for writing python code and executing it a line at a time. You will typically use it for learning purposes or perhaps to troubleshoot some code.

The Python shell is started from within the Terminal by typing`python` at the terminal prompt.

### Virtual Environments

Think of this as a little isolated area within your computer, used just for the app you are about to create. This allows you to work on many apps or projects without the risk of them interfering with each other. We will create a virtual environment for the myFuelwatch app. More info is available [here](https://virtualenv.pypa.io/en/stable/).

### PIP

Pip is a tool for installing and managing Python packages. We will use pip to install some of the additional software we need when working through this tutorial. More info is available [here](https://pip.pypa.io/en/stable/user_guide/). 

### API

API stands for Application Programming Interface. We will be using the Fuelwatch API to get information about fuel prices. The API provides a standard, programmable way to access information. More info is available [here](https://www.mulesoft.com/resources/api/what-is-an-api).

### XML

XML stands for Extensible Markup Language. In this tutorial, the fuel data provided by Fuelwatch is in XML format. Think of it like a file, with standardised formatting that contains information. The standard formatting allows a computer program to read information out of the file. The example XML file shown below is what was returned by the Fuelwatch API.

{% code-tabs %}
{% code-tabs-item title="Example XML" %}
```markup
<rss version="2.0">
    <channel>
        <title>FuelWatch Prices For Cloverdale</title>
        <ttl>720</ttl>
        <link>http://www.fuelwatch.wa.gov.au</link>
        <description>09/04/2018 - Cloverdale</description>
        <language>en-us</language>
        <copyright>Copyright 2005 FuelWatch. All Rights Reserved.</copyright>
        <lastBuildDate>
            Mon Apr 09 12:45:04 WST 2018Mon Apr 09 12:45:04 WST 2018
        </lastBuildDate>
        <image>
            <url>/fuelwatch/art/fuelwatch-logo.gif</url>
            <title>FuelWatch</title>
            <link>http://www.fuelwatch.wa.gov.au</link>
        </image>
        <item>
            <title>129.9: Coles Express Cloverdale</title>
            <description>
                Address: 223 Belmont Ave (Cnr Wright St), CLOVERDALE, Phone: (08) 9277 1660
            </description>
            <brand>Coles Express</brand>
            <date>2018-04-09</date>
            <price>129.9</price>
            <trading-name>Coles Express Cloverdale</trading-name>
            <location>CLOVERDALE</location>
            <address>223 Belmont Ave (Cnr Wright St)</address>
            <phone>(08) 9277 1660</phone>
            <latitude>-31.965057</latitude>
            <longitude>115.933164</longitude>
            <site-features>,</site-features>
        </item>
    </channel>
</rss>
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Source Code

When we say source code we are referring to the code you as the developer writes. A simple example of source code is show below.

{% code-tabs %}
{% code-tabs-item title="Example Source Code" %}
```python
print("hello world")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Brew

Homebrew is a free and open-source software package management system that makes it easy to install software on macOS. You use the Terminal to run brew commands. More info is available [here](https://brew.sh/).

**Next Up:   
**Setting up your computer for coding

