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
import re

sources = """
Sources:
"""

version = 'sbit_file-v1'

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
The purpose of this script is to generate the sha1 file and a subsequent
sbit file for whatever source file your choice may prevail.

To run this command, use start as the first parameter.
./osprey_app-{0} /path/to/file
"""
	print(motd_help.format(version))
	exit(0)

if len(sys.argv) <= 1:
        print('[ERROR] Missing file.')
        exit(1)
else:
        filepath = sys.argv[1]

if not os.path.isfile(filepath):
	print("[ERROR] Path is not a file: " + filepath)
	exit(1)

sbit_cmd = "/divideme.app.osprey.app/osprey_app-sbit-v4.py"

cmd = "sha1=$( openssl dgst -sha1 " + filepath + " | awk '{ print $NF }' > " + filepath + ".sha1 )"

try:
	sha1_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	sha1 = sha1_proc.stdout.read().decode('utf-8').strip()
	sha1_proc.terminate()
except Exception as e:
	print('[ERROR] Unable to produce sha1. Error:' + str(e))
	exit(1)

if os.path.isfile(filepath + '.sha1'):
	print("** Successfully created file: " + filepath + '.sha1')

cmd = "sha1=$( cat " + filepath + ".sha1 ) && " + sbit_cmd + " $sha1 > " + filepath + ".sbit"

try:
	sbit_file_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	sbit_file = sbit_file_proc.stdout.read().decode('utf-8').strip()
	sbit_file_proc.terminate()
except Exception as e:
	print('[ERROR] Unable to produce sbit. Error:' + str(e))
	exit(1)

if os.path.isfile(filepath + '.sbit'):
	print("** Successfully created file: " + filepath + '.sbit')

cmd = "sha1=$( cat " + filepath + ".sha1 ) && " + sbit_cmd + " -json $sha1 > " + filepath + ".sbit.json"

try:
	sbit_file_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	sbit_file = sbit_file_proc.stdout.read().decode('utf-8').strip()
	sbit_file_proc.terminate()
except Exception as e:
	print('[ERROR] Unable to produce sbit.json. Error:' + str(e))
	exit(1)

if os.path.isfile(filepath + '.sbit.json'):
	print("** Successfully created file: " + filepath + '.sbit.json')

exit(0)