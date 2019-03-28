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
- feature branch workflow: each new feature should take place in a dedicated branch
- gitflow : strict management of branches designed for releases. One branch per:
    - releases
    - each feature
    - fix

----

forking workflow
................

This is not the goal today to see all the different type of workflows.
But for the hands on session today we will consider to be in the 'forking flow'.


.. image:: images/fork_workflow_remote.png
    :align: center

.. image:: images/github-workflow.png
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

Example: create a new git project
---------------------------------

The goal is to create a git project from a single source file: polynom.py

In order to create this git project we:

1. create an empty folder where to create the project


.. code-block:: bash

    mkdir pypolynom
    cd pypolynom

2. create the directory which will contains the source code file(s)


.. code-block:: bash

    mkdir pypolynom

3. add your source code file(s)


.. code-block:: bash

    touch pypolynom/polynom.py


.. note:: For those which intend to create a new git project from existing source code you can follow the same procedure.


----

Example: create a new git project (2)
-------------------------------------

init the git project file (from the root directory)

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


Now each person will create his own repository.


.. image:: images/github-workflow.png
    :align: center


----

Hands on: fork an existing project
..................................

fork the project from the webinterface of gitlab or github.
This will provide you an url to your personal repository.

.. class:: center

    |fork-gitlab| |fork-github|

.. |fork-gitlab| image:: images/gitlab-fork.png
   :width: 45%

.. |fork-github| image:: images/github-fork.png
   :width: 45%


Then clone the project:

.. code-block:: bash

    git clone git@gitlab.esrf.fr:[my_id]/pypolynom_completed.git


And add the gitlab / github repository:


.. code-block:: bash

    git remote add upstream git@gitlab.esrf.fr:silx/silx-trainings/pypolynom.git

----

branches
........

We will consider the case where each new features, bug fix or improvements will be developed in a dedicated branch.

The history of the branch evolve with a serie of commits (see next slides).

Once the modifications are made they can be proposed to be merged on an other branch. This is a Pull request.

The branch can be part of different repositories.

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

Default parameters are usually origin/master

----

Hands on: create a new branch
.............................

The goal is to:

* create a new branch
* make some modifications on the source code

1. create a new branch branch_my_name

.. code-block:: bash

    git checkout -b branch_my_name

2. Then modify the source code, creating a new function using `polynom` function for example.

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

Hands on: create a commit
.........................


* check the current status of your project

.. code-block:: bash

    git status ./

* create your first commit:
    * add the modification you want to embed
    * create a commit from those

----

Hands on: create pull request
.............................

Now we want to merge those modifications into the original gitlab/github repository.


.. image:: images/github-workflow.png
    :align: center
    :width: 40%

1. Push those modifications on your personal repository.

.. code-block:: bash
    git push origin <branch>

you can now see the branch on your personal directory.

.. image:: images/new_branch_git_push.png
    :align: center
    :width: 40%

----

Hands on: create pull request (2)
.................................


2. create a merge request to an other branch (original gitlab / github repository)

.. image:: images/create_merge_request.png
    :align: center

.. image:: images/merge_request_1.png
    :align: center

.. image:: images/merge_request_1.png
    :align: center

.. image:: images/merge_request_2.png
    :align: center

3. ask one of your neighbour to review and merge the PR

----

* push those modifications to the upstream repository and create a pull-request
* ask one of your neighbour to review this PR and merge it on the upstream repository
* retrieve the modifications to your own master branch

----

Git - Interact with another repository
......................................

To interact with a remote repository : 

* *remote* : manage tracked repositories
* *remote add name url* : Adds a remote named <name> for the repository at <url>

.. note:: all this information is stored in .git/config file

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
