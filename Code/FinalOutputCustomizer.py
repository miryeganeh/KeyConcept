__author__ = 'nimayeganeh'


InFile=open("../Output/Final.csv").readlines()
OutFile=open("../Output/FinalCustomized.csv",'w')

count=0
max=0
previous=1
Outline=""
Sec_Outline=""
for line in InFile:
    if count==0:
        count+=1
        OutFile.write("Query#,NounePhrase,label,P(ci|q)\n")
        continue
    else:
        Qnum=line.split(",")[0]
        if int(Qnum)==previous:
            NounPhrase=line.split(",")[1]
            label=line.split(",")[7]
            prob=line.split(",")[9]
            if float(prob)>max:
                max=float(prob)
                Outline=Qnum+","+NounPhrase+","+label+","+prob

        else:
            second_max=0
            for second_line in InFile:
                Sec_Qnum=second_line.split(",")[0]
                if Sec_Qnum==str(int(Qnum)-1):
                    Sec_NounPhrase=second_line.split(",")[1]
                    Sec_label=second_line.split(",")[7]
                    Sec_prob=second_line.split(",")[9]
                    if float(Sec_prob)>second_max and float(Sec_prob)<max:
                        second_max=float(Sec_prob)
                        Sec_Outline=Sec_Qnum+","+Sec_NounPhrase+","+Sec_label+","+Sec_prob
            OutFile.write(Outline+Sec_Outline)
            previous=int(Qnum)
            max=0
            NounPhrase=line.split(",")[1]
            label=line.split(",")[7]
            prob=line.split(",")[9]
            if float(prob)>max:
                max=float(prob)
                Outline=Qnum+","+NounPhrase+","+label+","+prob
        count+=1

second_max=0
for second_line in InFile:
    Sec_Qnum=second_line.split(",")[0]
    if Sec_Qnum==Qnum:
        Sec_NounPhrase=second_line.split(",")[1]
        Sec_label=second_line.split(",")[7]
        Sec_prob=second_line.split(",")[9]
        if float(Sec_prob)>second_max and float(Sec_prob)<max:
            second_max=float(Sec_prob)
            Sec_Outline=Sec_Qnum+","+Sec_NounPhrase+","+Sec_label+","+Sec_prob
OutFile.write(Outline+Sec_Outline)

OutFile.close()