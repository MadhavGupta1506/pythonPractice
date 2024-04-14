def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maximum=0
    l=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            print(i,j)
            if(prices[i]<prices[j] and prices[j]-prices[i]>maximum):
                maximum=prices[j]-prices[i]
                # print(maximum)
    return maximum
print(maxProfit([1,2]))