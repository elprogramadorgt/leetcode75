def edu_max(items):
    max = items[0]
    for i in range(1,len(items)):
        if items[i] > max:
            max = items[i]
    return max
def kidsWithCandies(candies, extraCandies):
    max = edu_max(candies)
    res = []

    for i in range(len(candies)):
        if candies[i]+extraCandies >= max:
            res.append(True)
        else:
            res.append(False)

    return res

candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies,extraCandies))