#~/anaconda3/envs/ai_env/bin/python /Desktop/ai-t3/main.py
import tictactoe as ttt
import q_agent as qa
import numpy as np

agent1 = qa.qAgent(0.01, 0.99, 0.25)
agent2 = qa.qAgent(0.01, 0.99, 0.25)
env = ttt.game(1)

for x in range(1,10):

'''pA1, pA2 = None, None
for x in range(int(input())):
	env.reset()
	while env.end:
		pA1 = np.copy(env.board)
		pA2 = -np.copy(env.board)	

while input() != 'e':
	env.reset()
	while not env.end:
		env.printBoard()

		i, j = input().split(' ')
		env.move((int(i), int(j)))

		i, j = input().split(' ')
		env.move((int(i), int(j)))

		#env.move(agent1.action(env.board))'''