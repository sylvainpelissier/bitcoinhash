#!/usr/bin/python
import argparse
import json
import sys

from binascii import unhexlify
from hashlib import sha256
from urllib.request import urlopen

def littleEndian(string):
	string = unhexlify(string)[::-1]
	return string

def test_block_hash():
	url = "https://blockchain.info/rawblock/000000000000000000046308409bb6a9fe11d98529efd3c50ba0445e06bc8746"
	response = json.loads(urlopen(url).read())
	hash = computeHash(response)
	assert hash == "4687bc065e44a00bc5d3ef2985d911fea9b69b40086304000000000000000000"

def computeHash(block, verbose=False):
	version = littleEndian('{:8x}'.format(block['ver']))
	previousHash = littleEndian(block['prev_block'])
	merkleRoot = littleEndian(block['mrkl_root'])
	time = littleEndian(hex(block['time'])[2:])
	difficultyBits = littleEndian(hex(block['bits'])[2:])
	nonce = littleEndian(hex(block['nonce'])[2:])

	header = version + previousHash + merkleRoot + time + difficultyBits + nonce

	# First hash
	firstHash = sha256(header).hexdigest()
	if(verbose):
		print(firstHash)

	# Second Hash
	calculatedHash = sha256(unhexlify(firstHash)).hexdigest()
	return calculatedHash

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", help="display intermediate hash", action="store_true")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f', "--file", type=str, help='read the block from a json file')
	group.add_argument('-u', "--url", type=str, help='read the block from a URL')
	args = parser.parse_args()

	if (args.file is not None):
		response = json.load(open(args.file))
	elif (args.url is not None):
		response = json.loads(urlopen(args.url).read())
	else:
		url = "https://blockchain.info/latestblock"
		response = json.loads(urlopen(url).read())
		hash = response["hash"]
		url = "https://blockchain.info/rawblock/"+hash
		response = json.loads(urlopen(url).read())
		print("Latest block hash:")
				
	print(computeHash(response, args.verbose))

