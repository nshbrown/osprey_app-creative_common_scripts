#!/usr/bin/python3.8

# LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
# https://creativecommons.org/licenses/by-sa/3.0/legalcode
# Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

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
https://www.askpython.com/python/built-in-methods/python-read-file
"""

SCRIPT_SBIT = '/osprey_apps-scripts/osprey_app-sbit-v8.py'
SCRIPT_QRID = '/osprey_app-scripts/osprey_app-qrid-v1.py'

version = 'sbit_qrid-v1'

if len(sys.argv) == 1:
	motd_help = """
Welcome to OSPREY.app's {0}
-----------------------------------------------------
LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
https://creativecommons.org/licenses/by-sa/3.0/legalcode
Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

[REQS] 	
This is script is compiled to run on Ubuntu 16LTS and above with 
python3 support having net-tools and OpenSSL 1.1.1l installed.

[USAGE]
The purpose of this script is to generate a qrcode based on a string
used through to the latest sbit script (v4) as of writing this code.

To run this command, use start as the first parameter.
./osprey_app-{0} "Your Message Here"
"""
	print(motd_help.format(version))
	exit(0)

if len(sys.argv) <= 1:
        print('[ERROR] Missing message.')
        exit(1)
else:
        message = sys.argv[1]

msg_as_file_name = re.sub(r'[^a-zA-Z0-9]+', '_', message)
sbit_json_file_path = '/sbit.osprey.app/json/' + msg_as_file_name[:255] + '.json'

cmd = SCRIPT_SBIT + ' -json "' + message + '" > ' + sbit_json_file_path
sbit_json_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
sbit_json = sbit_json_proc.stdout.read().decode('utf-8').strip()
sbit_json_proc.terminate()

if os.path.isfile(sbit_json_file_path):
	print("** file created: " + sbit_json_file_path)

def sha2_256_sumfile(sbit_json_file_path):
	cmd = 'openssl dgst -sha256 ' + sbit_json_file_path
	json_sha2_256_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	json_sha2_256_return = json_sha2_256_proc.stdout.read().decode('utf-8').strip()
	json_sha2_256_proc.terminate()
	# print(json_sha2_256)
	json_sha2_256 = json_sha2_256_return.split(' ')[1]

	cmd = 'echo "' + json_sha2_256 + '" > ' + sbit_json_file_path + '.sha2_256'
	json_sha2_256_copy_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	json_sha2_256_copy_proc.terminate()

	print("** file created: " + sbit_json_file_path + '.sha2_256')

	cmd = SCRIPT_SBIT + ' "' + json_sha2_256 + '" > ' + sbit_json_file_path + '.sbit'
	sbit_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
	sbit_return = sbit_proc.stdout.read().decode('utf-8').strip()
	sbit_proc.terminate()

	print("** file created: " + sbit_json_file_path + '.sbit')


sha2_256_sumfile(sbit_json_file_path)

cmd = SCRIPT_QRID + ' "' + sbit_json_file_path + '"'
sbit_json_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
sbit_json = sbit_json_proc.stdout.read().decode('utf-8').strip()
sbit_json_proc.terminate()

png_filename = '/sbit.osprey.app/qr.png/' + os.path.basename(sbit_json_file_path) + '.png'

if os.path.isfile(png_filename):
	print("** file created: " + png_filename)
	sha2_256_sumfile(png_filename)
	

exit(0)