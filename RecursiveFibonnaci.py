def steps(n):
    if(n==0):
      return 0
    elif(n<4):
      return n  
    else:
        return steps(n-1)+steps(n-2)+steps(n-3)

print(steps(5))