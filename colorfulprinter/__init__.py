# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-05-24 16:20:39
# @Last Modified by:   drinks
# @Last Modified time: 2016-05-25 10:58:51
# try:
from .npprint import PrettyPrinter, pformat, isreadable, isrecursive, saferepr, pprint
from .termcolor import color_write, cprint
__all__ = ("pprint", "pformat", "isreadable", "isrecursive", "saferepr",
           "PrettyPrinter", 'color_write', 'cprint')

