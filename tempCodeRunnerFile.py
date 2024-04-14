def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n1=nums
    for i in range(0,len(nums)):
        print(nums[i])
        t=nums[i]

        n1.remove(t)
        if(t in n1):
            return True
    return False