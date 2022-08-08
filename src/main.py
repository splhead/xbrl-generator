from xml.etree.ElementTree import Element, SubElement, tostring, indent

def prettify(element):
  indent(element)
  return tostring(element, 'utf-8',xml_declaration=True)

xbrl = Element('xbrl')

link_schema_ref = SubElement(xbrl,'link:schemaRef')
link_schema_ref.set('xlink:href', 'aapl-20200926.xsd')
link_schema_ref.set('xlink:type', 'simple')

with open("./src/instance.xml", "wb") as file:
  file.write(prettify(xbrl))
