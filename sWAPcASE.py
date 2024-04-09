string="Www.HackerRank.com"

def sWAPcASE(s:list):
    s1=[]
    for i in range(len(s)):
        if(s[i].islower()):
            s1.append(s[i].upper())
        else:
            s1.append(s[i].lower())
    s1="".join(s1)
    return s1
print(sWAPcASE(string))