.. _library-index:

###############################
  CODE project documentation
###############################

Description
-----------
Code project is designed to simplify the life of those who teach or attend 
the course with programming exercises.
We provide a service for automatic code verification in cloud. Currently, 
we support Python and Java programming languages, but later service can be 
easily extended with any language you want. We use sandboxes to make code 
execution safe.

Architecture
------------
Our system consists of separate modules which are written in different 
languages:

.. figure::  _static/images/architecture.png
   :align:   center

.. toctree::
   :maxdepth: 4

   web_portal.rst
   web_service.rst
   workers.rst
   support.rst