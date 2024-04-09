s="madhav gupta"
def solve(s):
    s=list(s)
    for i in range(len(s)):
        if(i==0 or s[i-1]==" "):
            s[i]=str(s[i]).capitalize()
    return "".join(s)
print(solve(s))