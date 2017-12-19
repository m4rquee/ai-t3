import numpy as np
import random as rnd

class qAgent():
	def __init__(self, α, γ, ε):
		self.α = α
		self.γ = γ
		self.ε = ε

		self.qtable = {}

	def toNum(self, board):
		ret = 0
		for i in range(3):
			for j in range(3):
				ret +=  int(board[i][j]) << 6 * i + 2 * j

		return ret

	def getQ(self, state, action):
		actions = self.qtable.get(self.toNum(state), np.zeros((3, 3)))

		return actions[action[0]][action[1]]

	def updateQ(self, state, action, r, newState):
		if action is None:
			return

		cod = self.toNum(state)

		actions = self.qtable.get(cod, np.zeros((3, 3)))
		
		if not newState is None:
			newCod = self.toNum(newState)
			newActions = self.qtable.get(newCod, np.zeros((3, 3)))
			maxNewQ = newState.max()
		else:
			maxNewQ = 0

		qValue = actions[action[0]][action[1]]
		newQ = qValue + self.α * (self.γ * maxNewQ + r - qValue)

		actions[action[0]][action[1]] = newQ

	def doAction(self, state):
		actions = self.qtable.get(self.toNum(state), np.zeros((3, 3)))
		
		if rnd.random() > self.ε:
			return np.unravel_index(actions.argmax(), (3, 3))
		else:
			return (rnd.randint(0, 2), rnd.randint(0, 2))