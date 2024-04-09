l=[]

Queue=[]
string=""
while(string!="END"):
    string=input()
    l.append([string])
for i in range(len(l)):
    if(l[i][0]=='JOIN'):
        Queue.append(l[i][1])
        head=Queue[0]
    elif(l[i][0]=='PRINT'):
        print(','.join(map(str, Queue)))
    elif(l[i][0]=='LEAVE'):
        Queue.pop(0)
        tail=Queue[-1]
    elif(l[i][0]=='MOVE' and l[i][2]=="TAIL"):
        
        Queue.append([l[i][2]])
        tail=Queue[-1]
    elif(l[i][0]=='MOVE' and l[i][2]=="HEAD"):        
        head=Queue[l[i][2]]
        Queue.insert[0,l[i][2]]