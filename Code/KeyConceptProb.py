__author__ = 'nimayeganeh'

# Documentation
# This Code analyses the Weka Output and calculates the probability of lable for each NounePhrase


# reading Weka's Output and Sort it

Wekafil=open("WekaOutput.txt").readlines()


Predicted=[]
for sort in range(1,740):
    for line in Wekafil:
        if line.split(",")[5].strip()==str(sort):
            Predicted.append(line.strip())
            break


# Reading CSV file

CsvFile=open("WekaInputIdentifier.csv").readlines()

Prev=1
sum_prob=0
sums=[]
for i in range(0,CsvFile.__len__()):
    if CsvFile[i].split(",")[0].isdigit():
        number=CsvFile[i].split(",")[0]
        if str(Prev)==number:
            prob=Predicted[i-1].split(",")[4]
            sum_prob+=float(prob)
        else:
            sums.append(sum_prob)
            sum_prob=0
            prob=Predicted[i-1].split(",")[4]
            sum_prob+=float(prob)
            Prev+=1
sums.append(sum_prob)

outfile=open("Final.csv",'w')
outfile.write('Query#'+',NounePhrase'+ ',IsBig'+',tf'+',idf'+',ridf'+',wig'+',label'+',hk(ci)'+',P(ci|q)\n')
for i in range(0,CsvFile.__len__()):
    if CsvFile[i].split(",")[0].isdigit():
        number=CsvFile[i].split(",")[0]
        # print Predicted[i-1]
        prob=Predicted[i-1].split(",")[4]

        outfile.write(CsvFile[i].strip()+','+prob+','+str(float(prob)/sums[int(number)-1])+"\n")
outfile.close()
