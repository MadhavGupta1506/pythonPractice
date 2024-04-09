l=[]
n=int(input())
for i in range(n):
    name = input()
    score = float(input())
    l.append([name,score])
low="0"
temp=float(100.0)
sec_low=low
for i in range(n):
    if( l[i][1]<=temp):
        sec_low=sec_low.replace(sec_low,low) 
        low=low.replace(low,l[i][0])
        temp=l[i][1]  
if(low.islower()>sec_low.islower()):
    print(sec_low ,"\n", low)
else:
    print(low ,"\n",sec_low)
# print(low)
# print(sec_low)