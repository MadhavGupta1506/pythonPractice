vowel=list("AEIOU")
string=list(input())
Kevin_score=Stuart_score=0
string="BANANA"
for i in range(len(string)):
    if(string[i] in vowel):
        Kevin_score+=len(string)-i
    else:
        Stuart_score+=len(string)-i
if(Kevin_score>Stuart_score):
    print("Kevin",Kevin_score)
elif(Kevin_score<Stuart_score):
    print("Stuart",Stuart_score)

else:
    print("Draw")