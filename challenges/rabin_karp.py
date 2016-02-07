import unittest


def substring(text, pattern):
    """
    Determines the first index of the given pattern in text

    :param text: The string to be searched on
    :param pattern: The string to match
    :return: The first index of a matched pattern, otherwise None if pattern was not found in text
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

    def recompute_hash(old_index, new_index, old_hash):
        """
        Updates a hash to its new value without recomputing most
        of the original hash all over again

        :param old_index: The index of the first letter in text
        :param new_index: The index of the next letter
        :param oldHash: The previous integer hash
        :return: A new integer hash
        """
        old_hash -= ord(text[old_index])
        old_hash /= prime
        return old_hash + ord(text[new_index]) * (prime ** (m - 1))

    #Compute the hash for the pattern and the first 3 letters of the text
    hashed_pattern = compute_hash(pattern)
    hashed_subtext = compute_hash(text[:len(pattern)])

    for i in xrange(n - m):
        if hashed_pattern == hashed_subtext and pattern == text[i:i+m]:
            return i

        #The current hash already has majority of the new hash calculation done
        #So only need to make small calcuation
        hashed_subtext = recompute_hash(i, i+m, hashed_subtext)
    
    #Still need to check the last recomputed hash
    return n - m if (hashed_pattern == hashed_subtext and pattern == text[n-m:]) else None


class TestRabinKarp(unittest.TestCase):

    def test_ends(self):
        self.assertEqual(substring("abedabc","abc"), 4)
        self.assertEqual(substring("carpet", "car"), 0)

    def test_normal(self):
        self.assertEqual(substring("aneedleinahaystack", "needle"), 1)

    def test_absent(self):
        self.assertEqual(substring("java", "ada"), None)

if __name__ == "__main__":
    TestRabinKarp.main()