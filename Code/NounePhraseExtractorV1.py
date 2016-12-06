__author__ = 'nimayeganeh'

from MontyLib import MontyLingua
import xml.etree.ElementTree as ET
import json

# Documentation
# this Code Extracts nounPhrases from an xml file and writes them to another xml file

theTagger = MontyLingua.MontyLingua()


tree = ET.parse('English_topics_AH.xml')
root = tree.getroot()

Outroot = ET.Element("topics")

for child in root:
    identifier=""
    description=""
    title=""
    for attr in child:
        if attr.tag=="identifier":
            identifier=attr.text
        if attr.tag=="description":
            description=attr.text
        if attr.tag=="title":
            title=attr.text
    doc = ET.SubElement(Outroot, "query" , identifier=identifier)
    ET.SubElement(doc, "title").text = title
    tagString = theTagger.jist(description)
    for noune in tagString[0]['noun_phrases']:
        ET.SubElement(doc, "NounePhrase", weight="0").text = noune

Outtree = ET.ElementTree(Outroot)
Outtree.write("OutPut.xml")