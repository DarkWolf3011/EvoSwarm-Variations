import csv
import pandas as pd 

LINES = True

in_file = r'C:\users\josed\documents\github\EvoSwarm-Variations\OG.csv'

out_file =  r'C:\users\josed\documents\github\EvoSwarm-Variations\ProcedOG.csv'

auxinst = ''

aux = 0
caux = 0
Writelist = []
ListDispo = []
auxstring = ''

with open(in_file) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if int(row[3]) == 1:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 2:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 3:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 9:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 10:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 15:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 17:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 18:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 21:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        
        elif int(row[3]) == 22:
            if int(row[0]) == 10:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)
            else:
                if int(row[1]) == 1:
                    ListDispo.clear()
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==2:
                    if caux == 0:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==3:
                    print('aqui : '+str(caux))
                    if caux == 1:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==4:
                    if caux == 2:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==5:
                    if caux == 3:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==6:
                    if caux == 4:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==7:
                    if caux == 5:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==8:
                    if caux == 6:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==9:
                    if caux == 7:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==10:
                    if caux == 8:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==11:
                    if caux == 9:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==12:
                    if caux == 10:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==13:
                    if caux == 11:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==14:
                    if caux == 12:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==15:
                    if caux == 13:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==16:
                    if caux == 14:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==17:
                    if caux == 15:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==18:
                    if caux == 16:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==19:
                    if caux == 17:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==20:
                    if caux == 18:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==21:
                    if caux == 19:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==22:
                    if caux == 20:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==23:
                    if caux == 21:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==24:
                    if caux == 22:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==25:
                    if caux == 23:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==26:
                    if caux == 24:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==27:
                    if caux == 25:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==28:
                    if caux == 26:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                elif int(row[1])==29:
                    if caux == 27:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]
                    
                elif int(row[1])==30:
                    if caux == 28:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux +=1
                    
                    ListDispo.append(float(row[2]))
                    auxinst = row[1]

                if caux == 29:
                        aux = 0
                        aux = min(ListDispo, key=abs)
                        auxstring = ''+row[0]+','+auxinst+','+str(aux)+','+row[3]
                        Writelist.append(auxstring)
                        ListDispo.clear()
                        caux = 0
                        print(Writelist)        

      

with open(out_file, mode= 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for element in Writelist:    
        csv_writer.writerow(element.split(','))