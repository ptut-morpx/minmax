class Game:
	def __init__(self):
		"""
		instantiates a state
		"""
		self.grid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.player=1
	
	def play(self, x, y):
		"""
		plays at the given coordinates
		"""
		self.grid[x][y]=self.player
		self.player*=-1
	
	def clone(self):
		"""
		creates an identical but distinct copy of this state
		"""
		clone=Game()
		clone.grid=[]
		for i in [0, 1, 2]:
			clone.grid.append([self.grid[i][0], self.grid[i][1], self.grid[i][2]])
		clone.player=self.player
		return clone
	
	def playClone(self, x, y):
		"""
		creates a new state and play in it
		"""
		clone=self.clone()
		clone.play(x, y)
		return clone
	
	def checkStatus(self):
		"""
		checks for a win
		"""
		for i in [0, 1, 2]:
			if self.grid[i][0]==self.grid[i][1] and self.grid[i][1]==self.grid[i][2] and self.grid[i][1]!=0:
				return self.grid[i][1]
			if self.grid[0][i]==self.grid[1][i] and self.grid[1][i]==self.grid[2][i] and self.grid[1][i]!=0:
				return self.grid[1][i]
		if self.grid[1][1]!=0:
			if self.grid[0][0]==self.grid[1][1] and self.grid[1][1]==self.grid[2][2]:
				return self.grid[1][1]
			if self.grid[2][0]==self.grid[1][1] and self.grid[1][1]==self.grid[0][2]:
				return self.grid[1][1]
		return 0
	
	def getScore(self):
		"""
		calculates a score for a grid
		a win gives you 100 points
		an unblockable two gives you 10 points
		a blockable two gives you 1 point
		"""
		status=self.checkStatus()
		if status!=0:
			return status*100
		
		def double(v, a):
			"""
			checks if v has an advantage in a
			"""
			c=0
			for k in a:
				if k==v:
					c+=1
				elif k==-v:
					return False
			return c==2
		
		score=0
		for i in [-1, 1]:
			val=(i==self.player and 10 or 1)*i
			
			# diagonals
			if double(i, [self.grid[0][0], self.grid[1][1], self.grid[2][2]]):
				score+=val
			if double(i, [self.grid[2][0], self.grid[1][1], self.grid[0][2]]):
				score+=val
			
			# rows and cols
			for j in [0, 1, 2]:
				if double(i, [self.grid[j][0], self.grid[j][1], self.grid[j][2]]):
					score+=val
				if double(i, [self.grid[0][j], self.grid[1][j], self.grid[2][j]]):
					score+=val
		return score
	
	def getMoves(self):
		"""
		returns a list containing all valid moves as tuples ((x, y), state, score)
		"""
		if self.checkStatus()!=0:
			return []
		
		moves=[]
		for x in [0, 1, 2]:
			for y in [0, 1, 2]:
				if self.grid[x][y]==0:
					coords=(x, y)
					state=self.playClone(x, y)
					score=state.getScore()
					moves.append((coords, state, score))
		return moves
