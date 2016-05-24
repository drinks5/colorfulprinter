# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-05-24 16:21:07
# @Last Modified by:   drinks
# @Last Modified time: 2016-05-24 23:19:32
from __future__ import print_function
import os
from random import choice
ATTRIBUTES = dict(zip(
    [
        'bold', 'dark', '', 'underline', 'blink', '', 'reverse', 'concealed'
    ], list(range(1, 9))))
del ATTRIBUTES['']

HIGHLIGHTS = dict(zip(
    [
        'on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta',
        'on_cyan', 'on_white'
    ], list(range(40, 48))))
COLORS = dict(zip(
    [
        'grey',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
    ], list(range(30, 38))))
RESET = '\033[0m'


def colored(text, color=None, on_color=None, attrs=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[{0}m{1}'
        text = color is not None and fmt_str.format(COLORS[color],
                                                    text) or text
        text = on_color is not None and fmt_str.format(HIGHLIGHTS[on_color],
                                                       text) or text
        if attrs is not None:
            for attr in attrs:
                text = fmt_str.format(ATTRIBUTES[attr], text)
        text = ''.join([text, RESET])
    return text


def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    print(colored(text, color=None, on_color=None, attrs=None), **kwargs)


def color_write(func):
    def warp(text):
        'Underline red on grey color',
        color = choice(list(COLORS))
        text = func(colored(text, color=color))
        return text

    return warp

# from pprint import ter