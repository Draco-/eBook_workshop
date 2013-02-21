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

eBookStructure.py
#=====================================================================================================
A module, defining the structure of an eBook information 
"""

#=====================================================================================================
# Import section
#=====================================================================================================
from eBookTreeElement import *

#=====================================================================================================
# eBook structure definition
#=====================================================================================================
book = eBookTreeElement('book', None, 'book')

#==== mimetype ========================================================================================
book.addChild('mimetype', None, 'file')
book['book/mimetype'].content = 'application/epub+zip'

#==== com.apple.ibooks.display-options.xml =================================================================
book.addChild('com.apple.ibooks.display-options.xml', None, 'file')
book['book/com.apple.ibooks.display-options.xml'].content = '<?xml version="1.0" encoding="UTF-8"?>\n'

book['book/com.apple.ibooks.display-options.xml'].addChild('display_options', None, 'display_options')

book['book/com.apple.ibooks.display-options.xml/display_options'].addChild('platform', None, 'platform')
book['book/com.apple.ibooks.display-options.xml/display_options/platform'].addAttribute('name', '*')
book['book/com.apple.ibooks.display-options.xml/display_options/platform'].addChild('option', None, 'option')

book['book/com.apple.ibooks.display-options.xml/display_options/platform/option'].addAttribute('name', 'specified-fonts')
book['book/com.apple.ibooks.display-options.xml/display_options/platform/option'].content = 'true'

#==== container.xml =====================================================================================
book.addChild('container.xml', None, 'file')
book['book/container.xml'].content = '<?xml version="1.0" ?>\n'

book['book/container.xml'].addChild('container', None, 'container')
book['book/container.xml/container'].addAttribute('version', '1.0')
book['book/container.xml/container'].addAttribute('xmlns', 'urn:oasis:names:tc:opendocument:xmlns:container')

book['book/container.xml/container'].addChild('rootfiles', None, 'rootfiles')
book['book/container.xml/container/rootfiles'].addChild('rootfile', None, 'rootfile')
book['book/container.xml/container/rootfiles/rootfile'].addAttribute('full-path', 'OPS/content.opf')
book['book/container.xml/container/rootfiles/rootfile'].addAttribute('media-type', 'application/oebps-package+xml')

#==== content.opf =======================================================================================
book.addChild('content.opf', None, 'file')
book['book/content.opf'].content = '<?xml version="1.0" encoding="UTF-8"?>\n'

book['book/content.opf'].addChild('package', None, 'package')
book['book/content.opf/package'].addAttribute('xmlns', 'http://www.idpf.org/2007/opf')
book['book/content.opf/package'].addAttribute('unique-identifier', 'BookId')
book['book/content.opf/package'].addAttribute('version', '2.0')

book['book/content.opf/package'].addChild('metadata', None, 'metadata')
book['book/content.opf/package/metadata'].addAttribute('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
book['book/content.opf/package/metadata'].addAttribute('xmlns:dcterms', 'http://purl.org/dc/terms/')
book['book/content.opf/package/metadata'].addAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
book['book/content.opf/package/metadata'].addAttribute('xmlns:opf', 'http://www.idpf.org/2007/opf')

book['book/content.opf/package/metadata'].addChild('dc:title', None, 'dc:title')
book['book/content.opf/package/metadata/dc:title'].content = 'EPUB - Testbuch'

book['book/content.opf/package/metadata'].addChild('dc:creator', None, 'dc:creator')
book['book/content.opf/package/metadata/dc:creator'].content = 'Jürgen Baumeister'

book['book/content.opf/package/metadata'].addChild('dc:contributor', None, 'dc:contributor')
book['book/content.opf/package/metadata/dc:contributor'].addAttribute('opf:role', 'bkp')
book['book/content.opf/package/metadata/dc:contributor'].content = 'Notepad'

book['book/content.opf/package/metadata'].addChild('dc:language', None, 'dc:language')
book['book/content.opf/package/metadata/dc:language'].content = 'de'

book['book/content.opf/package/metadata'].addChild('dc:identifier', None, 'dc:identifier')
book['book/content.opf/package/metadata/dc:identifier'].addAttribute('id', 'BookId')
book['book/content.opf/package/metadata/dc:identifier'].content = 'not given'

book['book/content.opf/package/metadata'].addChild('dc:subject', None, 'dc:subject')
book['book/content.opf/package/metadata/dc:subject'].content = 'Test'

book['book/content.opf/package/metadata'].addChild('dc:date', None, 'dc:date')
book['book/content.opf/package/metadata/dc:date'].content = '2013'

book['book/content.opf/package/metadata'].addChild('meta', None, 'meta')
book['book/content.opf/package/metadata/meta'].addAttribute('name', 'cover')
book['book/content.opf/package/metadata/meta'].addAttribute('content', 'cover')

book['book/content.opf/package'].addChild('manifest', None, 'manifest')

book['book/content.opf/package/manifest'].addChild('toc_ncx', None, 'item')
book['book/content.opf/package/manifest/toc_ncx'].addAttribute('id', 'toc_ncx')
book['book/content.opf/package/manifest/toc_ncx'].addAttribute('href', 'toc.ncx')
book['book/content.opf/package/manifest/toc_ncx'].addAttribute('media-type', 'application/x-dtbncx+xml')

book['book/content.opf/package/manifest'].addChild('cover', None, 'item')
book['book/content.opf/package/manifest/cover'].addAttribute('id', 'cover')
book['book/content.opf/package/manifest/cover'].addAttribute('href', 'Cover.jpg')
book['book/content.opf/package/manifest/cover'].addAttribute('media-type', 'image/jpeg')

book['book/content.opf/package/manifest'].addChild('CoverPage_html', None, 'item')
book['book/content.opf/package/manifest/CoverPage_html'].addAttribute('id', 'CoverPage_html')
book['book/content.opf/package/manifest/CoverPage_html'].addAttribute('href', 'CoverPage.html')
book['book/content.opf/package/manifest/CoverPage_html'].addAttribute('media-type', 'application/xhtml+xml')

book['book/content.opf/package/manifest'].addChild('styles_css', None, 'item')
book['book/content.opf/package/manifest/styles_css'].addAttribute('id', 'styles_css')
book['book/content.opf/package/manifest/styles_css'].addAttribute('href', 'styles.css')
book['book/content.opf/package/manifest/styles_css'].addAttribute('media-type', 'text/css')

book['book/content.opf/package/manifest'].addChild('section-0001_html', None, 'item')
book['book/content.opf/package/manifest/section-0001_html'].addAttribute('id', 'section-0001_html')
book['book/content.opf/package/manifest/section-0001_html'].addAttribute('href', 'section-0001.html')
book['book/content.opf/package/manifest/section-0001_html'].addAttribute('media-type', 'application/xhtml+xml')
 
book['book/content.opf/package'].addChild('spine', None, 'spine')
book['book/content.opf/package/spine'].addAttribute('toc', 'toc_ncx')

book['book/content.opf/package/spine'].addChild('CoverPage_html', None, 'itemref')
book['book/content.opf/package/spine/CoverPage_html'].addAttribute('idref', 'CoverPage_html')
book['book/content.opf/package/spine/CoverPage_html'].addAttribute('linear', 'no')

book['book/content.opf/package/spine'].addChild('section-0001_html', None, 'itemref')
book['book/content.opf/package/spine/section-0001_html'].addAttribute('idref', 'section-0001_html')

#==== toc.ncx ==========================================================================================
book.addChild('toc.ncx', None, 'file')
book['book/toc.ncx'].content = '<?xml version="1.0" encoding="utf-8" ?>\n'
book['book/toc.ncx'].content += '<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">\n'

book['book/toc.ncx'].addChild('ncx', None, 'ncx')
book['book/toc.ncx/ncx'].addAttribute('xmlns', 'http://www.daisy.org/z3986/2005/ncx/')
book['book/toc.ncx/ncx'].addAttribute('xml:lang', 'en')
book['book/toc.ncx/ncx'].addAttribute('version', '2005-1')

book['book/toc.ncx/ncx'].addChild('head', None, 'head')

book['book/toc.ncx/ncx/head'].addChild('dtb:uid', None, 'meta')
book['book/toc.ncx/ncx/head/dtb:uid'].addAttribute('name', 'dtb:uid')
book['book/toc.ncx/ncx/head/dtb:uid'].addAttribute('content', 'E-Pub Testbuch')

book['book/toc.ncx/ncx/head'].addChild('dtb:depth', None, 'meta')
book['book/toc.ncx/ncx/head/dtb:depth'].addAttribute('name', 'dtb:depth')
book['book/toc.ncx/ncx/head/dtb:depth'].addAttribute('content', '1')

book['book/toc.ncx/ncx/head'].addChild('dtb:totalPageCount', None, 'meta')
book['book/toc.ncx/ncx/head/dtb:totalPageCount'].addAttribute('name', 'dtb:totalPageCount')
book['book/toc.ncx/ncx/head/dtb:totalPageCount'].addAttribute('content', '0')

book['book/toc.ncx/ncx/head'].addChild('dtb:maxPageNumber', None, 'meta')
book['book/toc.ncx/ncx/head/dtb:maxPageNumber'].addAttribute('name', 'dtb:maxPageNumber')
book['book/toc.ncx/ncx/head/dtb:maxPageNumber'].addAttribute('content', '0')

book['book/toc.ncx/ncx'].addChild('docTitle', None, 'docTitle')

book['book/toc.ncx/ncx/docTitle'].addChild('text', None, 'text')
book['book/toc.ncx/ncx/docTitle/text'].content = 'EPUB - Testbuch'

book['book/toc.ncx/ncx'].addChild('navMap', None, 'navMap')

book['book/toc.ncx/ncx/navMap'].addChild('navPoint-1', None, 'navPoint')
book['book/toc.ncx/ncx/navMap/navPoint-1'].addAttribute('id', 'navPoint-1')
book['book/toc.ncx/ncx/navMap/navPoint-1'].addAttribute('playOrder', '1')

book['book/toc.ncx/ncx/navMap/navPoint-1'].addChild('navLabel', None, 'navLabel')

book['book/toc.ncx/ncx/navMap/navPoint-1/navLabel'].addChild('text', None, 'text')
book['book/toc.ncx/ncx/navMap/navPoint-1/navLabel/text'].content = 'EPUB - Testbuch'

book['book/toc.ncx/ncx/navMap/navPoint-1'].addChild('content', None, 'content')
book['book/toc.ncx/ncx/navMap/navPoint-1/content'].addAttribute('src', 'section-0001.html')

#==== CoverPage.html ===================================================================================
book.addChild('CoverPage.html', None, 'file')
book['book/CoverPage.html'].content = '<?xml version="1.0" encoding="utf-8" ?>\n'
book['book/CoverPage.html'].content += '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n'

book['book/CoverPage.html'].addChild('html', None, 'html')
book['book/CoverPage.html/html'].addAttribute('xmlns', 'http://www.w3.org/1999/xhtml')
book['book/CoverPage.html/html'].addAttribute('xml:lang', 'en')

book['book/CoverPage.html/html'].addChild('head', None, 'head')

book['book/CoverPage.html/html/head'].addChild('meta', None, 'meta')
book['book/CoverPage.html/html/head/meta'].addAttribute('http-equiv', 'Content-Type')
book['book/CoverPage.html/html/head/meta'].addAttribute('content', 'application/xhtml+xml; charset=utf-8')

book['book/CoverPage.html/html/head'].addChild('link', None, 'link')
book['book/CoverPage.html/html/head/link'].addAttribute('rel', 'stylesheet')
book['book/CoverPage.html/html/head/link'].addAttribute('type', 'text/css')
book['book/CoverPage.html/html/head/link'].addAttribute('href', 'styles.css')

book['book/CoverPage.html/html/head'].addChild('title', None, 'title')
book['book/CoverPage.html/html/head/title'].content = 'Cover Page'

book['book/CoverPage.html/html/head'].addChild('style', None, 'style')
book['book/CoverPage.html/html/head/style'].addAttribute('type', 'text/css')
book['book/CoverPage.html/html/head/style'].content = '@page { margin:0; }'

book['book/CoverPage.html/html'].addChild('body', None, 'body')
book['book/CoverPage.html/html/body'].addAttribute('style', 'margin: 0; padding: 0; oeb-column-number: 1; ')

book['book/CoverPage.html/html/body'].addChild('paragraph-001', None, 'p')
book['book/CoverPage.html/html/body/paragraph-001'].addAttribute('style', 'margin: 0; padding: 0; text-align: center')

book['book/CoverPage.html/html/body/paragraph-001'].addChild('content', None, 'img')
book['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('id', 'CoverImage')
book['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('src', 'Cover.jpg')
book['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('style', 'height: 100%; padding: 0; margin: 0;')
book['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('alt', 'Cover')


book.addChild('styles', None, 'styles')								# style elements for file styles.css


#=====================================================================================================
# eBook structure definition
#=====================================================================================================
book1 = eBookTreeElement('book', None, 'book')

#==== mimetype ========================================================================================
book1.addChild('mimetype', None, 'file')
book1['book/mimetype'].content = 'application/epub+zip'

#==== com.apple.ibooks.display-options.xml =================================================================
book1.addChild('com.apple.ibooks.display-options.xml', None, 'file')
book1['book/com.apple.ibooks.display-options.xml'].content = '<?xml version="1.0" encoding="UTF-8"?>\n'

book1['book/com.apple.ibooks.display-options.xml'].addChild('display_options', None, 'display_options')

book1['book/com.apple.ibooks.display-options.xml/display_options'].addChild('platform', None, 'platform')
book1['book/com.apple.ibooks.display-options.xml/display_options/platform'].addAttribute('name', '*', 'name')

book1['book/com.apple.ibooks.display-options.xml/display_options/platform'].addChild('option', None, 'option')
book1['book/com.apple.ibooks.display-options.xml/display_options/platform/option'].addAttribute('name', 'specified-fonts', 'name')
book1['book/com.apple.ibooks.display-options.xml/display_options/platform/option'].content = 'true'

#==== container.xml =====================================================================================
book1.addChild('container.xml', None, 'file')
book1['book/container.xml'].content = '<?xml version="1.0" ?>\n'

book1['book/container.xml'].addChild('container', None, 'container')
book1['book/container.xml/container'].addAttribute('version', '1.0', 'version')
book1['book/container.xml/container'].addAttribute('xmlns', 'urn:oasis:names:tc:opendocument:xmlns:container', 'xmlns')

book1['book/container.xml/container'].addChild('rootfiles', None, 'rootfiles')

book1['book/container.xml/container/rootfiles'].addChild('rootfile', None, 'rootfile')
book1['book/container.xml/container/rootfiles/rootfile'].addAttribute('full-path', 'OPS/content.opf', 'full-path')
book1['book/container.xml/container/rootfiles/rootfile'].addAttribute('media-type', 'application/oebps-package+xml', 'media-type')

#==== content.opf =======================================================================================
book1.addChild('content.opf', None, 'file')
book1['book/content.opf'].content = '<?xml version="1.0" encoding="UTF-8"?>\n'

book1['book/content.opf'].addChild('package', None, 'package')
book1['book/content.opf/package'].addAttribute('xmlns', 'http://www.idpf.org/2007/opf')
book1['book/content.opf/package'].addAttribute('unique-identifier', 'BookId')
book1['book/content.opf/package'].addAttribute('version', '2.0')

book1['book/content.opf/package'].addChild('metadata', None, 'metadata')
book1['book/content.opf/package/metadata'].addAttribute('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
book1['book/content.opf/package/metadata'].addAttribute('xmlns:dcterms', 'http://purl.org/dc/terms/')
book1['book/content.opf/package/metadata'].addAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
book1['book/content.opf/package/metadata'].addAttribute('xmlns:opf', 'http://www.idpf.org/2007/opf')

# Here metadata items will be inserted by eBook object

book1['book/content.opf/package'].addChild('manifest', None, 'manifest')

book1['book/content.opf/package/manifest'].addChild('toc_ncx', None, 'item')
book1['book/content.opf/package/manifest/toc_ncx'].addAttribute('id', 'toc_ncx')
book1['book/content.opf/package/manifest/toc_ncx'].addAttribute('href', 'toc.ncx')
book1['book/content.opf/package/manifest/toc_ncx'].addAttribute('media-type', 'application/x-dtbncx+xml')

book1['book/content.opf/package/manifest'].addChild('cover', None, 'item')
book1['book/content.opf/package/manifest/cover'].addAttribute('id', 'cover')
book1['book/content.opf/package/manifest/cover'].addAttribute('href', 'Cover.jpg')
book1['book/content.opf/package/manifest/cover'].addAttribute('media-type', 'image/jpeg')

book1['book/content.opf/package/manifest'].addChild('CoverPage_html', None, 'item')
book1['book/content.opf/package/manifest/CoverPage_html'].addAttribute('id', 'CoverPage_html')
book1['book/content.opf/package/manifest/CoverPage_html'].addAttribute('href', 'CoverPage.html')
book1['book/content.opf/package/manifest/CoverPage_html'].addAttribute('media-type', 'application/xhtml+xml')

book1['book/content.opf/package/manifest'].addChild('styles_css', None, 'item')
book1['book/content.opf/package/manifest/styles_css'].addAttribute('id', 'styles_css')
book1['book/content.opf/package/manifest/styles_css'].addAttribute('href', 'styles.css')
book1['book/content.opf/package/manifest/styles_css'].addAttribute('media-type', 'text/css')

book1['book/content.opf/package/manifest'].addChild('section-0001_html', None, 'item')
book1['book/content.opf/package/manifest/section-0001_html'].addAttribute('id', 'section-0001_html')
book1['book/content.opf/package/manifest/section-0001_html'].addAttribute('href', 'section-0001.html')
book1['book/content.opf/package/manifest/section-0001_html'].addAttribute('media-type', 'application/xhtml+xml')
 
book1['book/content.opf/package'].addChild('spine', None, 'spine')
book1['book/content.opf/package/spine'].addAttribute('toc', 'toc_ncx')

book1['book/content.opf/package/spine'].addChild('CoverPage_html', None, 'itemref')
book1['book/content.opf/package/spine/CoverPage_html'].addAttribute('idref', 'CoverPage_html')
book1['book/content.opf/package/spine/CoverPage_html'].addAttribute('linear', 'no')

book1['book/content.opf/package/spine'].addChild('section-0001_html', None, 'itemref')
book1['book/content.opf/package/spine/section-0001_html'].addAttribute('idref', 'section-0001_html')

#==== toc.ncx ==========================================================================================
book1.addChild('toc.ncx', None, 'file')
book1['book/toc.ncx'].content = '<?xml version="1.0" encoding="utf-8" ?>\n'
book1['book/toc.ncx'].content += '<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">\n'

book1['book/toc.ncx'].addChild('ncx', None, 'ncx')
book1['book/toc.ncx/ncx'].addAttribute('xmlns', 'http://www.daisy.org/z3986/2005/ncx/')
book1['book/toc.ncx/ncx'].addAttribute('xml:lang', 'en')
book1['book/toc.ncx/ncx'].addAttribute('version', '2005-1')

book1['book/toc.ncx/ncx'].addChild('head', None, 'head')

book1['book/toc.ncx/ncx/head'].addChild('dtb:uid', None, 'meta')
book1['book/toc.ncx/ncx/head/dtb:uid'].addAttribute('name', 'dtb:uid')
book1['book/toc.ncx/ncx/head/dtb:uid'].addAttribute('content', 'E-Pub Testbuch')

book1['book/toc.ncx/ncx/head'].addChild('dtb:depth', None, 'meta')
book1['book/toc.ncx/ncx/head/dtb:depth'].addAttribute('name', 'dtb:depth')
book1['book/toc.ncx/ncx/head/dtb:depth'].addAttribute('content', '1')

book1['book/toc.ncx/ncx/head'].addChild('dtb:totalPageCount', None, 'meta')
book1['book/toc.ncx/ncx/head/dtb:totalPageCount'].addAttribute('name', 'dtb:totalPageCount')
book1['book/toc.ncx/ncx/head/dtb:totalPageCount'].addAttribute('content', '0')

book1['book/toc.ncx/ncx/head'].addChild('dtb:maxPageNumber', None, 'meta')
book1['book/toc.ncx/ncx/head/dtb:maxPageNumber'].addAttribute('name', 'dtb:maxPageNumber')
book1['book/toc.ncx/ncx/head/dtb:maxPageNumber'].addAttribute('content', '0')

book1['book/toc.ncx/ncx'].addChild('docTitle', None, 'docTitle')

book1['book/toc.ncx/ncx/docTitle'].addChild('text', None, 'text')
book1['book/toc.ncx/ncx/docTitle/text'].content = 'EPUB - Testbuch'

book1['book/toc.ncx/ncx'].addChild('navMap', None, 'navMap')

book1['book/toc.ncx/ncx/navMap'].addChild('navPoint-1', None, 'navPoint')
book1['book/toc.ncx/ncx/navMap/navPoint-1'].addAttribute('id', 'navPoint-1')
book1['book/toc.ncx/ncx/navMap/navPoint-1'].addAttribute('playOrder', '1')

book1['book/toc.ncx/ncx/navMap/navPoint-1'].addChild('navLabel', None, 'navLabel')

book1['book/toc.ncx/ncx/navMap/navPoint-1/navLabel'].addChild('text', None, 'text')
book1['book/toc.ncx/ncx/navMap/navPoint-1/navLabel/text'].content = 'EPUB - Testbuch'

book1['book/toc.ncx/ncx/navMap/navPoint-1'].addChild('content', None, 'content')
book1['book/toc.ncx/ncx/navMap/navPoint-1/content'].addAttribute('src', 'section-0001.html')

#==== CoverPage.html ===================================================================================
book1.addChild('CoverPage.html', None, 'file')
book1['book/CoverPage.html'].content = '<?xml version="1.0" encoding="utf-8" ?>\n'
book1['book/CoverPage.html'].content += '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n'

book1['book/CoverPage.html'].addChild('html', None, 'html')
book1['book/CoverPage.html/html'].addAttribute('xmlns', 'http://www.w3.org/1999/xhtml')
book1['book/CoverPage.html/html'].addAttribute('xml:lang', 'en')

book1['book/CoverPage.html/html'].addChild('head', None, 'head')

book1['book/CoverPage.html/html/head'].addChild('meta', None, 'meta')
book1['book/CoverPage.html/html/head/meta'].addAttribute('http-equiv', 'Content-Type')
book1['book/CoverPage.html/html/head/meta'].addAttribute('content', 'application/xhtml+xml; charset=utf-8')

book1['book/CoverPage.html/html/head'].addChild('link', None, 'link')
book1['book/CoverPage.html/html/head/link'].addAttribute('rel', 'stylesheet')
book1['book/CoverPage.html/html/head/link'].addAttribute('type', 'text/css')
book1['book/CoverPage.html/html/head/link'].addAttribute('href', 'styles.css')

book1['book/CoverPage.html/html/head'].addChild('title', None, 'title')
book1['book/CoverPage.html/html/head/title'].content = 'Cover Page'

book1['book/CoverPage.html/html/head'].addChild('style', None, 'style')
book1['book/CoverPage.html/html/head/style'].addAttribute('type', 'text/css')
book1['book/CoverPage.html/html/head/style'].content = '@page { margin:0; }'

book1['book/CoverPage.html/html'].addChild('body', None, 'body')
book1['book/CoverPage.html/html/body'].addAttribute('style', 'margin: 0; padding: 0; oeb-column-number: 1; ')

book1['book/CoverPage.html/html/body'].addChild('paragraph-001', None, 'p')
book1['book/CoverPage.html/html/body/paragraph-001'].addAttribute('style', 'margin: 0; padding: 0; text-align: center')

book1['book/CoverPage.html/html/body/paragraph-001'].addChild('content', None, 'img')
book1['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('id', 'CoverImage')
book1['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('src', 'Cover.jpg')
book1['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('style', 'height: 100%; padding: 0; margin: 0;')
book1['book/CoverPage.html/html/body/paragraph-001/content'].addAttribute('alt', 'Cover')


book1.addChild('styles', None, 'styles')								# style elements for file styles.css


def start():
	print 'Ready'
	