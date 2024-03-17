# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.


# def increasingTriplet(nums) ->bool:

#     if len(nums) < 3:
#         return False

#     first = float('inf')
#     second = float('inf')
#     for x in nums:
        
#         if x > second and second > first: 
#             print(first, second, x)
#             return True
        
#         if x  > first: 
#             if x < second:
#                 second = x

#         else:
#             first = x



#     return False



        



# nums = [3,2,4,5,8]

# nums = [3,2,4,4,8]
# nums = [5,1,5,5,2,5,4]
# print(increasingTriplet(nums))


def increasingTreplet(nums):
    length = len(nums)
    response = False
    for i in range(length):
        j = i + 1
        k = j + 1   
       
      
        if (k > length):
            break

        
        # print(nums[i] , nums[j] , nums[j])
        

        if(k == length): 
            print("igual")
        

        if nums[i] < nums[j] :
            print("es menor")
            if  nums[j] < nums[k]:
                print("no se evaluo")
        else:
            print(nums[i],nums[j],"keee")
        
        
        # if (nums[i] < nums[j] < nums[k]):
        if (nums[i] < nums[j] and nums[j] < nums[k]):
            response = True
            break
 
    return response
 
mylist = [5,1,5,5,8,5,4]
print(increasingTreplet(mylist))