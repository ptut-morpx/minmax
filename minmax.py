"""
minmax module
calculates most favorable route from any given state
states must have a `getMoves()` method returning a tuple in the following format: `(coords, state, score)` where
	- `coords` is any sensible object
	- `state` is a distinct state accessible with the original state and the `coords` object
	- `score` is a score between -100 and 100
states must have a `player` property which should alternate between 1 and -1 on each move
"""

class Tree:
	def __init__(self, move):
		self.coords=move[0]
		self.state=move[1]
		self.score=move[2]
		self.player=self.state.player
		self.children=[]
		self.preferred=None
	
	def recalculate(self):
		"""
		traverses the tree to find the most favorable branch
		"""
		# leaves are worthless if not a win or loss
		if len(self.children)==0:
			if not self.score in [-100, 100]:
				self.score=0
		
		# recalculate score based on children
		# first we go for a win, and then for the next most favorable outcone
		elif not self.score in [-100, 100]:
			
			# player 1 maximises score
			if self.player==1:
				high=-100
				branch=None
				for child in self.children:
					child.recalculate()
					if child.score==100:
						self.score=100
						self.preferred=child
						return
					elif child.score>=high:
						high=child.score
						branch=child
				self.score=high
				self.preferred=branch
			
			# player -1 minimises score
			else:
				low=100
				branch=None
				for child in self.children:
					child.recalculate()
					if child.score==-100:
						self.score=-100
						self.preferred=child
						return
					elif child.score<=low:
						low=child.score
						branch=child
				self.score=low
				self.preferred=branch
	
	def build(self, depth):
		"""
		recursively build the tree
		"""
		if depth==0:
			return
		for move in self.state.getMoves():
			child=Tree(move)
			self.children.append(child)
			child.build(depth-1)
	
	def getBest(self):
		"""
		find the best route
		"""
		list=[]
		elem=self
		while elem.preferred:
			list.append(elem.preferred.coords)
			elem=elem.preferred
		return list

def minmax(state, depth=9):
	"""
	calculate most favorable route and score
	"""
	tree=Tree((None, state, 0))
	tree.build(depth)
	tree.recalculate()
	return (tree.getBest(), tree.score)

from tictactoereverse import Game

# play a bit so that it's not impossible to win
a=Game()

print(minmax(a, 9))
