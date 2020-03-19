"""
"""
import xml.etree.ElementTree as ET
import re

class Xml(object):
    """
    """
    VsDataContainer = ["WTC1EENB14L", "1"]
    def __init__(self, fileName, requiredTags):
        """
        """
        self.root = fileName
        self.requiredTags = requiredTags

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, fileName):
        tree = ET.parse(fileName)
        self._root = tree.getroot()

    def parse(self, parent):
        """
        """
        for key in self.requiredTags:
            if re.search("^{.*}%s$"%key, parent.tag):
                if not parent.attrib["id"] in self.requiredTags[key]:
                    return None
        jList = []
        children = parent.getchildren()
        if not children:
            attributes = parent.attrib
            text = parent.text
            return {parent.tag:[{"text":text},{"attributres":attributes}]}
        for child in children:
            jList.append(self.parse(child))
        return {parent.tag:[{"attributes":parent.attrib}, jList]}






