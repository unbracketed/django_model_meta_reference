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

docs_path = os.path.abspath(os.path.join(__file__, '..', '..', 'docs'))

with open('index.rst', 'w') as f:
	for attr in [attr for attr in dir(Dummy._meta) if not attr.startswith('_')]:
		
		with open(os.path.join(docs_path, '%s.rst' % attr), 'w') as rf:
			rf.write('TODO documentation and/or example code')
		
		if callable(getattr(Dummy._meta, attr)) and getattr(Dummy._meta, attr).__doc__:
			#strip off newline and replace extraneous spaces
			doc = re.sub(r'\s{2,}', ' ', getattr(Dummy._meta, attr).__doc__.lstrip())
			f.write('\n%s\n' % attr)
			f.write('    %s\n' % doc)
		else:
			f.write('\n%s\n    TODO: need description\n' % attr)
