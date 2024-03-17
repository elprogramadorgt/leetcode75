# Input: s = "the sky is blue"
# Output: "blue is sky the"



from collections import deque

    # de.append(4)

def reverseWords(s: str) -> str:
    # return " ".join( s.split()[::-1])
    queue = deque()
    start = 0
    i = 0
    while i < len(s):
        if s[i] != " ":
            start = i

            while i < len(s) and s[i] != " ":
                i += 1
            queue.appendleft(s[start:i])

        i += 1
    return  " ".join(queue)




s = "   the   sky    is    blue    "

print(reverseWords(s))





