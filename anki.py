#!/usr/bin/env python3
def start(path='words.txt'):
	import card
	cards = []
	line = ''
	with open(path, mode='r') as f:
		for line in f:
			words = line.split(':')
			cards.append(card.Card(words[0], words[1]))
	from random import random
	points = 0
	length = len(cards)
	while True:
		word = cards[int(random() * length)]
		while True:
			print(word.get_word1())
			inp = input('Is: ')
			if (inp+'\n') == word.get_word2():
				points+=1
				if (points % 10) == 0:
					print('!!!Fine, you\'ve earned '+str(points)+'!!!')
				break

import sys
args = sys.argv
if len(args) == 1:
	start()
elif len(args) == 2:
	start(path=args[1])
