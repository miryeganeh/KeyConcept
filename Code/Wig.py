from __future__ import division
import xml.etree.ElementTree as ET
import json
import math

# Documentation
# Calculate Wig


def Wig(String , Qnumber ,secondPhrase):
    RetFile=open("Retreival","r").readlines()
    documents=[]
    sum=0.0
    for line in RetFile:
        if line.split(" ")[0].strip() == str(Qnumber):
            documents.append(line.split()[2].strip())
    documents.sort()
    DocFile=open("ap.txt","r").readlines()
    for item in documents:
        print item
        Found=False
        doc=""
        for i in range(DocFile.__len__()):
            if "DOCNO" in DocFile[i]:
                if item in DocFile[i]:
                    print "found"
                    Found=True
            if Found==True:
                if "<TEXT>" in DocFile[i]:
                    j=i+1
                    while "</TEXT>" not in DocFile[j]:
                        doc+=DocFile[j+1]
                        j+=1
                elif "</DOC>" in DocFile[i]:
                    Found=False
                    break
        if doc!="":
            print "entered"
            tf=0
            docLength=0
            for DocLine in doc.splitlines():
                tf+=DocLine.lower().count(String.strip().lower())
                docLength+=DocLine.split().__len__()
            firstPhrase=(tf+.05)/docLength
            sum+=math.log(firstPhrase,10)-math.log(secondPhrase,10)
    return sum


#
# tree = ET.parse('AP-tagged.xml')
# root = tree.getroot()
#
#
# count=1
# for child in root:
#     NounePhrase=""
#     for attr in child:
#         if attr.tag=="NounePhrase":
#             NounePhrase=attr.text
#             Wig(NounePhrase,count,0)
#             count+=1
#
#
