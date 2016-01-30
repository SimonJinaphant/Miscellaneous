prime = 3

def myord(s):
    return ord(s)-ord('a')+1

def substring(text, pattern):
    n = len(text)
    m = len(pattern)

    patternHash = computeHash(pattern)
    subtextHash = computeHash(text[:len(pattern)])

    for i in xrange(n - m):
        print "Subtext: {0} \t Pattern: {1}".format(subtextHash, patternHash)
        if patternHash == subtextHash and pattern == text[i:i+m]:
            return i

        subtextHash = recomputeHash(text, i, i+m, subtextHash, m)

    
    print "Last subtext " + text[n-m:]

    return n-m if (patternHash == subtextHash and pattern == text[n-m:]) else -1

def computeHash(text):
    hash = 0
    for i, character in enumerate(text):
        hash += myord(character) * (prime**i)

    return hash

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
