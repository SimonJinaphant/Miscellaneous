prime = 101


def substring(text, pattern):
    """
    Determines the first index of the given pattern in text

    :param text: The string to be searched on
    :param pattern: The string to match
    :return: The first index of a matched pattern, otherwise -1 if pattern was not found in text
    """
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
    """
    Computes an integer hash based on the given

    :param text: The string to be hashed
    :return: A hash of the given string
    """
    hash = 0
    for i, character in enumerate(text):
        hash += ord(character) * (prime**i)

    return hash


'''

'''
def recomputeHash(subtext, oldIndex, newIndex, oldHash, patternLength):
    """
    Updates a hash to its new value without recomputing most
    of the original hash all over again

    :param subtext: The string which contains the next letter
    :param oldIndex: The index of the first letter in subtext
    :param newIndex: The index of the next letter
    :param oldHash: The previous integer hash
    :param patternLength: The length of the overall pattern
    :return: A new integer hash
    """
    oldHash -= ord(subtext[oldIndex])
    oldHash /= prime    
    newHash = oldHash + ord(subtext[newIndex]) * (prime**(patternLength-1))

    return newHash

print substring("abedabc", "abc")
print substring("carpet", "arp")
print substring("noodleandneedleinastack","needle")
print substring("java", "ada")
print substring("snowwy","snow")