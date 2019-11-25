class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary_hash = {}
        for ele in dictionary:
            abbr = self.tran_to_abbr(ele)
            if not abbr in self.dictionary_hash:
                self.dictionary_hash[abbr] = [ele]
            elif abbr in self.dictionary_hash and not ele in self.dictionary_hash[abbr]:
                self.dictionary_hash[abbr].append(ele)

    def isUnique(self, word):
        """
    :type word: str
    :rtype: bool
    """

        abbr = self.tran_to_abbr(word)
        if not abbr in self.dictionary_hash:
            return True
        else:
            if len(self.dictionary_hash[abbr]) == 1 and word in self.dictionary_hash[abbr]:
                return True
            else:
                return False

    def tran_to_abbr(self, word):
        ele_length = len(word)
        if ele_length < 3:
            return word
        abbr = word[0] + str(ele_length - 2) + word[-1]
        return abbr


# Your ValidWordAbbr object will be instantiated and called as such:
# dictionary = ["deer","door","cake","card"]
# obj = ValidWordAbbr(dictionary)
# check = ["dear","cart","cane","make"]
# for word in check:
#     print(obj.isUnique(word))
print("------")
dictionary = ["deer","deer"]
obj = ValidWordAbbr(dictionary)
check = ["deer"]
for word in check:
    print(obj.isUnique(word))
