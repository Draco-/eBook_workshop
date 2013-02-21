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
This structure is also useable to represent the content of xml files. Therefore,
each tree element owns not only a list of children (necessary to build up a tree),
but also a list of attributes, a content field and a tail field (in correspondence
with various xml parsers available for python)
"""

#=====================================================================================================
# Import section
#=====================================================================================================
from TreeElementAttribute import TreeElementAttribute

#=====================================================================================================
# Class TreeElement
#=====================================================================================================
class TreeElement:
	"""
	A class to model a tree information structure
	This structure is also useable to represent the content of xml files. Therefore,
	each tree element owns not only a list of children (necessary to build up a tree),
	but also a list of attributes, a content field and a tail field (in correspondence
	with various xml parsers available for python)
	"""

	#=================================================================================================
	# Initialisation of object
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
											# tag and id may be the same, but this is not necessary
		self.attributes = []				# Key a list of TeeElementAttribute objects (value pairs),
											# providing attributes for the tree element
		self.children = []					# A list of TreeElements, that are children of this object
											# this way it is possible to build up complex trees
		self.content = None					# a content object for the tree element (its intended for the tag to be a indicator
											# for the object class, that goes here
		self.tail = None					# like the content object, but in a xml surrounding follows the closing xml tag
											# until the next xml tag is reached


	#=================================================================================================
	# Get and set methods for the TreeElement
	#=================================================================================================
	def getId(self):
		return self.id

	def getParent(self):
		return self.parent

	def getTag(self):
		return self.tag

	def getAttributes(self):
		return self.attributes

	def getAttribute(self, attr):
		"""
		Get an attribute by using its key as search parameter.
		If searched attribute is not available, rais KeyError
		"""
		for attribute in self.attributes:
			if attribute.getKey() == attr:
				return attribute
		raise KeyError

	def getChildren(self):
		return self.children

	def getChild(self, child_id):
		"""
		Get a child by using its id as search parameter.
		If searched child is not availabel, raise KeyError
		"""
		for child in self.children:
			if child.id == child_id:
				return child
		raise KeyError
	
	def getChildByTag(self, child_tag):
		"""
		Get a child by using its tag as search parameter.
		As multiple children with the same tag are allowed, the result is a
		list of matching children.
		If no child matches the given search parameter, an empty list is returned
		"""
		result = []
		for child in self.children:
			if child.tag == child_tag:
				result.append(child)
		return result

	def getContent(self):
		return self.content

	def getTail(self):
		return self.tail

	# the following two methods are used to find a special tree element by its tree path. Using the special method name __getitem__
	# enables the class to provide the object[element] usage pattern
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

	def setId(self, id):
		"""
		As a search path within the tree must be unique, we need to check, if another
		child with the given id already exists
		"""
		if self.parent != None:
			if self.parent.hasChild(id):
				raise KeyError
		self.id = id

	def setParent(self, parent):
		self.parent = parent

	def setTag(self, tag):
		self.tag = tag

	def setContent(self, cont):
		self.content = cont
		
	def setTail(self, tail):
		self.tail = tail

	#=================================================================================================
	# Info methods for TreeElement
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
		If the TreeElement has a child with the given id the position of the child is
		returned. Otherwise False is returned
		"""
		pos = 0
		for element in self.children:
			if element.id == id:
				return pos
			pos += 1
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
		If the TreeElement has an attribute with the given id the position of the
		attribute is returned. Otherwise False is returned
		"""
		pos = 0
		for attribute in self.attributes:
			if attribute.getKey() == attr:
				return pos
			pos += 1
		return False

	#=================================================================================================
	# Methods to manipulate a tree
	#=================================================================================================
	def addChild(self, id, pos=None, tag=None):
		"""
		Adds a child (another TreeElement) to the list of children, using the
		given id as id for the new tree element.
		If pos is given and not None, the child is inserted at this position.
		Otherwise the new child is appended at the end of the list.
		If tag is given, it is used to set the tag field of the new tree element.
		"""
		if self.hasChild(id) == False:
			if (pos != None and isinstance(pos, int)):
				self.children.insert(pos, self.__class__(id, self, tag))
			else:
				self.children.append(self.__class__(id, self, tag))
		else:
			raise KeyError
			
	def replaceChild(self, id, id_new, tag=None):
		"""
		Replaces the child with the given id by another TreeElement with id set to id_new and
		the given tag.
		All other elements (attribuet, children, content ...) of the replaced child get lost.
		"""
		# Get the position of the child to replace
		replace_pos = self.hasChild(id)
		if isinstance(replace_pos, bool):
			raise KeyError
			
		# Create a new tree element and replace the existing one
		if (not isinstance(self.hasChild(id_new), bool)) or (id_new == ''):
			raise KeyError
		else:
			new_element = self.__class__(id_new, self, tag)
			self.children[replace_pos] = new_element
		
	def moveChild(self, old_pos, new_pos):
		"""
		Moves a child from the given old position to the new position
		"""
		child = self.children[old_pos]
		del self.children[old_pos]
		self.children.insert(new_pos, child)
		
	def removeChild(self, id):
		"""
		Removes the child with the given id.
		All information, including subtrees are lost.
		"""
		# Get the position of the child to be removed
		remove_pos = self.hasChild(id)
		del self.children[remove_pos]

	def addAttribute(self, attr, value=None, tag=None, pos=None):
		"""
		Adds a new attribute to the list of attributes within the tree element,
		using the attr name (key) and the value given.
		If pos is given as an integer, the attribute inserted at this position.
		Otherwise the attribute is appended to the list of attributes
		"""
		if self.hasAttribute(attr) != True:
			if (pos != None and isinstance(pos, int)):
				if pos < len(self.attributes):
					self.attributes.insert(pos, TreeElementAttribute(attr, value, tag))
			else:
				self.attributes.append(TreeElementAttribute(attr, value, tag))
		else:
			raise KeyError

	#=================================================================================================
	# Methods to inspect the tree element (for debugging only)
	#=================================================================================================
	def inspect(self, printable=False):
	
		result = 'TreeElement inspector\n'
		result += '=====================\n'
		result += 'Element ID: ' + self.id + '\n'
		result += 'Parent:     '
		if self.parent == None:
			result += 'None\n'
		else:
			result += self.parent.getId() + '\n'
		result += 'Tag:        '
		if self.tag == None:
			result += 'None\n'
		else:
			result += self.tag + '\n'
		result += 'Attributes: ['
		for attr in self.attributes:
			result += '(%s:%s - %s)' % (attr.getKey(), attr.getTag(), attr.getValue(),)
		result += ']\n'
		result += 'Children:   ['
		for child in self.children:
			result += '(%s:%s)' % (child.getId(), child.getTag(),)
		result += ']\n'
		result += 'Content:    '
		if self.content == None:
			result += 'None\n'
		else:
			result += self.content + '\n'
		result += 'Tail:       '
		if self.tail == None:
			result += 'None\n'
		else:
			result += self.tail + '\n'
		
		if printable:
			return result
		else:
			print result
		
	
	#=================================================================================================
	# Methods to get a tree representation
	#=================================================================================================
	def toTreeString(self, level=0):
		"""
		Returns a string, that gives an overview over the included structure elements
		by printing their tags
		"""
		result = ' ' * (2 * level)
		result += self.id + ' : ' + self.tag + '\n'

		for child in self.children:
			result += child.toTreeString(level + 1)

		return result