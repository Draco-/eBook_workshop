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

TreeElement.py
#=====================================================================================================
A class to model a tree information structure
"""

#=====================================================================================================
# Import section
#=====================================================================================================
from TreeElementAttribute import TreeElementAttribute

#=====================================================================================================
# Class TreeElement
#=====================================================================================================
class TreeElement:

	#=================================================================================================
	# initialisation of object
	#=================================================================================================
	def __init__(self, id, parent=None, tag=None):
		"""
		Create a new TreeElement with a given id and a parent, if given.
		"""
		# id field may not be a empty string
		if id != '':
			self.id = id
		else:
			raise KeyError
		self.parent = parent				# The TreeElement, this object is a child of
		self.tag = tag						# A tag string for the element (e.g. correspondes with a tag name in xml)
		self.attributes = []				# Key value pairs, providing attributes for the tree element
		self.content = None					# a content object for the tree element (its intended for the tag to be a indicator
											# for the object class, that goes here
		self.children = []					# A list of TreeElements, that are children of this object
											# this way it is possible to build up complex trees

	#=================================================================================================
	# get and set methods for the TreeElement
	#=================================================================================================
	def get_id(self):
		return self.id

	def get_parent(self):
		return self.parent

	def get_tag(self):
		return self.tag

	def get_attributes(self):
		return self.attributes

	def get_attribute(self, attr):
		for attribute in self.attributes:
			if attribute.get_key() == attr:
				return attribute
		raise KeyError

	def get_content(self):
		return self.content

	def get_children(self):
		return self.children

	def get_child(self, child_id):
		for child in self.children:
			if child.id == child_id:
				return child
		raise KeyError

	def __getitem__(self, path):
		"""
		Method to retrieve an element, defined by a path string.
		This is a method, that enables the object[path] syntax of python
		The method uses the __findtree__ method to recursively search for the
		queried element
		"""
		if not isinstance(path, str):	  # path must be a string in the format 'element/element/element'
			raise TypeError

		# split the path into a list of ids
		path_list = path.strip().split('/')

		# check if the actual object meets the start of the path list
		if self.id == path_list[0].strip():
			# then start recursive search
			return self.__findTreeElement(path_list[1:], self)
		raise KeyError

	def __findTreeElement(self, path_list, tree):
		"""
		Recursively searches a tree for an element given by the path list
		This method should be called from __getitem__ to ensure, that path_list
		and tree are consistent
		"""
		if path_list == []:
			# if path list is empty, the given element is the searched element
			return tree
		else:
			for element in tree.children:
				if element.id == path_list[0]:
					return self.__findTreeElement(path_list[1:], element)
			raise KeyError

	def set_id(self, id):
		if self.parent != None:
			if self.parent.hasChild(id):
				raise KeyError
		self.id = id

	def set_parent(self, parent):
		self.parent = parent

	def set_tag(self, tag):
		self.tag = tag

	def set_content(self, cont):
		self.content = cont

	#=================================================================================================
	# info methods for TreeElement
	#=================================================================================================
	def hasChildren(self):
		"""
		Returns True, if the TreeElement has children, False otherwise
		"""
		if len(self.children) != 0:
			return True
		else:
			return False

	def hasChild(self, id):
		"""
		Returns True, if the TreeElement has a child with the given id, False otherwise
		"""
		for element in self.children:
			if element.id == id:
				return True
		return False

	def hasAttributes(self):
		"""
		Returns True, if the TreeElement has attributes, False otherwise
		"""
		if len(self.attributes) != 0:
			return True
		else:
			return False

	def hasAttribute(self, attr):
		"""
		Returns True, if the TreeElement has an attribute with the given name, False otherwise
		"""
		for attribute in self.attributes:
			if attribute.get_key() == attr:
				return True
		return False

	#=================================================================================================
	# methods to manipulate tree
	#=================================================================================================
	def addChild(self, id, pos=None, tag=None):
	
		if not self.hasChild(id):
			if (pos != None and isinstance(pos, int)):
				if pos < len(self.children):
					self.children.insert(pos, self.__class__(id, self, tag))
			else:
				self.children.append(self.__class__(id, self, tag))
		else:
			raise KeyError

	def addAttribute(self, attr, value, pos=None):

		if not self.hasAttribute(attr):
			if (pos != None and isinstance(pos, int)):
				if pos < len(self.attributes):
					self.attributes.insert(pos, TreeElementAttribute(attr, value))
			else:
				self.attributes.append(TreeElementAttribute(attr, value))
		else:
			raise KeyError

	#=================================================================================================
	# methods to get a tree representation
	#=================================================================================================
	def toTreeString(self, level=0):
		"""
		Returns a string, that gives an overview over the included structure elements
		by printing their tags
		"""
		result = ' ' * (2 * level)
		result += self.id + '\n'

		for child in self.children:
			result += child.toTreeString(level + 1)

		return result