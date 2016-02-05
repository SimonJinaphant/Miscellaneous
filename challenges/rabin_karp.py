def substring(text, pattern):
    """
    Determines the first index of the given pattern in text

    :param text: The string to be searched on
    :param pattern: The string to match
    :return: The first index of a matched pattern, otherwise -1 if pattern was not found in text
    """
    prime = 101

    n = len(text)
    m = len(pattern)

    def compute_hash(unhashed_text):
        """
        Computes an integer hash based on the given

        :param unhashed_text: The string to be hashed
        :return: A hash of the given string
        """
        hashed_text = 0
        for i, character in enumerate(unhashed_text):
            hashed_text += ord(character) * (prime**i)

        return hashed_text

    def recompute_hash(oldIndex, newIndex, oldHash):
        """
        Updates a hash to its new value without recomputing most
        of the original hash all over again

        :param oldIndex: The index of the first letter in text
        :param newIndex: The index of the next letter
        :param oldHash: The previous integer hash
        :return: A new integer hash
        """
        oldHash -= ord(text[oldIndex])
        oldHash /= prime
        newHash = oldHash + ord(text[newIndex]) * (prime**(m-1))

        return newHash
    
    #Compute the hash for the pattern and the first 3 letters of the text
    patternHash = compute_hash(pattern)
    subtextHash = compute_hash(text[:len(pattern)])

    for i in xrange(n - m):
        if patternHash == subtextHash and pattern == text[i:i+m]:
            return i

        #The current hash already has majority of the new hash calculation done
        #So only need to make small calcuation
        subtextHash = recompute_hash(i, i+m, subtextHash)
    
    #Still need to check the last recomputed hash
    return n - m if (patternHash == subtextHash and pattern == text[n-m:]) else -1




print substring("abedabc", "abc")
print substring("carpet", "arp")
print substring("noodleandneedleinastack","needle")
print substring("java", "ada")
print substring("snowwy","snow")