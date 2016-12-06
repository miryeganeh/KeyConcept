from __future__ import with_statement

# Documentation
# This Code replcae Titles with an ID

infile=open("WekaInput.csv").readlines()
outfile=open("WekaInputIdentifier.csv",'w')

count=-1
previous=infile[0].split(",")[0]
for line in infile:
    newline=""
    if count==-1:
        newline=infile[0]
        count+=1
    else:
        print line , line.split(",")[0]
        if line.split(",")[0]==previous:
            newline=line.replace(line.split(",")[0],str(count))
        else:
            previous=line.split(",")[0]
            count+=1
            newline=line.replace(line.split(",")[0],str(count))
    outfile.write(newline)
outfile.close()