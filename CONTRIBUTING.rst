
Guide lines adapted from `aiohttp <http://aiohttp.readthedocs.io/en/stable/>`_

Contributing
============

How to contribute

Imposter syndrome disclaimer: I want your help. No really, I do.

There might be a little voice inside that tells you you're not ready; that you need to do one more tutorial,
or learn another framework, or write a few more blog posts before you can help me with this project.

I assure you, that's not the case.

This project has some clear Contribution Guidelines and expectations that you can read here (link).

The contribution guidelines outline the process that you'll need to follow to get a patch merged.
By making expectations and process explicit, I hope it will make it easier for you to contribute.

And you don't just have to write code. You can help out by writing documentation, tests,
or even by giving feedback about this work.
(And yes, that includes giving feedback about the contribution guidelines.)

Thank you for contributing!

Code Evaluation
_______________

async_v20 aims to lower the barrier of entry to algorithmically trade on the FOREX market.

Features such as:
    - Correct signature for all API methods
    - Converting objects to *pandas*. **Series**

Are examples of features provided with this goal in mind.

Pull Requests that lessen the technical burden on users will be highly regarded


Instructions for contributors
-----------------------------


In order to make a clone of the GitHub_ repo: open the link and press the
"Fork" button on the upper-right menu of the web page.

Workflow:

  1. Clone the GitHub_ repo

  2. Make a change

  3. Make sure all tests passed

  4. Add a file into ``CHANGES`` folder (`Changelog update`_).

  5. Commit changes to own aiohttp clone

  6. Make pull request from github page for your clone against master branch

  .. note::
     If your PR has long history or many commits
     please rebase it from main repo before creating PR.


Tests coverage
--------------

Please add a test corresponding to any new features

async_v20 uses **pytest**

Install the test runner first:

.. code-block:: shell

   $ pip install pytest
   $ pip install pytest-asyncio

Test your changes with

.. code-block:: shell

   $ pytest


Documentation
-------------

documentation improvements are wanted!

Before making a Pull Request with documentation changes.

from async_v20 root directory run:

.. code-block:: shell

   $ make clean
   $ make html

Run the python's in built http server from async_v20's root directory

.. code-block:: shell

   $ python -m http.server

Navigate to:

http://localhost:8000/

And check the changes

Changelog update
----------------

Please add changes to ``CHANGELOG.txt``


The End
-------

After finishing all steps make a GitHub_ Pull Request, thanks.


.. _GitHub: https://github.com/jamespeterschinner/async_v20

