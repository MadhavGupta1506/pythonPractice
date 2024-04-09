n=int(input())
s=set(map(int,input().split(" "))) 
nOperation=int(input())
operationList=[]
for i in range(nOperation):
    operationList.append(input().split(" "))
print(operationList)
for i in range(nOperation):
    if(operationList[i][0]=="pop"):
        s.pop()
    elif(operationList[i][0]=="remove"):
        s.remove(int(operationList[i][1]))
    elif(operationList[i][0]=="discard"):
        s.discard(int(operationList[i][1]))
print(sum(s))