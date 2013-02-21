# coding=UTF-8
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

eBookTreeElement.py
#=====================================================================================================
A class to model the eBook structures derived from TreeElement
"""

#=====================================================================================================
# Import section
#=====================================================================================================
from TreeElement import TreeElement

#=====================================================================================================
# Class eBookTreeElement
#=====================================================================================================
class eBookTreeElement(TreeElement):
	"""
	A class derived from TreeElement
	This class is used to model the information structure for a epub eBook file.
	As the TreeElement is already designet to model xml document structures, this
	class only needs to implement a method to create a xml string from the given
	tree
	"""

	def toXMLString(self, level=0):
		"""
		Return a string, that is the xml representation of the tree
		"""
		# prepare resulting string
		result = ''
		# if level = 0 we start with the xml header
		#if level == 0:
		#	result += '<?xml version=\"%s\" encoding=\"%s\"?>\n' % ('1.0', 'UTF-8')

		# start with the tag
		result += ' '*(4 * level)
		result += '<%s' % (self.tag,)

		# if the tag also has attributes, put them into the tag
		if self.attributes != []:
			for attribute in self.attributes:
				result += ' %s=\"%s\"' % (attribute.getTag(), attribute.getValue(),)

		# if there is neither content nor children, close the tag
		if ((self.content == None or self.content == '') and self.children == []):
			result += ' />\n'
			return result
		else:
			result += '>'     # no \n here, because content could follow

		# if there is a content, put it into the result
		if (self.content != None and self.content != ''):
			result += self.content

		# if there are children, recursively put them to the result
		if self.children != []:
			result += '\n'
			for child in self.children:
				#result += '\n'
				result += child.toXMLString(level + 1)
				#result += '\n'
		else:
			result += '</%s>\n' % (self.tag,)
			return result

		result += ' ' * (4 * level)
		result += '</%s>\n' % (self.tag,)
		
		# if there is a tail, put it at the end of the tag
		if not (self.tail == None or self.tail == ''):
			result += self.tail + '\n'

		return result

