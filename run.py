#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess

PYTHON = ['python', ]

if __name__ == '__main__':

    modules_path = os.sep.join([
        os.path.dirname(os.path.abspath(__file__)), 'Data'])

    prog = subprocess.Popen(PYTHON + ['gui.py', ], cwd=modules_path)

    prog.wait()
    