# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        count = 0
        for c1, c2 in zip(word, 'acckzz'):
            if c1 == c2:
                count += 1
        return count
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            count_hash = {}
            for w1 in wordlist:
                for w2 in wordlist:
                    if self.match(w1, w2) == 0:
                        if w1 in count_hash:
                            count_hash[w1] += 1
                        else:
                            count_hash[w1] = 1
            if len(count_hash) > 0:
                sort_word_count = sorted(count_hash.items(), key = lambda x:x[1])
                cur = sort_word_count[0][0]
                print(cur)
            else:
                cur = wordlist[0]
            guess_count = master.guess(cur)
            word_list_new = []
            for w in wordlist:
                if self.match(w, cur) == guess_count:
                    word_list_new.append(w)
            wordlist =  word_list_new

    def match(self, w1, w2):
        count = 0
        for c1, c2 in zip(w1, w2):
            if c1 == c2:
                count += 1
        return count

s = Solution()
secret = "acckzz"
wordlist = ["ccbazz","eiowzz","acckzz", "abcczz"]
# secret = "hbaczn"
# wordlist = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]
# 10

master = Master()
print(s.findSecretWord(wordlist, master))
