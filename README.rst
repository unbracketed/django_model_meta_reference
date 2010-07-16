==========================================
Reference Guide for Django Model Internals
==========================================

If you need to do any work involving Model introspection or overriding the
default behaviors, you might have a hard time finding good documentation about
the internals of Django models.


Overview
---------

The goal of this project is to create and collect a good set of reference information for
the Django Model internals as of version 1.2.1. Rather than repeat information
that the Django documentation already covers adequately, the permalink back to
the Django docs will be favored.

Additionally, collecting high quality tutorials and/or well documented
snippets into a single location will help users get a better sense of the
patterns involved in tweaking model internals.


Structure
----------

There is an index page containing a data definition style list of the _meta
attributes. Each attribute also gets its own page; the intent of which is to
provide an appropriately thorough explanation of the attribute and/or example
code.

The gen_doc_skel script in bin was used to generate the initial skeleton for
this project. It will be deprecated in time but serves a useful purpose for
now with minimal investment in creating it. 



