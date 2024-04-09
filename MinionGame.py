string=list(input())
s1=0
s2=0    
consonant1=list("BCDFGHJKLMNPQRSTVWXYZ")
vowel=list("AEIOU")
for i in range(len(string)):
    if(string[i] in consonant1):
        for j in range(len(string),0,-1):
            word="".join(string[i:j])
            if(word!=""):
                s1+=1

    elif(string[i] in vowel):
        for j in range(len(string),0,-1):
            word="".join(string[i:j])
            if(word!=""):
                s2+=1     
            
if(s1>s2):
    print("Stuart",s1)
elif(s2>s1):
    print("Kevin",s2)
else:
    print("Draw")