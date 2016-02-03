def substring(text, pattern):
    """Determines the first index where the pattern occurs in a given text

    :param text: The text to query
    :param pattern: The pattern to match in text
    :return: The first index where the pattern matched, otherwise -1 if no pattern was found
    """

    N = len(text)
    M = len(pattern)
    
    if M > N:
        return False

    #Build skip table
    skiptable = {letter: i for i, letter in enumerate(pattern)}

    skip = 0
    i = 0
    
    while i <= N - M:
        skip = 0
        for j, patternLetter in reversed(list(enumerate(pattern))):
            if patternLetter != text[i+j]:
                if text[i+j] not in skiptable:
                    skip = j+1
                else:
                    skip = max(1, j - skiptable[text[i+j]])
                break

        if skip == 0:
            return i+j

        i += skip
    
    return -1

print substring("abedabc","abc")
print substring("carpet", "car")
print substring("aneedleinahaystack","needle")
print substring("java", "ada")