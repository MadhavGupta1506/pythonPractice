def josephus(n, k):
    print(n,k)
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1
n = 25 #Number of soldiers
k = 3 #Elimination factor
result = josephus(n, k)
print(result)