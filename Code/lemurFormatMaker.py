__author__ = 'nimayeganeh'

from MontyLib import MontyLingua
import xml.etree.ElementTree as ET
import json

# Documentation
# This code make a file that is suitable for Lemur Input QueryFile

tree = ET.parse('AP-tagged.xml')
root = tree.getroot()


Outroot = ET.Element("DOC")

DocCount=1
for child in root:

    for attr in child:
        NounePhrase=""
        NounePhrase+="\n"
        if attr.tag=="NounePhrase":
            doc = ET.SubElement(Outroot, "DOCNO" ).text=str(DocCount)
            for part in attr.text.split(" "):
                NounePhrase+=part.strip()+"\n"
            print NounePhrase
            text = ET.SubElement(Outroot, "TEXT" ).text=NounePhrase
            DocCount+=1
    print "******"

Write = ET.ElementTree(Outroot)
Write.write("lemur-formated.xml")