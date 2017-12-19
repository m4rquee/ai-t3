import numpy as np 

class game():
	def __init__(self, turn):
		self.board = np.zeros((3, 3))
		self.turn = turn
		self.end = False

	def reset(self):
		self.end = False
		self.board = np.zeros((3, 3))

	def toChar(self, n):
		if n == -1:
			return 'X'
		elif n == 1:
			return 'O' 

		return ' '

	def charAt(self, i, j):
		return self.toChar(self.board[i][j])

	def printBoard(self):
		print(' {} | {} | {} '.format(self.charAt(0, 0),\
			self.charAt(0, 1), self.charAt(0, 2)))
		print('___|___|___')
		print(' {} | {} | {} '.format(self.charAt(1, 0),\
			self.charAt(1, 1), self.charAt(1, 2)))
		print('___|___|___')
		print(' {} | {} | {} '.format(self.charAt(2, 0),\
				self.charAt(2, 1), self.charAt(2, 2)))
		print('   |   |   ')

	def won(self):
		for line in self.board:
			sum = line[0] + line[1] + line[2]
			if sum == 3:
				return 1
			elif sum == -3:
				return -1

		for i in range(3):
			sum = self.board[0][i] + self.board[1][i] +\
				self.board[2][i]
			if sum == 3:
				return 1
			elif sum == -3:
				return -1

		sum = self.board[0][0] + self.board[1][1] +\
			self.board[2][2]
		if sum == 3:
			return 1
		elif sum == -3:
			return -1

		sum = self.board[0][2] + self.board[1][1] +\
			self.board[2][0]
		if sum == 3:
			return 1
		elif sum == -3:
			return -1

		return 0

	def move(self, pos):
		if not self.board[pos[0]][pos[1]] == 0:
			return -0.1
		if self.end:
			return 0

		self.board[pos[0]][pos[1]] = self.turn
		self.turn *= -1

		self.end = self.won() != 0

		return 0