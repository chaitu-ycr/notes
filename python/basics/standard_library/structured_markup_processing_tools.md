
# Python Structured Markup Processing Tools

Below are detailed descriptions and usage examples for key Python standard libraries related to HTML and XML processing.

---

## html — HyperText Markup Language Support

**Description:**  
Provides utilities for working with HTML, including escaping and unescaping special characters.

**Usage Example:**
```python
import html

escaped = html.escape('<div>Hello & "world"</div>')
print(escaped)  # '&lt;div&gt;Hello &amp; &quot;world&quot;&lt;/div&gt;'
unescaped = html.unescape(escaped)
print(unescaped)  # '<div>Hello & "world"</div>'
```

---

## html.parser — Simple HTML and XHTML Parser

**Description:**  
Implements a simple parser for HTML and XHTML documents.

**Usage Example:**
```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start tag:", tag)

parser = MyHTMLParser()
parser.feed('<html><body><h1>Title</h1></body></html>')
```

---

## html.entities — Definitions of HTML General Entities

**Description:**  
Provides definitions for HTML general entities.

**Usage Example:**
```python
import html.entities

print(html.entities.name2codepoint['amp'])  # 38
```

---

# Python XML Processing Modules

---

## xml.etree.ElementTree — The ElementTree XML API

**Description:**  
Provides a simple and efficient API for parsing and creating XML data.

**Usage Example:**
```python
import xml.etree.ElementTree as ET

tree = ET.ElementTree(ET.fromstring('<root><child/></root>'))
root = tree.getroot()
print(root.tag)  # 'root'
```

---

## xml.dom — The Document Object Model API

**Description:**  
Implements the W3C Document Object Model (DOM) API for XML documents.

**Usage Example:**
```python
import xml.dom.minidom

doc = xml.dom.minidom.parseString('<root><child/></root>')
print(doc.documentElement.tagName)  # 'root'
```

---

## xml.dom.minidom — Minimal DOM Implementation

**Description:**  
Provides a lightweight DOM implementation for XML.

**Usage Example:**
```python
from xml.dom.minidom import parseString

doc = parseString('<root><child/></root>')
print(doc.documentElement.tagName)  # 'root'
```

---

## xml.dom.pulldom — Support for Building Partial DOM Trees

**Description:**  
Supports building partial DOM trees from XML documents.

**Usage Example:**
```python
from xml.dom.pulldom import parseString

events = parseString('<root><child/></root>')
for event, node in events:
	if event == 'START_ELEMENT':
		print(node.tagName)
```

---

## xml.sax — Support for SAX2 Parsers

**Description:**  
Provides support for SAX2 (Simple API for XML) parsers.

**Usage Example:**
```python
import xml.sax

class MyHandler(xml.sax.ContentHandler):
	def startElement(self, name, attrs):
		print('Start element:', name)

xml.sax.parseString('<root><child/></root>', MyHandler())
```

---

## xml.sax.handler — Base Classes for SAX Handlers

**Description:**  
Defines base classes for SAX event handlers.

**Usage Example:**
```python
from xml.sax.handler import ContentHandler

class MyHandler(ContentHandler):
	def startElement(self, name, attrs):
		print('Start element:', name)
```

---

## xml.sax.saxutils — SAX Utilities

**Description:**  
Provides utility functions for working with SAX parsers.

**Usage Example:**
```python
from xml.sax.saxutils import escape

print(escape('<tag>'))  # '&lt;tag&gt;'
```

---

## xml.sax.xmlreader — Interface for XML Parsers

**Description:**  
Defines the interface for XML parsers in the SAX API.

**Usage Example:**
```python
from xml.sax.xmlreader import XMLReader

# Typically used as a base for custom parser implementations.
```

---

## xml.parsers.expat — Fast XML Parsing Using Expat

**Description:**  
Provides fast, non-validating XML parsing using the Expat library.

**Usage Example:**
```python
import xml.parsers.expat

parser = xml.parsers.expat.ParserCreate()
def start_element(name, attrs):
	print('Start element:', name)
parser.StartElementHandler = start_element
parser.Parse('<root><child/></root>')
```

---
