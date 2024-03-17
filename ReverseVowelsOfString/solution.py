def reverseVowels( s: str) -> str:

    slist = [l for l in s]

    vowels = set(['a','e','i','o','u','A','E','I','O','U'])
    start = 0
    end = len(s)-1
    while(start < end ):
        while start < end and slist[start] not in vowels:
            start += 1
            
        while end > start and slist[end] not in vowels:
            end -= 1
 
        slist[start],slist[end] = slist[end], slist[start]
        start += 1
        end -= 1
        # if slist[start] in vowels and slist[end] in vowels:
        #    slist[start],slist[end] = slist[end], slist[start]
        #    start += 1
        #    end -= 1
        # else:
        #     if slist[start] not in vowels:
        #         start += 1
            
        #     if slist[end] not in vowels:
        #         end -= 1     

    return "".join(slist)
print(reverseVowels("leetcode"))
print(reverseVowels("elprogramadorgt"))