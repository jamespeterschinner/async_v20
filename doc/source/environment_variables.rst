.. _adding-environment-variables:

Adding Environment Variables
============================

Due to the abundance of information in regards to configuring environment
variables, it can be challenging to find information that will result in success.

Here we will try and and point you in the correct direction.

PyCharm
-------

    https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm

Mac
---
    https://stackoverflow.com/questions/135688/setting-environment-variables-in-os-x/3756686#3756686

Windows
-------

    https://stackoverflow.com/questions/1672281/environment-variables-for-java-installation

Ubuntu
------

    https://askubuntu.com/questions/58814/how-do-i-add-environment-variables


What is an environment variable?
--------------------------------

For our requirements, we will think of an environment variable,
as a variable stored outside the scope of the application.

Python programs can access these variables via the *os* module

Why store the token in an environment variable?
_______________________________________________

There are a couple of reason. Primarily:

 - Convenience, create a client with `OandaClient()` not
   `OandaClient(xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)`
 - Secure, prevents you from uploading the token to an online repository
 - May simplify deployment of your trading program

