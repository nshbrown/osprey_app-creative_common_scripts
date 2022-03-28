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

import re
import subprocess
import sys
from sys import exit
# import datetime.datetime
import time
import json
import uuid
import select
import os


sources = """
Sources:
https://stackoverflow.com/questions/3877623/can-you-have-variables-within-triple-quotes-if-so-how
"""

version = 'e-v1'
motd_help = """
Welcome to OSPREY.app's {0}
-----------------------------------------------------
Created by: Nathaniel Steven Henry Brown
Email: nate@purefame.com

[LICENSE] Acceptable use only as permitted. Contact to co-ordinate an agreement.

[REQS] 	This is script is compiled to run on Ubuntu 16LTS and above with 
		python3.

The purpose of this script is to encrypt the machine hardware address with a UUID
and then run it through software to encrpyt the result.

To run this command, run the command:
eg: e=$(/osprey_app-scripts/osprey_app-{0}.py) && /osprey_app-scripts/osprey_app-{0}.py "$e"
"""

if len(sys.argv) == 2 and sys.argv[1] == 'motd':
	print(motd_help.format(version))
	exit(0)

if len(sys.argv) == 1:
	cmd = '/osprey_app-scripts/osprey_app-sbit-v6.py -log-raw hw'
	hw_log_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	hw_log = hw_log_proc.stdout.read().decode('utf-8').strip()
	hw_log_proc.terminate()

	hw_moment = hw_log + ' ' + str(uuid.uuid4())
	print(hw_moment, end="")
	exit(0)
elif len(sys.argv) == 2:
	hw_moment = sys.argv[1]
else:
	print('[ERROR] Unknown number of parameters')
	exit(1)

cmd = '/osprey_app-scripts/osprey_app-bits-v1.py "' + hw_moment + '"'
bits_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
bits = bits_proc.stdout.read().decode('utf-8').strip()
bits_proc.terminate()

print(bits, end="")
exit(0)