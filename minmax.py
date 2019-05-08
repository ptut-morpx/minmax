"""
pyright 2019 Nathan DÉCHER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


class Minmax:
	"""
	Minmax tree
	"""
	
	def __init__(self, state, move=None):
		"""
		Constructor
		Instantiate a tree for a given Game state.
		"""
		self.state=state
		self.move=move
		self.score=100*state.getStatus()
		self.children=[]
		self.preferred=None
	
	def __repr__(self, indent=''):
		a=indent+str(self.move)+": "+str(self.score)+": "+self.state.__repr__()
		for c in self.children:
			a+='\n'+c.__repr__(indent+'\t')
		return a
	
	def build(self, depth, weights=None):
		"""
		Tree builder
		"""
		
		# handle leaves
		if depth==0:
			if self.state.getStatus()!=0:
				self.score=self.state.getScore(weights)
			return
		
		# create children
		for move in self.state.getMoves():
			child=Minmax(self.state.playClone(*move), move)
			child.build(depth-1, weights) #TODO find somewhere appropriate to recurse
			self.children.append(child)
			
			# stop immediately on win condition
			if child.score*self.state.getPlayer()==100:
				self.score=child.score
				self.preferred=child
				return
		
		# handle leaves
		if len(self.children)==0:
			return
		
		# find best child
		score=-100
		for child in self.children:
			if child.score*self.state.getPlayer()>=score:
				score=child.score*self.state.getPlayer()
				self.preferred=child
		self.score=score*self.state.getPlayer()
	
	@classmethod
	def getBestMove(Minmax, state, depth, weights=None):
		"""
		Best move finder
		"""
		
		# build the tree and compute minmax on it
		tree=Minmax(state)
		tree.build(depth, weights)
		
		# get best path
		moves=[]
		elem=tree
		while elem.preferred:
			moves.append(elem.preferred.move)
			elem=elem.preferred
		return (moves, tree.score)


from tictactoe import TicTacToe
a=TicTacToe()
print(Minmax.getBestMove(a, 9))
