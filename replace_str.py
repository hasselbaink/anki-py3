#!/usr/bin/env python3
line = ''
words = []
output = []
with open('words.txt', mode='r') as f:
	for line in f:
		words = line.split(':')
		output.append(words[1]+':'+words[0])
with open('words.txt', mode='a') as f:
	for w in output:
		f.write(w)