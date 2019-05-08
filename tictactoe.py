"""
Copyright 2019 Nathan DÉCHER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from game import Game

class TicTacToe(Game):
	"""
	Tic Tac Toe game state
	"""
	
	def __init__(self, clone=None):
		if clone:
			self.board=[i for i in clone.board]
			self.player=clone.player
			self.status=clone.status
		else:
			self.board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
			self.player=1
			self.status=0
	
	def __repr__(self):
		return str(self.board)+' -> '+str(self.player)+' -> '+str(self.status)+' ('+str(self.getScore())+')'
	
	def getPlayer(self):
		return self.player
	
	def getStatus(self):
		return self.status
	
	def getMoves(self):
		"""
		Move generator
		"""
		if self.status!=0:
			return []
		moves=[]
		for i in range(9):
			if self.board[i]==0:
				moves.append((i%3, i//3))
		return moves
	
	def play(self, x, y):
		"""
		Game play
		"""
		
		# make the actual move 
		self.board[x+y*3]=self.player
		self.player=-self.player
		
		# check for the diagonals first
		if (x==1)==(y==1):
			if self.board[0]==self.board[4] and self.board[4]==self.board[8]:
				self.status=self.board[0]
				return
			if self.board[2]==self.board[4] and self.board[4]==self.board[6]:
				self.status=self.board[0]
				return
		
		# check for the row and column
		if self.board[x]==self.board[x+3] and self.board[x]==self.board[x+6]:
			self.status=self.board[x]
			return
		if self.board[y*3]==self.board[1+y*3] and self.board[y*3]==self.board[2+y*3]:
			self.status=self.board[y*3]
			return
	
	def clone(self):
		"""
		Game state clone
		"""
		return type(self)(self)
	
	def playClone(self, x, y):
		"""
		Game play
		"""
		clone=self.clone()
		clone.play(x, y)
		return clone
	
	def getScore(self, a):
		"""
		Score estimation method
		"""
		
		# a won or lost game gives 100 points
		if self.status!=0:
			return 100*self.status
		
		# function to count the instances of -1's and 1's in its arguments
		def count(a, b, c):
			x, y=0, 0
			if a==-1:
				x+=1
			elif a==1:
				y+=1
			if b==-1:
				x+=1
			elif b==1:
				y+=1
			if c==-1:
				x+=1
			elif c==1:
				y+=1
			return (x, y)
		
		# function to compute the score for three values
		def value(a, b, c):
			n, p=count(self.board[a], self.board[b], self.board[c])
			if p==0:
				if n==1:
					return -1
				if n==2:
					return -10
			if n==0:
				if p==1:
					return 1
				if p==2:
					return 10
			return 0
		
		# calculate the overall score
		score=0
		score+=value(0, 1, 2)+value(3, 4, 5)+value(6, 7, 8) # rows
		score+=value(0, 3, 6)+value(1, 4, 7)+value(2, 5, 8) # cols
		score+=value(0, 4, 8)+value(2, 4, 6) #diagonals
		return score
