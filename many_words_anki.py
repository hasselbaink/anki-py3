#!/usr/bin/env python3
import os
import sys
import replace_str
def start_game(path='words.txt'):
	import card 		# Preparing
	cards = []
	line = ''
	with open(path, mode='r') as f:
		for line in f:
			words = line.split('_')
			cards.append(card.Card(words[0], words[1]))
	from random import random
	length = len(cards)
	while True:		# Starting
		word = cards[int(random() * length)]
		while True:
			print(word.get_word1())
			inp = input('Is: ')
			if inp is 'X':
				sys.exit()
			else:
				print('True variant: '+word.get_word2())
				inp = input('Are you sure in your answer?(default: y):')
				if inp is '' or inp is 'y':
					break
				else:
					pass
def create_file(path='words.txt'):
	if not os.path.exists(path):
		with open(path, mode='w') as f:
			f.write('')
		inp = input('Are you want open file with \'nano\'?(y/n): ')
		if inp is 'y' or inp is 'Y':
			os.system('nano '+path)
		else:
			inp = input('Are you want open file with \'leafpad\'?(y/n): ')
			if inp is 'y' or inp is 'Y':
				os.system('leafpad '+path)

args = sys.argv
if len(args) == 1:
	filename_label = 'File name(default: words.txt): '
	inp = input('What are you doing?(play|create|replace|change): ')
	if inp == 'play':
		start_game()
	elif inp == 'create':
		inp = input(filename_label)
		if not inp == '':
			create_file(path=inp)
		else:
			create_file()
	elif inp == 'replace':
		inp = input(filename_label)
		if not inp == '':
			replace_str.start(path=inp)
		else:
			replace_str.start()
	elif inp == 'change':
		inp = input(filename_label)
		if not inp is '\n':
			os.system('nano '+inp[:-1])
		else:
			os.system('nano words.txt')
elif len(args) == 2:
	if args[1] == '-h' or args[1] == '--help':
		print('Usage: ./anki.py [path to file]/[flag]')
		print('Flags:\n\t-h\t-\tHelp\n\t--help')
	elif args[1] == 'replace':
		import replace_str; replace_str.start()
	else:
		start_game(path=args[1])
elif len(args) == 3:
	if args[1] == 'create':
		create_file(path=args[2])
	elif args[1] == 'replace':
		replace_str.start(path=args[2])
