class Card:
	def __init__(self, word1, word2):
		self.word1 = word1;
		self.word2 = word2;
	def get_word1(self):
		return self.word1;
	def get_word2(self):
		return self.word2;
	def equals(self, word):
		if self.word2 == word:
			return True
		else:
			return False
