MAX_X = 7
MAX_Y = 5

FILL_X 			= 1
FILL_Y 			= 2
OUT_X  			= 3
OUT_Y 			= 4
X_TO_Y_FLOAT    = 5
Y_TO_X_FLOAT 	= 6
X_TO_Y_NOTFLOAT = 7
Y_TO_X_NOTFLOAT = 8


class WaterJug:
	def __init__(self):
		self.initialState = (0, 0)
		self.goalState 	  = (3, 1)

	def getActions(self, state):
		actionList = []
		if state[0] < MAX_X: actionList.append(FILL_X)
		if state[1] < MAX_Y: actionList.append(FILL_Y)

		if state[0] > 0: actionList.append(OUT_X)
		if state[1] > 0: actionList.append(OUT_Y)

		if state[0] + state[1] >= MAX_Y and state[0] > 0: actionList.append(X_TO_Y_FLOAT)
		if state[0] + state[1] >= MAX_X and state[1] > 0: actionList.append(Y_TO_X_FLOAT)

		if state[0] + state[1] < MAX_Y and state[0] > 0: actionList.append(X_TO_Y_NOTFLOAT)
		if state[0] + state[1] < MAX_X and state[1] > 0: actionList.append(Y_TO_X_NOTFLOAT)

		return actionList

	def getResult(self, state, action):
		if   action == FILL_X: return (MAX_X, state[1])
		elif action == FILL_Y: return (state[0], MAX_Y)

		elif action == OUT_X: return (0, state[1])
		elif action == OUT_Y: return (state[0], 0)

		elif action == X_TO_Y_FLOAT: return (state[0] - (MAX_Y - state[1]), MAX_Y)
		elif action == Y_TO_X_FLOAT: return (MAX_X, state[1] - (MAX_X - state[0]))
		
		elif action == X_TO_Y_NOTFLOAT: return (0, state[0] + state[1])
		elif action == Y_TO_X_NOTFLOAT: return (state[0] + state[1], 0)	

	def getStepCost(self, state, action):
		return 1

	def testGoal(self, state):
		return state == self.goalState


if __name__ == "__main__":
	problem = WaterJug()
	print problem.getActions(problem.initialState)
	print problem.getResult(problem.initialState, FILL_X)
