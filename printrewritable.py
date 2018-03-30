#!/usr/bin/python

#import sys
from sys import stdout

CR = '\r'

class PrintRewritable():
	def __init__(self):
		self._lineLength = 0
		self._lineRewriteable = False
		self._firstTime = True

	def _SpaceFillLastText(self):
		return ' ' * self._lineLength

	def _Prefix(self):
		if self._lineRewriteable:
			return CR + self._SpaceFillLastText() + CR
		else:
			if self._firstTime:
				return ''
			else:
				return '\n'

	def _WriteToScreen(self, text):
		text = str(text)

		#sys.stdout.write(text)
		stdout.write(text)
		#sys.stdout.flush()
		stdout.flush()

	def Print(self, text, lineRewriteable=False):
		'''Stores the line length of the last passed message and if it should be rewritten.
		If it should be rewriten, the next time a line is printed the cursor is reset with a "\\r"
		character and the last line overwritten with space characters and the cursor reset again,
		before writing in the new text and flushing it to screen.
		'''
		text = str(text)

		self._WriteToScreen(self._Prefix() + text)

		#multiline text cannot be fully overwritten so do not try
		self._lineRewriteable = lineRewriteable and not '\n' in text

		self._lineLength = len(text)
		self._firstTime = False
