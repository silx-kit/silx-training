.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>


Software engineering tips & tools
=================================

The initial idea has been stolen from
`software carpentry <http://swcarpentry.github.io/slideshows/best-practices/index.html>`_
defined in this `publication <http://dx.doi.org/10.1371/journal.pbio.1001745>`_
from 2014.

The most important message for scientists writing code can be summarized in 8
points they consider being the *best practices*.

----

1. Write programs for people...
-------------------------------

Write programs for people, not computers.

*  A program should not require its readers to hold more
   than a handful of facts in memory at once.
*  Make names consistent, distinctive, and meaningful.
*  Make code style and formatting consistent.

----

2. Let the computer do the work.
--------------------------------

*   Make the computer repeat tasks.
*   Save recent commands in a file for re-use.
*   Use a build tool to automate workflows.

----

3. Make incremental changes.
----------------------------
*  Work in small steps with frequent feedback and course
   correction.
*  Use a version control system.
*  Put everything that has been created manually in version
   control.

----

4. Don’t repeat yourself (or others).
-------------------------------------
*   Every piece of data must have a single authoritative
    representation in the system.
*   Modularize code rather than copying and pasting.
*   Re-use code instead of rewriting it.

----


5. Plan for mistakes.
---------------------
*   Add assertions to programs to check their operation.
*   Use an off-the-shelf unit testing library.
*   Turn bugs into test cases.
*   Use a symbolic debugger.

----

6. Optimize software only after it works
----------------------------------------

*   Use a profiler to identify bottlenecks.
*   Write code in the highest-level language possible.

-----

7. Document design and purpose
------------------------------

It is more important than to document mechanics.

*   Document interfaces and reasons, not implementations.
*   Refactor code in preference to explaining how it works.
*   Embed the documentation for a piece of software in that
    software.

----

8. Collaborate.
---------------

*  Use pre-merge code reviews.
*  Use pair programming when bringing someone new up to
   speed and when tackling particularly tricky problems.
*  Use an issue tracking tool

----

Summary.
--------

While we agree on the "*why ?*" basic software engineering practice is important,
it does not address the "*how do I do ?*" question.

We have tried to summarize all the needed information into a 1 day tutorial
which we hope, will save you a lot of time in your future:

#. Structure your project
#. Distribution and packaging
#. Testing and validation
#. Documentation

This training is focusing on Python only ... and presents a deliberately
simplified view:

There should be one, *and preferably only one*, obvious way to do it.
.....................................................................

