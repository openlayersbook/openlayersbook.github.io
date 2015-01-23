#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import csv
import re
import os
from itertools import islice

markdown_template = """
!INCLUDE "{header}"

<iframe src="../openlayers_book_samples/{ch_filename_path}" width="770" height="600" frameBorder="0" seamless="seamless">
</iframe>

<a href="../openlayers_book_samples/{ch_filename_path}" target="_blank">Open sample in a new windows</a>

```html
{{{{ ../openlayers_book_samples/{ch_filename_path} }}}}
```
""".format

with open('content_organisation.txt', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    for row in islice(reader, 1, None):
        if row[0].startswith('ch'):
            path_base = row[0] + '/example-' + row[1][10:12]
            print('    * [' + row[2] + '](' + path_base + '.md)')
            with open(path_base + '-header.md', 'w') as outfile:
                outfile.write('# ' + row[2])
            with open(path_base + '.md', 'w') as outfile:
                outfile.write(
                	markdown_template(
                		header='example-' + row[1][10:12] + '-header.md',
                		ch_filename_path='chapter' + row[1][7:9] + '/' + row[1]
                	)
                )
