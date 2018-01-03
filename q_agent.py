import math as m
import numpy as np
import random as rnd

class qAgent():
	def __init__(self, α, γ):
		self.α = α
		self.γ = γ

		self.qtable = {}

	def toNum(self, board):
		ret = 0
		for i in range(3):
                        for j in range(3):
                                ret +=  int(board[i][j]) << 6 * i + 2 * j

		return ret

	def getQ(self, state, action):
		actions = np.copy(self.qtable.get(self.toNum(state),\
                                                  np.zeros((3, 3))))

		return actions[action[0]][action[1]]

	def getQEntry(self, state):
                return self.qtable.get(self.toNum(state), np.zeros((3, 3)))

	def updateQ(self, state, action, r, newState):
		if action is None:
			return

		cod = self.toNum(state)
		actions = self.qtable.get(cod, None)

		if actions is None:
			self.qtable[cod] = np.zeros((3, 3))
			actions = np.zeros((3, 3))
		
		if not (newState is None):
			newCod = self.toNum(newState)
			newActions = self.qtable.get(newCod, np.zeros((3, 3)))
			maxNewQ = newActions.max()
		else:
			maxNewQ = 0

		qValue = actions[action[0]][action[1]]
		newQ = qValue + self.α * (self.γ * maxNewQ + r - qValue)

		self.qtable[cod][action[0]][action[1]] = newQ

	def softMax(self, z):
		z_exp = [m.exp(i) for i in z]
		sumz_exp = sum(z_exp)

		return [i / sumz_exp for i in z_exp]
                

	def doAction(self, state):
		actions = self.getQEntry(state)
		index = np.random.choice(9, 1, p=self.softMax(actions.flatten()))[0]
##		index = np.argmax(actions.flatten())
		
		return np.unravel_index(index, (3, 3))

