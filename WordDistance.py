word1=list(input("Enter a word"))
word2=list(input("Enter a word"))
def alpha(w):
    s=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    for i in range(len(s)):
        if(s[i]==w):
            return i
def distance(word1,word2):
    if(len(word1)!=len(word2)):
        return -1
    else:
        s=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        sum=0
        s1=[]
        for i in range(len(word1)):
            s1.append(word1[i])
            s1.append(word2[i])
            sum=sum+ abs(alpha(s1[0])-alpha(s1[1]))
            s1.remove(word1[i])
            s1.remove(word2[i])
    return sum
print(distance(word1,word2))                 