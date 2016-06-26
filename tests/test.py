# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-05-24 16:24:54
# @Last Modified by:   drinks
# @Last Modified time: 2016-06-03 22:38:50
from __future__ import print_function

from collections import OrderedDict
from colorfulprinter import PrettyPrinter
from colorfulprinter import color_write, npprint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
si = StringIO()
si.write = color_write(si.write)
pp = PrettyPrinter(indent=4, stream=si)
d = OrderedDict()
f = OrderedDict()
for i in range(15):
    f[i] = range(i)
    d[str(i)] = {i: {tuple(range(i)): range(i)}}
d['3'] = [u'中国', u'中国']
a = {1: {2: {3: {4: {5: 6}}}}}
npprint(d)
