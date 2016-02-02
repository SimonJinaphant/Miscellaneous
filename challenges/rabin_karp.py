prime = 101

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
    return n - m if (patternHash == subtextHash and pattern == text[n-m:]) else -1

'''
    Compute a hash for the given string
'''
def computeHash(text):
    hash = 0
    for i, character in enumerate(text):
        hash += ord(character) * (prime**i)

    return hash


'''
    Update a hash to its new value without having to recompute most
    of the original hash all over again
'''
def recomputeHash(subtext, oldIndex, newIndex, oldHash, patternLength):
    oldHash -= ord(subtext[oldIndex])
    oldHash /= prime    
    newHash = oldHash + ord(subtext[newIndex]) * (prime**(patternLength-1))

    return newHash

print substring("abedabc", "abc")
print substring("carpet", "arp")
print substring("noodleandneedleinastack","needle")
print substring("java", "ada")
print substring("snowwy","snow")