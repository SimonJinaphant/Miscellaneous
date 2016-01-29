def substring(text, pattern):
    N = len(text)
    M = len(pattern)
    skip = 0

    #Build skip table
    skiptable = {}
    for i, letter in enumerate(pattern):
        if letter not in skiptable:
            skiptable[letter] = i
        else:
            skiptable[letter] = i

    i = 0
    while i <= N-M:
        skip = 0
        for j, patternLetter in reversed(list(enumerate(pattern))):
            if patternLetter != text[i+j]:
                if text[i+j] not in skiptable:
                    skip = 1
                else:
                    skip = max(1, j - skiptable[text[i+j]])
                break

        if skip == 0:
            return True

        i += skip
    
    return False


print substring("carpet", "car")
print substring("aneedleinahaystack","needle")
print substring("java", "ada")
