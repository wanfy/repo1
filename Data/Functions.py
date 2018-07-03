"""
Module contains helpful general functions.
"""

import sys
import os
import re

__author__ = "Lukas 'Wanfy' Musil"
__version__ = "1:6/2018"


findX = lambda key, lines: next(i for i, line in enumerate(lines) for match in re.finditer(key, line))
findAll = lambda key, lines: [i for i, line in enumerate(lines) for match in re.finditer(key, line)]


def readArgs():
    """
    Function for reading arguments from terminal
    :return: args - (list) contains input arguments
    """

    args = sys.argv
    if len(args) > 1:
        return args[1::]
    else:
        return []


def loadFiles(selected_dir=os.path.dirname(os.path.abspath(__file__)), file_type='.txt'):
    """
    Function search files by type in current directory.
    :param selected_dir: (str) - path to file directory
    :param file_type: (str) - file type (.txt, .csv, ...)
    :return: (list) contains file/directory names
    """

    if file_type == 'dir':
        return [[dirs] for dname, dirs, files in os.walk(selected_dir)]

    else:
        for dname, dirs, files in os.walk(selected_dir):
            return [[fname] for fname in files if file_type in fname]


def clearTerminal():
    if sys.platform.startswith("linux2"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")




