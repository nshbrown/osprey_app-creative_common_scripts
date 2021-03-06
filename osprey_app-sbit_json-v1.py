#!/usr/bin/python3.8

# LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
# https://creativecommons.org/licenses/by-sa/3.0/legalcode
# Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

import json
import subprocess
import sys
import os.path
from sys import exit

sources = """
Sources:
https://careerkarma.com/blog/python-check-if-file-exists/
https://www.kite.com/python/answers/how-to-find-the-position-of-an-element-in-an-array-in-python#:~:text=Use%20list.,position%20of%20value%20in%20list%20.
"""

version = 'sbit_json-v1'

if len(sys.argv) == 1:
	motd_help = """
Welcome to OSPREY.app's {0}
-----------------------------------------------------
Created by: Nathaniel Steven Henry Brown
Email: nate@purefame.com

LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
https://creativecommons.org/licenses/by-sa/3.0/legalcode
Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

[REQS] 	
This is script is compiled to run on Ubuntu 16LTS and above with 
python3 support having net-tools and OpenSSL 1.1.1l installed.

[USAGE]
The purpose of this script is to find the encrpyted bit for a color 
in a hexadecimal format without the # as found in HTML and CSS.

To run this command, use start as the first parameter.
./osprey_app-{0} start
"""
	print(motd_help.format(version))
	exit(0)

positions = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')

for position_0 in positions:
	for position_1 in positions:
		for position_2 in positions:
			for position_3 in positions:
				for position_4 in positions:
					for position_5 in positions:
						color_hex = (str(position_0) + str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5))
						sbit_file_path = '/sbit.osprey.app/json/' + color_hex

						if not os.path.isfile(sbit_file_path):
							cmd = '/divideme.app.osprey.app/osprey_app-sbit-v4.py -json "' + color_hex + '" > ' + sbit_file_path
							dm = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
							dm_log = dm.stdout.read().decode('utf-8').strip()
							dm.terminate()
						# else:
							# print('[INFO] ' + version + ' alredy done: ' + sbit_file_path)

exit(0)

