#!/usr/bin/env python3
words = []
with open('words.txt', mode='r') as f:
	for line in f:
		words.append(line)
from random import random
length = len(words)
points = 0
while True:
	word = words[int(random() * length)].split(':')
	while True:
		print(word[0])
		inp = input('To russian is: ')
		if (inp+'\n') == word[1]:
			points+=1
			if (points % 10) == 0:
				print('!!!Fine, you\'ve earned {} points!!!'.format(points))
			break
		else:
			pass
