#!/usr/bin/python3.8

# LICENSE CREATIVE_COMMONS-ATTRIBUTION_SHARE_ALIKE
# https://creativecommons.org/licenses/by-sa/3.0/legalcode
# Copyright (c) 2020-2022 Nathaniel Steven Henry Brown [0+nate@purefame.com]

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
