def isAnagram(self, s: str, t: str) -> bool:

#Check for length of characters first
    if len(s) != len(t):
        return False

    hashmapS = {}
    hashmapT = {}
    for n in range(len(s)):

#this will add the key(charater) to the dictionary with its key
#  as the 1 incremented by 1 each time it occurrs and if it doesnt occur add 0
        hashmapS[s[n]] = 1 + hashmapS.get(s[n], 0)
        hashmapT[t[n]] = 1 + hashmapT.get(t[n], 0)

    for c in hashmapS:
        if hashmapS[c] != hashmapT.get(c, 0):
            return False
    return True
    
