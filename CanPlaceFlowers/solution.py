def canPlaceFlowers( flowerbed: list[int], n: int) -> bool:

    if n == 0:
        return True
#n 1
#[0,0,0,0,0]
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n = n - 1
            if n == 0:
                print(flowerbed)
                return True
    return False
    print(n)
    print(flowerbed)
    i = -1
    # while( n > 0 ):
    #     i = i + 1
    #     print(i)
    #     print(len(flowerbed),"len")

    #     if(i > len(flowerbed)):
    #         print("si puede ser mayor")
    #         break


    #     if( len(flowerbed) == i):
    #         print("no es mayor")
    #         break
    #     if(flowerbed[i] == 1):
    #         continue
        
    #     if 

    #     if(i == 0 and (flowerbed[i] == 0 and flowerbed[i+1] == 0)):
    #         print(flowerbed)
    #         flowerbed[i] = 1
             
    #         n = n - 1
    #         if(n == 0):
    #             return True
    #         continue 
    #     elif(i == len(flowerbed)-1):
    #         if(flowerbed[i-1] == 0):
    #             flowerbed[i] = 1
    #             n = n - 1
    #             if(n == 0):
    #                 return True
    #     else:
    #         print("arrayoutofbound ",i)
    #         if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
    #             flowerbed[i] = 1
    #             i = i + 1
    #             n = n - 1
    #             if(n == 0):
    #                 return True



    
    # print(flowerbed)
    # return False



#[1 0 0 0 1]

#case 1
#[0,0,1]

flowerbed = [0,0,0,0,0]

n = 1
print(canPlaceFlowers(flowerbed,n))


# flowerbed = [1,0,1,0,0]
# n = 1
# print(canPlaceFlowers(flowerbed,n))


# flowerbed = [0,0,0,1]
# n = 2
# print(canPlaceFlowers(flowerbed,n))
    
# flowerbed = [1,0,0,0,1]
# canPlaceFlowers(flowerbed,n)