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

eBook.py
#=====================================================================================================
A class to create an epub eBook, using its defined files
"""

#=====================================================================================================
# Import section
#=====================================================================================================
from zipfile import ZipFile
from zipfile import ZIP_STORED, ZIP_DEFLATED

import eBookStructure

#=====================================================================================================
# Class eBook
#=====================================================================================================
class eBook:

	#=================================================================================================
	# initialisation of object
	#=================================================================================================
	def __init__(self):
		"""
		Initializing an eBook object.
		This is just an empty eBook object, that can't be used.
		In order to be of any use, a eBook structure has to be created, by
		either reading a default structure (method new()) or by importin an
		existing eBook (method imp())
		"""
		eBook_file = None
		eBook_filename = None
		eBook_structure = None
		
	def new(self, filename):
		"""
		Initializes a new eBook from default eBook structure
		"""
		self.eBook_structure = eBookStructure.book1
		self.eBook_filename = filename
	
	def imp(self, filename):
		"""
		Import the structure of an existing eBook and build up the structure tree
		"""
		pass
		
	#=================================================================================================
	# Get and set methods
	#=================================================================================================
	def getFile(self):
		"""
		Return the zip file object, that is used to store the eBook
		"""
		return self.eBook_file
		
	def getFilename(self):
		"""
		Return the name (and path) of the eBook file, that is used to store the eBook
		"""
		return self.eBook_filename
		
	def getStructure(self):
		"""
		Return the structure tree for the eBook
		"""
		return self.eBook_structure
	
	def setFilename(self, filename):
		"""
		Set the filename (and path) for the eBook
		"""
		self.eBook_filename = filename
		
	#=================================================================================================
	# Open and close methods
	#=================================================================================================
	def open(self, mode):
		"""
		Open the eBook in the given mode
		"""
		if mode == 'w':
			self.eBook_file = ZipFile(self.eBook_filename, 'w', ZIP_DEFLATED)
		else:
			self.eBook_file = ZipFile(self.eBook_filename, 'r')
	
	def close(self):
		"""
		Close the eBook
		"""
		self.eBook_file.close()
	
	#=================================================================================================
	# Create the epub file and write the eBook
	#=================================================================================================
	def write_eBookStructure(self):
		"""
		Fill the prepared epub file (self.eBook_file) with the file structre and
		files, using the ebook tree structure, where already implemented.
		Other files are just copied from the testbook directory
		"""
		
		# Get a list of all required files
		for file in self.list_files():
			# strip each file from its path information
			file_ = file.split('/')[-1]
			#print file_
			# if the file is already implemented within the ebook structure write its content to the file
			if file_ in ['mimetype', 'com.apple.ibooks.display-options.xml','container.xml', 'content.opf', 'toc.ncx', 'CoverPage.html']:
				self.write_structureFile(file_, file)
			# else just copy from directory 'testbook'
			else:
				self.eBook_file.write('testbook/' + file, file)
		
		
	def write_structureFile(self, filename, arc_filename):
		"""
		Create an write an ebook file, from the ebook structure to the actual epub file
		"""
		file_content = u''
		print 'book/' + filename + '\n'
		file_content += self.eBook_structure['book/' + filename].content.decode('utf-8')
		for child in self.eBook_structure['book/' + filename].children:
			file_content += child.toXMLString().decode('utf-8')
		
		print (file_content + '\n').encode('latin-1')
		self.eBook_file.writestr(arc_filename, file_content.encode('utf-8'))
		
	#=================================================================================================
	# Methods to work with the eBook parameters (meta data)
	#=================================================================================================
	def checkMetadata(self):
		"""
		Check, if the available metadate meet the minimum requirements for an eBook
		"""
		result = ''
		errors = 0
		warnings = 0
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('title'), bool):
			result += 'ERROR:   eBook structure metadata do not define book title\n'
			errors += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('identifier'), bool):
			result += 'ERROR:   eBook structure metadata do not define book identifier\n'
			errors += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('language'), bool):
			result += 'ERROR:   eBook structure metadata do not define book language\n'
			errors += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('creator'), bool):
			result += 'WARNING: eBook structure metadata do not define book creator\n'
			warnings += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('contributor'), bool):
			result += 'WARNING: eBook structure metadata do not define book contributor\n'
			warnings += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('subject'), bool):
			result += 'WARNING: eBook structure metadata do not define book subject\n'
			warnings += 1
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('date'), bool):
			result += 'WARNING: eBook structure metadata do not define book date\n'
			warnings += 1
			
		return 'Errors: %d; Warnings: %d\n' % (errors, warnings,) + result
	
	def getMetadata(self, element, subelement=None):
		"""
		Return the content and the attribute value from the subelement for the given element from
		the metadata structure of the eBook
		"""
		value = '-'
		for child in self.eBook_structure['book/content.opf/package/metadata'].children:
			if child.getId() == ('dc:' + element):
				if subelement != None:
					if not isinstance(child.hasAttribute('opf:' + subelement), bool):
						value = 'opf:' + subelement + ':' + child.getAttribute('opf:' + subelement).getValue() + ' - ' + child.getContent()
				else:
					value = child.getContent()
					
		return value

		
	def set_BookTitle(self, title):
		
		if isinstance(self.eBook_structure['book/content.opf/package/metadata'].hasChild('title'), bool):
			self.eBook_structure['book/content.opf/package/metadata'].addChild('title', 0, 'dc:title')
			self.eBook_structure['book/content.opf/package/metadata/title'].setContent(title)
		else:
			self.eBook_structure['book/content.opf/package/metadata/dc:title'].setContent(title)
		
		#self.eBook_structure['book/content.opf/package/metadata/dc:identifier'].content = title
		self.eBook_structure['book/toc.ncx/ncx/head/dtb:uid'].getAttribute('content').setValue(title)
		self.eBook_structure['book/toc.ncx/ncx/docTitle/text'].content = title

		
		
		
		
	def get_BookTitle(self):
		return self.eBook_structure['book/content.opf/package/metadata/dc:title'].content
		
	def get_BookIdentifier(self):
		return self.eBook_structure['book/content.opf/package/metadata/dc:identifier'].content
		
	def set_BookIdentifier(self, identifier):
		self.eBook_structure['book/content.opf/package/metadata/dc:identifier'].content = identifier
		
	def get_BookLanguage(self):
		return self.eBook_structure['book/content.opf/package/metadata/dc:language'].content
	
	def set_BookLanguage(self, language):
		self.eBook_structure['book/content.opf/package/metadata/dc:language'].content = language
		
	def get_BookMetadataElement(self, element, subelement=None):
		value = '-'
		for child in self.eBook_structure['book/content.opf/package/metadata'].children:
			if child.get_id() == ('dc:' + element):
				if subelement != None:
					if child.hasAttribute('opf:' + subelement):
						value = child.get_attribute('opf:' + subelement).get_value() + ':' + child.get_content()
				else:
					value = child.get_content()
					
		return value

	def set_BookMetadataElement(self, element, value, subelement=None, subel_value=None):
		
		if not self.eBook_structure['book/content.opf/package/metadata'].hasChild('dc:' + element):
			self.eBook_structure['book/content.opf/package/metadata'].addChild('dc:' + element, None, 'dc:' + element)
			self.eBook_structure['book/content.opf/package/metadata/dc:' + element].content = value
			if subelement != None:
				self.eBook_structure['book/content.opf/package/metadata/dc:' + element].addAttribute(subelement, subel_value)
				
	
	
	#=================================================================================================
	# Methods to manage the files for the eBook
	#=================================================================================================
	def list_files(self):
	
		file_list = ['mimetype', 'META-INF/com.apple.ibooks.display-options.xml', 'META-INF/container.xml','OPS/content.opf']
		for child in self.eBook_structure['book/content.opf/package/manifest'].children:
			file_list.append('OPS/' + child.getAttribute('href').getValue())
		
		return file_list



ebook = eBook()

