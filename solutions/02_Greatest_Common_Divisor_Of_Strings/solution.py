def gcdOfStrings(str1: str, str2: str) -> str:

    len1, len2 = len(str1), len(str2)

    minVal = min(len1, len2)

    def isDivisible(length):

        if len1 % length != 0 or len2 % length != 0:
            return False

        maxS1, maxS2 = len1 // length, len2 // length

        return str1[:length] * maxS1 == str1 and str2[:length] * maxS2 == str2

    for i in range(minVal, 0, -1):

        if isDivisible(i):
            return str1[:i]

str1 = "ABABAB"
str2 = "ABAB"


print(gcdOfStrings(str1, str2))

str1 = "ABABABAB"
str2 = "ABAB"

print(gcdOfStrings(str1, str2))
