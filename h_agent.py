import tictactoe as ttt

class hAgent():    
    def updateQ(self, state, action, r, newState):
        pass
    
    def doAction(self, state):
        ret = (None, None)
        rng = range(3)

        while not (ret[0] in rng and ret[1] in rng):
            try:
                pos = input('\nDigite uma posição válida: ')
                ret = (int(pos[0]), int(pos[1]))
            except Exception:
                pass

        return ret
        
