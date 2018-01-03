#~/anaconda3/envs/ai_env/bin/python /Desktop/ai-t3/main.py
import copy as cp
import tictactoe as ttt
import q_agent as qa
import h_agent as ha
import mov_aux as ma
import numpy as np
import math

p = False
def printBoard(env):
    if p: env.printBoard('\n')

def save(eps, ag, k):
    print(eps + 1)
    ag.qtable['k'] = k
    np.save('agentAI', ag.qtable)
    
env = ttt.game(-1)

aiData = np.load('agentAI.npy').item()
k = 1

ag1 = qa.qAgent(1, 0.999)
ag1.qtable = aiData

ag2 = qa.qAgent(1, 0.999)
ag2.qtable = cp.deepcopy(aiData)

##ag2 = ha.hAgent()

aiMov = ma.ai_mov(ag1, ag2)

print('k = ' + str(k))
##while input('\nDeseja parar? ') != 's':
for i in range(int(input('Número de eps: '))):
    ag1.α = 4.6 / math.log(99 + k)
    ag2.α = ag1.α

    env.reset()
    k += 1
    
    if (i + 1) % 10000 == 0:
        save(i, ag1, k)
        
    while True:
        if aiMov.doMove(env):
##            printBoard(env)
            break
##        printBoard(env)
        
        if aiMov.doMove(env):
##            printBoard(env)
            break
##        printBoard(env)
        
print('\nk = ' + str(k))
ag1.qtable['k'] = k
np.save('agentAI', ag1.qtable)
