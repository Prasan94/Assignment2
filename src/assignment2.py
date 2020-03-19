"""
"""
from XML import Xml

xmlToBeParsed = r'C:\Users\prasanhe\Desktop\Assignment\sample.xml'
requiredTags = {"VsDataContainer":["WTC1EENB14L", "1"]}

xmlObj = Xml(xmlToBeParsed, requiredTags)
preparedJson = xmlObj.parse(xmlObj.root)

print preparedJson
