# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-05-24 16:59:42
# @Last Modified by:   drinks
# @Last Modified time: 2016-05-24 23:09:56
__all__ = ('PY3', 'unicode')

import sys
PY3 = sys.version_info[0] > 2
if PY3:
    unicode = str
unicode = unicode
