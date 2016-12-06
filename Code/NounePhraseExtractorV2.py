__author__ = 'nimayeganeh'

from MontyLib import MontyLingua
import xml.etree.ElementTree as ET
import json

# Documentation
# this Code Extracts the nounePhrases from a bad formated file and writes them to a well-formated xml 

theTagger = MontyLingua.MontyLingua()


lines=open("topics.51-100", "r")


file=lines.readlines()
Outroot = ET.Element("topics")
identifier=""
description=""
title=""
for i in range(file.__len__()):

    if "<num>" in file[i]:
        identifier=file[i].split(":")[1].strip()
    if "<title>" in file[i] :
        title=file[i].split(':')[1].strip()
    if "<desc>" in file[i] :
        j=i+1
        while True:
            if "<" not in file[j]:
                description+=file[j]
            else:
                break
            j+=1
    if identifier!="" and description!="" and title!="":
        description=description.replace("\n"," ").strip()
        identifier=identifier.strip()
        doc = ET.SubElement(Outroot, "query" , identifier=identifier)
        ET.SubElement(doc, "title").text = title
        ET.SubElement(doc, "desc").text = description
        tagString = theTagger.jist(description)
        for noune in tagString[0]['noun_phrases']:
            ET.SubElement(doc, "NounePhrase", weight="0").text = noune

        identifier=""
        description=""
        title=""


Outtree = ET.ElementTree(Outroot)
Outtree.write("APOut2.xml")