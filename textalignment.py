n=5
for i in range(n*n):
    for j in range(n*n):
        if(i<n) and(j<n):
            print("H".center(n," "),end="")