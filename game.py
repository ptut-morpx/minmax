"""
Copyright 2019 Nathan DÉCHER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class Game:
	"""
	The base class for minmax-compatible games
	All objects given to the minmax algorithm should have all of these methods and properties.
	"""
	
	def __init__(self):
		"""
		Base constructor
		Should at least define these properties.
		"""
		self.player=1 # the next player to play, either 1 or -1
		self.status=0 # the state of the game, 1 or -1 in case of a win or loss, and 0 otherwise.
	
	def getScore(self):
		"""
		Score estimation method
		Should return a value between -100 and 100 where -100 means that -1 has won and 100 means that 1 has won.
		"""
		return 0
	
	def getMoves(self):
		"""
		Move generator
		Should generate an iterable yielding all valid moves as tuples which will then be expanded and given to the playClone method.
		"""
		return [(0, 0), (0, 1), (1, 0), (1, 1)]
	
	def playClone(self, *args):
		"""
		Game play
		Should return a distinct state identical to this one after having played the given move.
		This method can handle its arguments in any way. 
		This is usually implemented using a clone method and a play method, but this is by no means required.
		"""
		clone=Game()
		clone.player=-self.player
		return clone
