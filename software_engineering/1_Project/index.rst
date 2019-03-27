
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

1. Structure your project
=========================

#. Have a clean structure
#. A word about licenses
#. Coding convention

   #. PEP8
   #. PEP20

#. Version control system - git

----

Have a clean structure
----------------------

- Separate library from scripts:

  * libraries are reusable

- Separate GUI from calculation:

  *  Otherwise maintenance becomes a nightmare
  *  allows to change the front-end
  *  allows to access to core function without the GUI
  *  simplify unit tests

- Separate I/O from calculation

- Define a license for your work.

Presenter Notes
...............

Will also help you to :

- find back your code
- avoid code duplication

License : otherwise can't be distributed or reused

----

A word about Licenses
---------------------

According to the French law, one should distinguish authorship from ownership:

 - Authorship is inalienable: your work becomes public domain 50 years after
   your death.
 - ESRF, your employer, owns the code you may have written during your contract
   (unless you can prove this development has no correlation with your work)

Licenses define how a piece of software can be used (and sometimes what for).
None of them claim any liability of the author.

----

One can define 2 categories:
----------------------------

- Proprietary licenses

  * Commercial licenses: one needs to purchase a license to use the code
  * Academic licenses: free for academic research

- Open source licenses:

  * GPL like enforces the distribution of source code
  * LGPL like enforces the publication of modified code
  * MIT/BSD which provides the name of the author for information
    (for scientific citation)

The Python scientific stack has a BSD-like licenses.

Defining licenses for your developments is important as the beamline can not
build code on top of unlicensed or proprietary work without explicit license
agreement.

Presenter Notes
...............

Warning : code under MIT/BSD/Apache licenses can be integrated under proprieteray licences, redistributed...

Why MIT instead of GPL or LGPL?
    -> GPL enforces publication of source code
    -> LGPL enforces publication of any modification of the original work
Why MIT instead of BSD ?
    -> Different version of BSD, complexify a bit
Why MIT instead of Apache 2.0 ?
    -> MIT is shorter and simpler

----

Coding convention
=================

----

Python 2 end of support
-----------------------

By 2020, the `support of Python2 will end <https://pythonclock.org/>_`.
All your projects should be python3 based.

Supporting Python3 is a must have today.

Look at the download statistics of projects like
`WinPython <https://sourceforge.net/projects/winpython/files/>`_: about 5900 downloads/week for Python_3.x vs 324 for Python_2.7

You can use the `six library <https://pypi.python.org/pypi/six>`_ to provide code that
runs both under Python2 and Python3.

Presenter Notes
...............

python-future is a higher-level compatibility layer than six that includes more backported functionality from Python 3, more forward-ported functionality from Python 2

----

Coding convention: `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_
----------------------------------------------------------------------

- Wrap lines at 79 char.
- Indent with 4 spaces.
- Put spaces around arguments (except in function declaration).
- English docstrings and triple quoted.
- One single import per line.
- Variable, method, modules name should be lower_case
  (with underscore, only if needed).
- Constant should be UPPER_CASE (with underscores).
- Class names should be CamelCased.
- Single letter variable should be limited to loop indexes.
- One single statement per line
- Two empty lines between top-level objects, only one later.

`PEP 7 <https://www.python.org/dev/peps/pep-0007/>`_: Style Guide for C Code

Presenter Notes
...............

PEP : python enhancement proposal
Why PEP ? :

- insure code homogeneity
- insure readability
- insure maintenance / avoid some classical errors

----

Zen of Python: `PEP20 <https://www.python.org/dev/peps/pep-0020/>`_
...................................................................

.. code-block:: python

   import this

::

 Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 Special cases aren't special enough to break the rules.
 Although practicality beats purity.
 Errors should never pass silently.
 Unless explicitly silenced.
 In the face of ambiguity, refuse the temptation to guess.
 There should be one-- and preferably only one --obvious way to do it.
 Although that way may not be obvious at first unless you're Dutch.
 Now is better than never.
 Although never is often better than *right* now.
 If the implementation is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
 Namespaces are one honking great idea -- let's do more of those!

----

Tools
-----

* `flake8 <https://pypi.python.org/pypi/flake8>`_
* `pylint <https://www.pylint.org/>`_
* `modernize <https://pypi.python.org/pypi/modernize>`_
* `autopep8 <https://pypi.python.org/pypi/autopep8>`_
* `landscape.io <https://landscape.io/>`_: `Example <https://landscape.io/github/silx-kit/silx/>`_
* IDE

  - `pyDev (eclipse) <http://www.pydev.org/>`_
  - `pyCharm <https://www.jetbrains.com/pycharm/>`_

----

Version Control System
----------------------

.. image:: http://www.phdcomics.com/comics/archive/phd101212s.gif
   :alt: Why use a version control system?
   :align: center
   :width: 400

Image from http://phdcomics.com/comics/archive_print.php?comicid=1531

----

Git version control
...................

Git is the current (2019) standard, it has replaced SVN, CVS, ...

If you have heard of any of them, the concepts in Git are similar while offering a lot of flexibility.


* starting commands
    * git *clone <url>* to copy another existing (remote) project
    or

    * git *init* to initiate a new project

----


github and gitlab
.................

**github.com** and **gitlab.esrf.fr** provides free git-hosting for open-source project and
encourages collaboration using forks of projects.

The main advantages are:

 - `Offer a fixed pipeline based on *Pull request* <https://help.github.com/articles/using-pull-requests/>`_
 - Many tutorials on `gitHub <https://guides.github.com/>`_ and `gitlab <https://docs.gitlab.com/ee/gitlab-basics/>`_
 - Web page hosting for projects
 - over the years a cluster of services, directly have pop up to help developers (`Travis <https://github.com/marketplace/travis-ci>`_, `AppVeyor <https://github.com/marketplace/appveyor>`_)

----

github vs gitlab
................

- github should bring to your project an `Higher visibility compared to other hosting (in 2017) <http://software.ac.uk/resources/guides/choosing-repository-your-software-project>`_
- github is usually one step ahead of gitlab on features and usability
- Activities on github are monitored by head-hunters and can be useful for professional placement.
- You can select a privacy level for your gitlab projects. Public projects can be seen from outside: https://gitlab.esrf.fr/public

.. image:: images/gitlab_privacy.png
    :align: center

----

Different types of workflow
...........................

They are different workflows with git:

* `centralized workflow  <https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow>`_
* `feature branch workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow>`_
* `gitflow workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_
* `forking workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow>`_

Presenter Notes
...............

- centralized : a single point of entry 'central repository'. Let each users to deal with synchronization

- gitflow : strict management of branches. One branch per:
    - releases
    - each feature
    - fix

----

Different types of workflow
...........................

This is not the goal today to see all the different type of workflows.
But for the hands on session today we will consider to be in the 'forking flow'.


.. image:: images/fork_workflow_remote.png
    :align: center


Presenter Notes
...............

The idea is that each developer can interact with other from his own fork.
Each developer can request to merge some modifications (feature, bug fix...) with others: this is a pull request

Presenter Notes
...............

- simplify branch forking
- Always keep upstream branch ready for deployment with features and fixes
- Each new branch starts from the master (up to date)
- Use merge request for each new feature


----


Hands on: create a new git project
----------------------------------

Test case: project life.

--- initial project ---

We create a simple git project only containing one file: polynom.py. We now want to
modify it.

In order to create this git project we just:

create an empty folder to create the project


.. code-block:: bash

    mkdir pypolynom
    cd pypolynom

create the directory which will contains the source code


.. code-block:: bash

    mkdir pypolynom

create one source code file


.. code-block:: bash

    touch pypolynom/polynom.py


----

Hands on: create a new git project(2)
-------------------------------------

then add code to the file

.. code-block:: bash

    ...

init the git project file

.. code-block:: bash

    git init

then create a new project from `gitlab <http://gitlab.esrf.fr/>`_ or `github <http://github.com/>`_

.. code-block:: bash
    ...

you can now register the gitlab / github project url to the current git project

.. code-block:: bash

    git remote add origin git@gitlab.esrf.fr:silx/silx-trainings/pypolynom.git
    git push origin master


----


Hands on: fork an existing project
..................................

fork the project from the webinterface of gitlab or github.
This will provide you an url to the fork.

.. class:: center

    |fork-gitlab| |fork-github|

.. |fork-gitlab| image:: images/gitlab-fork.png
   :width: 45%

.. |fork-github| image:: images/github-fork.png
   :width: 45%


Then clone the project:

.. code-block:: bash

    git clone git@gitlab.esrf.fr:[my_id]/pypolynom_completed.git


And add some remote repository:


.. code-block:: bash

    git remote add upstream git@gitlab.esrf.fr:silx/silx-trainings/pypolynom.git


----


branch
......

new features / bug fix / improvements will be developed in a dedicated branch.
You can have an infinite number of branch on each repository.

The history of the branch evolve with commits (see next slides).
Once the modifications are made they can be proposed to be merged on `upstream` repository and merge into a branch.


.. image:: images/git_branch.png
    :align: center

----

Branches commands
.................

* *fetch <branch>* retrieve history from another branch
* *merge <branch>* : merge history of <branch> into the current branch
* *checkout <branch>* : move to another branch.
* *checkout -b <branch>* : create a new branch

Note : *pull* command is grouping *fetch* and *merge*

Presenter Notes
...............

Default parameters origin/master rot git actions

----

Hands on: create a new branch
.............................

The goal is to create a new branch for making some modifications on the source code and propose those modification into the upstream repository.

create a new branch branch_my_name

.. code-block:: bash

    git checkout -b branch_my_name

Then modify the source code, creating a new function using `polynom` function for example.



----

Git actions
...........

To made modification locally you will have to follow the current process :

1. *add* files to the list of tracked files
2. *commit* the files, locally
3. *push* your changes to a remote repository

The cycle 1-2-3 is the normal development cycle for a local project.

Any git repository contains all the history of the project, i.e all
commits with authors, data time, file changed, and the chain of commits called *branch*

----

Some useful git commands
........................

* *status* : show the working tree status (branch name, file modified, added...)
* *log* : show commits logs
* *diff* : show changes between commits

----

Hands on: create a pull request
...............................


* check the current status of your project

.. code-block:: bash

    git status ./

* create your first commit:
    * add the modification you want to embed
    * create a commit from those

* push those modifications to the upstream repository and create a pull-request
* ask one of your neighbour to review this PR and merge it on the upstream repository
* retrieve the modifications to your own master branch

----

Git - Interact with another repository
......................................

To interact with a remote repository : 

* *remote* : manage tracked repositories
* *remote add name url* : Adds a remote named <name> for the repository at <url>

Then you can retrieve commits from those repositories:

* *fetch <repository> <branch>* retrieve history from another branch
* *merge <repository>/<branch>* : merge history of <branch> into the current branch

The cycle 1-2 is the normal cycle to retrieve commits.


Presenter Notes
...............

git actions have defaults parameters in order to simplify commands and to fit sith workflows
For example *fetch* and *merge* have default values for:

- repository --> origin
- branch  --> master

----


Hands on: remote repository
...........................

* add one an other `fork repository` and fetch it.
* move to one of its branch and log history of the branch.

----

Some tutorials and utils for git/github
.......................................

* `Comprehensive tutorial <http://gitref.org>`_
* `Cheat sheet from Github <https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf>`_
* `simple Cheat sheet <http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf>`_
* `list of default .gitignore for several languages <https://github.com/github/gitignore>`_

----

Contribution in OSS
...................

If your project becomes popular, you may have external contributors...
or you might want to contribute to other projects.

How to contribute to an Open Source project is presented in
`this document <http://scikit-image.org/docs/stable/contribute.html>`_
for scikit-image.

----

Take home message
-----------------

#. Keep your code tidy so that you can still understand it in 6 month
#. Define a license so that it can be re-used.
#. Stick to the PEP8 so that it looks *Pythonic*
#. Use a VCS: GitHub made *git* useable for human beings.
