class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        size = len(word)
        if size <= 1:
            return True

        for i in range(1, size):
            if word[i - 1].islower() and word[i].isupper():
                return False
            elif word[i - 1].isupper():
                if i != 1 and word[i].islower():
                    return False
        return True
