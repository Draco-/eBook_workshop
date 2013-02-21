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
	"""
	
	def __init__(self, key=None, value=None):
		"""
		Create an object, that represents a key value pair as a attribute
		"""
		if key == None or key == '':
			raise KeyError
			
		self.key = key
		self.value = value
	
	def get_key(self):
		return self.key
		
	def get_value(self):
		return self.value
		
	def set_value(self, value):
		self.value = value
		
	def clear(self):
		self.value = None
