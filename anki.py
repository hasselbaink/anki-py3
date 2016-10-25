#!/usr/bin/env python3
def start(path='words.txt'):
	import card 		# Preparing
	cards = []
	line = ''
	with open(path, mode='r') as f:
		for line in f:
			words = line.split(':')
			cards.append(card.Card(words[0], words[1]))
	from random import random
	points = 0
	chances = 3
	length = len(cards)
	while True:		# Starting
		word = cards[int(random() * length)]
		while True:
			print(word.get_word1())
			inp = input('Is: ')
			if (inp+'\n') == word.get_word2():
				points+=1
				chances=3
				if (points % 10) == 0:
					print('!!!Fine, you\'ve earned '+str(points)+'!!!')
				break
			elif inp is 'X':
				sys.exit()
			else:
				if chances > 0:
					points-=1
					chances-=1
					print('You are lose 1 point.')
				else:
					points-=1
					chances=3
					print('True variant: '+word.get_word2())
					break

import sys
args = sys.argv
if len(args) == 1:
	start()
elif len(args) == 2:
	if args[1] == '-h' or args[1] == '--help':
		print('Usage: ./anki.py [path to file]/[flag]')
		print('Flags:\n\t-h\t-\tHelp\n\t--help')
	else:
		start(path=args[1])
