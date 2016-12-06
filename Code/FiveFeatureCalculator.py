from __future__ import division

import xml.etree.ElementTree as ET
import json
import math
import Wig
import csv

# Documentation
#this Code calculates all 5 features for every nounePhrase and writes them to a CSV file as Weka Input

def Is_Big( String ):
    for word in String.split(" "):
        if word[0].islower():
            return 0
    return 1


def MainFuction( String ,number ):
    # xml file was not well formated , so i read it like a text file

    RetFile=open("Retreival","r").readlines()
    documents=[]
    sum=0.0
    for line in RetFile:
        if line.split(" ")[0].strip() == str(number):
            documents.append(line.split()[2].strip())
    documents.sort()

    file = open("ap.txt", "r")
    read=False
    DocCount=0
    count=0
    tf=0
    specialTF=0
    specialCount=0
    found=False
    special=False  #indicate that if a document is in the top 50

    wigPhrases=[]

    for line in file:
        if "DOCNO" in line:
            for item in documents:
                if item in line:
                    special=True
        if "</TEXT>" in line:
            read=False
            if found:
                count+=1
                found=False
            if special:
                if specialCount!=0:
                    firstPhrase=(specialTF+.05)/specialCount
                firstPhrase=0
                wigPhrases.append(firstPhrase)
                special=False
                specialTF=0
                specialCount=0

        if read:
            if special:
                specialTF+=line.lower().count(String.strip().lower())
                specialCount+=line.split().__len__()

            if String.strip().lower() in line.lower():
                tf+=line.lower().count(String.strip().lower())
                found=True
        if "<TEXT>" in line:
            read=True
            DocCount+=1

    file.close()

    x=(DocCount+1)/(count+.5)
    idf=math.log(x,2)
    teta=0-(tf+1)/DocCount
    ridf=idf-math.log(1/(1-math.exp(teta)),2)

    WigNumerator=0
    WigDenominator=tf/DocCount
    wig=0
    if wigPhrases.__len__() !=0 and WigDenominator!=0:
        for each in wigPhrases:
            WigNumerator+=math.log(each+0.5,10)-math.log(WigDenominator,10)

    print "*********** " , wigPhrases.__len__() , "***" , String
    if WigDenominator!=0:
        wig=0-(WigNumerator/WigDenominator)/50
        print "This is Wig numerator: " ,WigNumerator ,"----" , count
    return [tf,idf,ridf,wig]



#######  main

tree = ET.parse('AP-tagged.xml')
root = tree.getroot()

Outroot = ET.Element("topics")


with open('WekaInput.csv', 'r+ a') as csvfile:
    fieldnames = ['title','NounePhrase', 'IsBig','tf','idf','ridf','wig','weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writen=csvfile.readlines().__len__()
    if writen==0:
        writer.writeheader()
    count=1
    for child in root:
        NounePhrase=""
        weight=""
        description=""
        title=""
        for attr in child:
            if attr.tag=="NounePhrase":
                NounePhrase=attr.text
                weight=str(attr.attrib).split("\'")[3]
            if attr.tag=="title":
                title=attr.text

            if NounePhrase!="":
                if count >= writen:
                    result=MainFuction(NounePhrase,count)
                    print count , "###" , NounePhrase , "----> tf:",result[0] , "***** idf:" , result[1] , "***** ridf:" , result[2], "***** wig:" , result[3]
                    writer.writerow({'title': title, 'NounePhrase': NounePhrase, 'IsBig':Is_Big(NounePhrase), 'tf':result[0] , 'idf':result[1] , 'ridf':result[2] ,'wig':result[3],'weight':weight})
                count+=1