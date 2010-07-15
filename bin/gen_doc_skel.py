import re

from django.db import models

class Meta: pass
Dummy = type('Dummy', (models.Model, ), {'__module__': 'django.db', 'Meta': Meta})


with open('index.rst', 'w') as f:
	for attr in [attr for attr in dir(Dummy._meta) if not attr.startswith('_')]:
		if callable(getattr(Dummy._meta, attr)) and getattr(Dummy._meta, attr).__doc__:
			#strip off newline and replace extraneous spaces
			doc = re.sub(r'\s{2,}', ' ', getattr(Dummy._meta, attr).__doc__.lstrip())
			f.write('\n%s\n' % attr)
			f.write('    %s\n' % doc)
		else:
			f.write('\n%s\n    TODO: need description\n' % attr)
