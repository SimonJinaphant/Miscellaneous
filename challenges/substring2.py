prime = 3

def myord(s):
    #Purely for ease in computation and manual testing, use normal ord instead
    return ord(s)-ord('a')+1

'''
    Returns the first index of pattern inside the text
    otherwise -1 if the pattern doesn't exist
'''
def substring(text, pattern):
    n = len(text)
    m = len(pattern)
    
    #Test for substrings using hashes
    patternHash = computeHash(pattern)
    subtextHash = computeHash(text[:len(pattern)])

    for i in xrange(n - m):
        if patternHash == subtextHash and pattern == text[i:i+m]:
            return i

        #The current hash already has majority of the new hash calculation done
        #So only need to make small calcuation
        subtextHash = recomputeHash(text, i, i+m, subtextHash, m)
    
    #Still need to check the last recomputed hash
    return n-m if (patternHash == subtextHash and pattern == text[n-m:]) else -1

'''
    Compute a hash for the given string
'''
def computeHash(text):
    hash = 0
    for i, character in enumerate(text):
        hash += myord(character) * (prime**i)

    return hash


'''
    Update a hash to its new value without having to recompute most
    of the original hash all over again
'''
def recomputeHash(subtext, oldIndex, newIndex, oldHash, patternLength):
    oldHash -= myord(subtext[oldIndex])
    oldHash /= prime    
    newHash = oldHash + myord(subtext[newIndex]) * (prime**(patternLength-1))

    return newHash

print substring("abedabc", "abc")
print substring("carpet", "arp")
print substring("noodleandneedleinastack","needle")
print substring("java", "ada")
print substring("snowwy","snow")
