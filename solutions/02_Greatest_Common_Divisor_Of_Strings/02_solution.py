class Solution:
       def gcd(self,str1, str2):
        len1, len2 = len(str1), len(str2)
        print("length 1:",len1)
        print("length 2:",len2)
        def isDivisible(length):
            if len1 % length != 0 or len2 % length != 0:
                return False
            maxR1, maxR2 = len1 // length, len2 //length
            
            return str1[:length] * maxR1 == str1 and str1[:length] * maxR2 == str2

        for i in range(min(len1, len2), 0, -1):
            if isDivisible(i):
                return str1[:i]
        return ""

#Divisible means a number goes evenly (without reminder) into a number
   
s = Solution()
#s.gcd("ABABAB","ABAB")
print(s.gcd("ABABABABABABABABABABABAB", "ABABABABABAB"))
print(s.gcd("LEET", "CODE"))

