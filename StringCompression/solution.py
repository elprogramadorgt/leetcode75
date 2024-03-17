from typing import List


# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: 
# ["a","2","b","2","c","3"]

# Input: chars = ["a","a","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: 
# ["a","2","b","c","3"]


class Solution:
    def compress(self, chars: List[str]) -> int:

        pos, i = 0,0
        
        while i < len(chars):

            counter = 0
            currChar = chars[i]

            while i < len(chars) and currChar == chars[i]:
                counter += 1
            
                i += 1  

            chars[pos] = currChar
            pos += 1
        
            if counter > 1:
                for x in str(counter):
                    chars[pos] = x
                    pos += 1
            
            

                

        return pos

chars = ["a","a","b","b","c","c","c","d","d"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

s = Solution()
print(s.compress(chars))
print(chars)

