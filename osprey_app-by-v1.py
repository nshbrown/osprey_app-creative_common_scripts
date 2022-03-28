#!/usr/bin/python3.8

# MIT License
#
# Copyright (c) 2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]
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

sources = """
Sources:
https://stackoverflow.com/questions/3877623/can-you-have-variables-within-triple-quotes-if-so-how
"""

version = 'by-v1'

if len(sys.argv) > 1:
	motd_help = """
Welcome to OSPREY.app's {0}
-----------------------------------------------------
Created by: Nathaniel Steven Henry Brown
Email: nate@purefame.com

MIT License

Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[REQS] 	This is script is compiled to run on Ubuntu 16LTS and above with 
		python3.

The purpose of this script is to produce a bit based on the data on the machine
relative to an ipv6 and a moment calculated by uuid4 by way of a Qubit ~1 not ~0.

To run this command, run the command:
eg: ./osprey_app-{0}
"""
	print(motd_help.format(version))
	exit(0)

# by="Brown, Nathaniel Steven Henry" && sbit=$(/osprey_app-scripts/osprey_app-sbit-v6.py -sha2-256-hex "$by") && dm=$(/osprey_app-scripts/osprey_app-divide_me-v10.py $sbit "$by" | openssl dgst -sha3-256 | awk '{print $NF}') && echo $dm

cmd = "/osprey_app-scripts/osprey_app-sbit-v6.py -log-raw ipv6"
# print(cmd)
ipv6_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
ipv6 = ipv6_proc.stdout.read().decode('utf-8').strip()
ipv6_proc.terminate()

ipv6_uuid = str(uuid.uuid4())
cmd = "echo '" + ipv6 + " " + ipv6_uuid + "' | openssl dgst -sha256 | awk '{print $NF}'"
# print(cmd)
ipv6_sha2_256_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
ipv6_sha2_256 = ipv6_sha2_256_proc.stdout.read().decode('utf-8').strip()
ipv6_sha2_256_proc.terminate()

cmd = "/osprey_app-scripts/osprey_app-divide_me-v10.py '" + ipv6_sha2_256 + "' '" + ipv6 + "' | openssl dgst -sha3-256 | awk '{print $NF}'"
# print(cmd)
divide_me_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
divide_me = divide_me_proc.stdout.read().decode('utf-8').strip()
divide_me_proc.terminate()

divide_me_int = int.from_bytes(divide_me.encode('utf-8'), 'big')
print(divide_me_int, end="")
exit(0)
