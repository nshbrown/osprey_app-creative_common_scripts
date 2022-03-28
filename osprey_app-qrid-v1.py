#!/usr/bin/python3.8

# MIT License
#
# Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from sys import exit
import os.path
import json
import pyqrcode as qrcode
import io
import subprocess

sources = """
Sources:
https://www.askpython.com/python/built-in-methods/python-read-file
"""

version = 'qrid-v1'

if len(sys.argv) == 1:
	motd_help = """
Welcome to OSPREY.app's {0}
-----------------------------------------------------
Created by: Nathaniel Steven Henry Brown
Email: nate@purefame.com

[LICENSE] 
Acceptable use only as permitted. Contact to co-ordinate an agreement.

[REQS] 	
This is script is compiled to run on Ubuntu 16LTS and above with 
python3 support having net-tools and OpenSSL 1.1.1l installed.

[USAGE]
The purpose of this script is to generate a qrcode based on either a
file as the parameter or a directory to gather JSON data from

To run this command, use start as the first parameter.
./osprey_app-{0} path/to/file.json
"""
	print(motd_help.format(version))
	exit(0)

json_path = ''
json_paths = []

if len(sys.argv) <= 1:
        print('[WARNING] Missing JSON path as param. Using default.')
        json_path = '/sbit.osprey.app/json/'
else:
        json_path = sys.argv[1]

if os.path.isfile(json_path):
	json_paths = [json_path]
elif os.path.isdir(json_path):
	cmd = 'find ' + json_path + ' | xargs'
	find_xargs_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	find_xargs = find_xargs_proc.stdout.read().decode('utf-8').strip()
	find_xargs_proc.terminate()

	json_paths = find_xargs.split(" ")
else:
	print("[ERROR] Parameter of a file or directory of json data was not present.")
	exit(1)


for json_path in json_paths:
        qr_png = '/sbit.osprey.app/qr.png/' + os.path.basename(json_path) + '.png'
        if not os.path.isfile(qr_png) and os.path.isfile(json_path):
                with open(json_path) as f:
                        json_data_raw = f.read()
                        qr = qrcode.create(json_data_raw)
                        qr.png(qr_png, scale=10)
                        print("[INFO] ** Finished: " + os.path.basename(json_path))

exit(0)