from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        
    """

    zp = 0

    for i in range(len(nums)):

        if nums[i] != 0:

            nums[zp] , nums[i]= nums[i] ,nums[zp]
            zp += 1



    return nums   

    zp = 0

    for n in enumerate(nums):

        if n[1] != 0:

            nums[zp] , nums[n[0]]= n[1] ,nums[zp]
            zp += 1



    return nums    
        
 



nums = [4,1,0,3,12]

print(moveZeroes(nums))