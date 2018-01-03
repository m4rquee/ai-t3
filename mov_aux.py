import tictactoe as ttt
import q_agent as qa

class ai_mov():
    def __init__(self, ag1, ag2):
        self.ais = { -1: { 'ag' : ag1,\
                           's' : None,\
                           'a' : None },
                     
                     1: { 'ag' : ag2,\
                          's' : None,\
                          'a' : None } }

    def updateEQ(self, i, er):
        agent = self.ais[i]['ag']
        s = self.ais[i]['s']
        a = self.ais[i]['a']

        agent.updateQ(s, a, 1 if er == 1 else -2, None)

    def doMove(self, env):
        i = env.turn
        s = i * env.get_board()
        agent = self.ais[i]['ag']

##        if i == -1: print(agent.getQEntry(env.board))
        
        r = -1
        while r < 0:
            a = agent.doAction(s)
            r = env.move(a)
            if r <= 0:
                agent.updateQ(s, a, r, i * env.board)

        self.ais[i]['s'] = s
        self.ais[i]['a'] = a
            
        if r > 0:
            agent.updateQ(s, a, r, None)
            self.updateEQ(-i, r)
            return True

        return False
