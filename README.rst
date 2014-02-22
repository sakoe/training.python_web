.. contents::

Introduction
============

This package provides the source for all lecture materials for a 10-session
course in Web Development using Python.

This package provides the source for all lecture materials used for the
`Internet Programming in Python`_ section of the `Certificate in Python
Programming`_ offered by the `University of Washington Professional &
Continuing Education`_ program. This version of the documentation is used for
the Winter 2014 instance of the course, Taught by `Cris Ewing`_

.. _Internet Programming in Python: http://www.pce.uw.edu/courses/internet-programming-python/downtown-seattle-winter-2014/
.. _Certificate in Python Programming: http://www.pce.uw.edu/certificates/python-programming.html
.. _University of Washington Professional & Continuing Education: http://www.pce.uw.edu/
.. _Cris Ewing: http://www.linkedin.com/profile/view?id=19741495

Building The Documentation
--------------------------

This documentation is built using docutils and Sphinx. The package uses
`zc.buildout` to manage setup and dependencies. This package uses the version
2 `bootstrap.py` script. This version of the script will attempt to use
setuptools 0.7 or better. If you have an earlier version of setuptools
installed, please upgrade prior to bootstrapping this buildout.

After cloning this package from the repository, do the following::

  $ cd training.python_web  # the location of your local copy
  $ python bootstrap.py  # must be Python 2.6 or 2.7
  $ bin/buildout
  $ bin/sphinx   # to build the main documentation and course outline
  $ bin/build_s5   # to build the class session presentations

At the end of a successful build, you will find a ``build/html`` directory,
containing the completed documentation and presentations.

.. _zc.buildout: https://pypi.python.org/pypi/zc.buildout/
.. _bootstrap.py: http://downloads.buildout.org/2/bootstrap.py

Reading The Documentation
-------------------------

A rendered version of this documentation is maintained online.  You can view
the latest updates at http://cewing.github.com/training.python_web/

LICENSE
=======

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of
this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
California, 94041, USA.

A copy of this license in text format is included in this package under the
``docs`` directory
