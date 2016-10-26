#!/usr/bin/env python3
# this code don't work, but it will be use in future versions
def start(path='words.txt'):
	input = []
	output = []
	line = ''
	with open('words.txt', mode='r') as f:
		for line in f:
			if line.find(':') == -1:
				continue
			else:
				input = line.split(':')
				output.append(input[1][:-1]+':'+input[0]+'\n')
	with open('words.txt', mode='w') as f:
		for w in output:
			f.write(w)
#import sys
#args = sys.argv
#if len(args) == 1:
#	start()
#elif len(args) == 2:
#	if args[1] == '-h' or args[1] == '--help':
#		pass
#	else:
#		start(path=args[1])
