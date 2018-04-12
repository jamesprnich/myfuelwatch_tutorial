# Source control using git

### What is Git?

Simple answer: Git is a version control system. You use it to store your source code. 

### Why use it?

* Maintain versions of your code as you add features or fix bugs
* Easily allow multiple developers to work on your code
* Its the industry standard tool for source control

> An awesome visual guide summarising Git commands is [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/)

### What we are going to cover:

1. Installing Git
2. Creating a Github repository \(repo\)
3. Cloning the Github repo to your computer
4. Adding a file to your repo
5. Committing that file
6. Changing that files content
7. Committing that file with its changes
8. Pushing those commits to Github

### 1. Installing Git

We install Git using brew.

> REMINDER: brew is a command line tool that lets us install software easily.

 Run the following command in your terminal window.

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% brew install git
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Check that Git is installed by typing the following command into your terminal window.

{% code-tabs %}
{% code-tabs-item title="Terminal" %}
```text
% git --version
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Terminal \(output\)" %}
```text
git version 2.6.2
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### 2. Creating a Github Repo

* Go to http://www.github.com
* Sign into Github or create an account if you don't already have one
* Create a repo following these instructions [https://help.github.com/articles/create-a-repo/](https://help.github.com/articles/create-a-repo/)

### 3. Cloning the Github repo to your computer

* Create a folder on your computer called `git_example`
* Follow the instructions here [https://help.github.com/articles/cloning-a-repository/](https://help.github.com/articles/cloning-a-repository/)

### 4. Adding a file to your repo

* pico test.py

git status

git add test.py

git commit -m "dsfdsfsd"

git status

git diff

git clone project 1b

git reset

git log

git pull









