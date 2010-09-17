"""
Introspect Model options to generate a skeleton for the documentation.
This script depends on being run from within a Django shell.
"""
import os
import re

from django.db import models


class Meta: pass
Dummy = type('Dummy', (models.Model, ), {'__module__': 'django.db',
					 'Meta': Meta})

index_header = \
"""Django Models Internals Documentation
=====================================

The goal of this project is to create and collect a good set of reference information for
the Django Model internals as of version 1.2.1. Rather than repeat information
that the Django documentation already covers adequately, the permalink back to
the Django docs will be favored.

Additionally, collecting high quality tutorials and/or well documented
snippets into a single location will help users get a better sense of the
patterns involved in tweaking model internals.


Model Options:

.. toctree::
   :maxdepth: 2
   
"""

index_footer = \
"""
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

docs_path = os.path.abspath(os.path.join(__file__, '..', '..', 'docs'))
print docs_path
with open('index.rst', 'w') as f:
	
	f.write(index_header)
	
	for attr in [attr for attr in dir(Dummy._meta) if not attr.startswith('_')]:
		
		with open(os.path.join(docs_path, '%s.rst' % attr), 'w') as rf:
			rf.write('%s\n'%attr)
			rf.write('=' * len(attr))
			rf.write('\n\n')
		
			if callable(getattr(Dummy._meta, attr)) and getattr(Dummy._meta, attr).__doc__:
				#strip off newline and replace extraneous spaces
				doc = re.sub(r'\s{2,}', ' ', getattr(Dummy._meta, attr).__doc__.lstrip())
				rf.write('   %s\n' % doc)
			else:
				rf.write('\n%s\n    TODO: need description\n' % attr)
		
		f.write("   %s\n" % attr)
	
	f.write(index_footer)
	
