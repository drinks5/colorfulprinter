# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-05-24 16:20:39
# @Last Modified by:   drinks
# @Last Modified time: 2016-05-24 23:22:17

from npprint import pprint, PrettyPrinter, pformat, isreadable, isrecursive, saferepr
from termcorlor import color_write, cprint

__all__ = ("pprint", "pformat", "isreadable", "isrecursive", "saferepr",
           "PrettyPrinter", 'color_write', 'cprint')

if __name__ == '__main__':
    pp = PrettyPrinter(indent=4)
    pp.pprint([1, 2, 3, [3, 4, [5, 6, [6,7, [7]]]]])