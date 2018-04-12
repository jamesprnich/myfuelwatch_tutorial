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

> NOTE: The output above will be different. This is example output only.

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

### What is the Python Shell?

The Python shell is an interactive interface for writing python code and executing it a line at a time. You will typically use it for learning purposes or perhaps to troubleshoot some code.

The Python shell is started from within the Terminal by typing`python ` at the terminal prompt.

### Virtual Environments

Think of this as a little isolated environment within your computer, used just for the app you are about to create

### PIP

What is PIP?

### API

API stands for Application Programming Interface. 

### XML

What is XML?

### Source Code

What is Source code...?

### Brew

Homebrew is a free and open-source software package management system that makes it easy to install software on macOS. [https://brew.sh/](https://brew.sh/)

