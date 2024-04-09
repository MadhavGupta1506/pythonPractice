l=[1,2,3,4,5,5,5,19,19]
nineteen=0
five=0
for i in l:
    if(i==19):
        nineteen+=1
    elif(i==5):
        five+=1
if((nineteen==2) and (five>=3)):
    print(True)
else:
    print(False)