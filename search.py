from util import *
from node import *
from waterjug import *

def getChildNode(problem, parent, action):
	cState = problem.getResult(parent.state, action)
	cParent = parent
	cAction = action
	cPathCost = parent.pathCost + problem.getStepCost(parent.state, action)
	return Node(cState, cParent, cAction, cPathCost)

def BFS(problem):
	root = Node(problem.initialState)
	if problem.testGoal(root.state): return getSolution(root)

	frontier = Queue()
	frontier.push(root)
	explored = set()

	while True:
		if frontier.isEmpty():
			print "Cannot find solution"
			return
		node = frontier.pop()
		explored.add(node.state)
		for action in problem.getActions(node.state):
			child = getChildNode(problem, node, action)
			if child.state not in explored:
				if problem.testGoal(child.state): return getSolution(child)
				frontier.push(child)

def DFS(problem):
	root = Node(problem.initialState)
	if problem.testGoal(root.state): return getSolution(root)

	frontier = Stack()
	frontier.push(root)
	explored = set()

	while True:
		if frontier.isEmpty():
			print "Cannot find solution"
			return
		node = frontier.pop()
		explored.add(node.state)
		for action in problem.getActions(node.state):
			child = getChildNode(problem, node, action)
			if child.state not in explored:
				if problem.testGoal(child.state): return getSolution(child)
				frontier.push(child)

def getSolution(node):
	stack = Stack()
	while node.parent != None:
		stack.push((node.state, node.action))
		node = node.parent
	stack.push((node.state, node.action))

	while not stack.isEmpty():
		state, action = stack.pop()

		if   action == FILL_X: print "Fill X"
		elif action == FILL_Y: print "Fill Y"

		elif action == OUT_X: print "Pour X out"
		elif action == OUT_Y: print "Pour Y out"

		elif action == X_TO_Y_FLOAT: print "Pour X to Y"
		elif action == Y_TO_X_FLOAT: print "Pour Y to X"

		elif action == X_TO_Y_NOTFLOAT: print "Pour X to Y"
		elif action == Y_TO_X_NOTFLOAT: print "Pour Y to X"

		print state, "\n"


if __name__ == "__main__":
	problem = WaterJug()
	BFS(problem)



