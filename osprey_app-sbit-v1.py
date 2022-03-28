#!/usr/local/bin/python3.8

import re
import subprocess

# LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
# https://creativecommons.org/licenses/by-sa/3.0/legalcode
# Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

eg = "1.639629710710792858755732690E-47 Hz (p.v8.0.0) [1 ÷ We did it! Woohoo ;)]"
print(eg)
# 082fd134ceb4f6e8ff8d65a227e57e6d2ecaffe38a97aa88c4bc3ba3985d3a97
hz_matches = re.match(r"((\d+\.\d+)([E]?[-+]?)(\d+))\sHz", eg)
head = hex(int(hz_matches[2].replace('.', '')))
tail = hex(int(hz_matches[4]))

coin = str(head.replace('0x', '')) + hz_matches[3] + str(tail.replace('0x', ''))

print(coin)
# 54c4518b8a1f126d47d14d2E-2f

coin_value = int.from_bytes(coin.encode('utf-8'), 'big')

print(coin_value)
# 21887118876010347795183703788327694437338207134076983283882472038

cmd = "echo '" + coin + "' | openssl dgst -sha3-256 | awk '{print $NF}'"
sha3_256_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
sha3_256 = sha3_256_proc.stdout.read().decode('utf-8').strip()
sha3_256_proc.terminate()

print(sha3_256)
# 2405b9434de85ad20bb85dedc9350aeb941387e0e7718cb5c14a87484494a468