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

# Version 1.2.1

# Sources:
# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
# https://www.programiz.com/python-programming/methods/string/index
# https://www.tutorialkart.com/python/python-read-file-as-string/

import subprocess
import hashlib
import re
import sys

class CodecCipher():
	# import random; l = list(default_values); random.shuffle(l);
	default_values = '+v9A!1tLQ8\\eKdlfJwBcmbsRau5hSnHq/IUONZiXrMTGCjP2xzVD6Wyok7403=EFYpg' + "-@#$%^&*()_<>?,.;':\"[]{}~`"

	def __get_divide_me_return(self, ret):
		ret = ret[2:][:-1]
		ret = ret if len(ret) != 0 else False
		return ret

	def chunks(self,str, length):
		return [str[i:i+length] for i in range(0, len(str), length)]


	def convert_base64_into_codec_ciphered_base64(self,data, chunk_size):
		codec_ciphered_base64 = ''
		for chunk in self.chunks(data, chunk_size):
			for byte_position in range(0, chunk_size):	
				if byte_position < len(chunk):
					# Find the position of the byte in question within the cipher
					try:
						cipher_chunk_byte = self.default_values.index(chunk[byte_position])
					except:
						exit("Error 1: Unknown character found based on cipher to encrypt: " + chunk[byte_position])
					# Take the previous position found and add 
					ciphered_byte = self.default_values[cipher_chunk_byte+int(codec[byte_position])]
					codec_ciphered_base64 = codec_ciphered_base64 + str(ciphered_byte)

		return codec_ciphered_base64

	def convert_codec_ciphered_base64_into_base64(self, data, chunk_size):
		codec_ciphered_base64_reversed = ''
		for rev_chunk in self.chunks(data, chunk_size):
			for rev_byte_position in range(0, chunk_size):	
				if rev_byte_position < len(rev_chunk):
					rev_cipher_chunk_byte = self.default_values.index(rev_chunk[rev_byte_position])
					rev_ciphered_byte = self.default_values[rev_cipher_chunk_byte-int(codec[rev_byte_position])]
					codec_ciphered_base64_reversed = codec_ciphered_base64_reversed + str(rev_ciphered_byte)

		return codec_ciphered_base64_reversed

	def get_codec(self, host):
		cmd = 'osprey_app_divide_me-inlovelike-v1 1 ' + host

		divide_me = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, executable="/bin/bash")
		divide_me_return = self.__get_divide_me_return(str(divide_me.stdout))

		divide_me_cipher = re.match(r'([0-9]\.[0-9]+)', divide_me_return)
		codec = divide_me_cipher[1].replace('.', '')

		return str(codec)

if len(sys.argv) >= 2:
	source = sys.argv[1]
else:
	source = 'https://inlovelike.com/'

if len(sys.argv) >= 3:
	file = sys.argv[2]
	file_handle = open(file, "r")

	#read whole file to a string
	base64_data = file_handle.read().strip()
	base64_data = re.sub(r'(\r\n|\r|\n)', '', base64_data)

	#close file
	file_handle.close()
else:
	base64_data = 'Lg==' # a dot

if len(sys.argv) >= 4:
	reverse = True
else:
	reverse = False


codec_cipher = CodecCipher()

codec = codec_cipher.get_codec(source)
chunk_size = len(codec)

if not reverse:
	codec_ciphered_base64 = codec_cipher.convert_base64_into_codec_ciphered_base64(base64_data, chunk_size)

# print("\nCode ciphered base64:")
	print(codec_ciphered_base64, end="")
else:
	codec_ciphered_base64_reversed = codec_cipher.convert_codec_ciphered_base64_into_base64(base64_data, chunk_size)

	print(codec_ciphered_base64_reversed, end="")
