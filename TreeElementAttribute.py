#  -*- coding=utf-8 -*-
"""
 Copyright (C) 2012 Jürgen Baumeister

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

TreeElementAttribute.py
#=====================================================================================================
A class to model the attributes for a tree element
"""

#=====================================================================================================
# Import section
#=====================================================================================================
# No imports needed so far

#=====================================================================================================
# Class TreeElementAttribute
#=====================================================================================================
class TreeElementAttribute:
	"""
	A class to represent the attributes for a tree element
	Each attribute can have an id, a tag (used to represent it in an xml document)
	and a value
	"""
	
	def __init__(self, key=None, value=None, tag=None):
		"""
		Create an object, that represents a key value pair as an attribute
		The tag field contains the tag, that is used to represent the attribute
		within a XML document
		"""
		if key == None or key == '':
			raise KeyError
			
		self.key = key
		self.value = value
		if tag != None:
			self.tag = tag
		else:
			self.tag = key
	
	def getKey(self):
		return self.key
		
	def getValue(self):
		return self.value
	
	def getTag(self):
		return self.tag
		
	def setValue(self, value):
		self.value = value
		
	def setTag(self, tag):
		self.tag = tag
		
	def clear(self):
		self.value = None
