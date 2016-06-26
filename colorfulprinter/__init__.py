# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-05-24 16:20:39
# @Last Modified by:   drinks
# @Last Modified time: 2016-06-03 10:15:14
from __future__ import print_function
from .npprint import PrettyPrinter, pformat, isreadable, isrecursive, saferepr
from .termcolor import color_write, cprint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

__all__ = ("pprint", "pformat", "isreadable", "isrecursive", "saferepr",
           "PrettyPrinter", 'color_write', 'cprint', 'npprint')


def npprint(object, **kwargs):
    si = StringIO()
    should_colored = kwargs.get('should_colored')
    si.write = should_colored and color_write(si.write) or si.write
    kwargs.update(dict(stream=si))
    pp = PrettyPrinter(indent=4, stream=si)
    pp.pprint(object)
    content = si.getvalue()
    print(content)
    si.close()
    return content
