from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prev = 1
    for i in range(len(nums)):
        res[i] *= prev
        prev *= nums[i]
        print("i")

    prev = 1
    for r in range(len(nums)-1,-1,-1):
      
        res[r] *= prev
        prev *= nums[r]
        print("j")
    



def function2(nums):
    res = [1] * len(nums)
    for i in range(len(nums)):
        #  print("Itero i vez",i)
         for k in range(len(nums)):
            print("Itero k",k)
            if(k != i):
                res[i] *=  nums[k]
 
    print(res)


a = [2,5,3,4]
a = [1,2,3,4,3,1,2,4,2,3,4,1]
print(a)
function2(a)


