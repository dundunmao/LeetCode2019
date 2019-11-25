class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        le = len(words)
        i = 0
        while i < le:
            k,l = 0,0
            # i是此行的起点，k是此行包含的word的个数
            while i+k< le and l + len(words[i+k]) + 1<= maxWidth: #l是len_so_far,如果该word加进去长度不超
                l += len(words[i+k]) +1  #就把该word加进去
                k += 1     #讨论下一个word
            temp = words[i]  #temp代表该行，从word_i开始加，因为只有i前面不需要空格，所以word_i是单独加的
            if k > 0:
                # （maxWidth - l）是需要填入的空格数，
                # (maxWidth - l) / (k - 1) 是空格数跟当前行单词数的比。也就是分配到每个词之间的空格的基数
                # (maxWidth - l) % (k - 1) 是空格数跟当前行单词数的mod，是多余出来的空格，需要依次从头开始填
                ave = (maxWidth - l) / (k - 1)
                mod = (maxWidth - l) % (k - 1)
                for j in range(0,k-1):  #对于加入该行的word
                    if i + k >= le:   #如果是最后一行了，每个单词之间只有一个空格
                        temp += " "
                    else:            #如果不是最后一行，
                        if j < mod:
                            temp +=' '*(ave+1)
                        else:
                            temp += ' '*(ave)
                    temp += words[i + j + 1]
            temp += ' '* (maxWidth - len(temp))
            res.append(temp)
            # if k == 0:
            #     return res
            i = i + k + 1
        return res

class Solution1(object):
    def fullJustify(self, words, maxWidth):
        res = []  #最后结果
        cur = []  #每行的word
        num_of_letters = 0  #所以letter的长度，不算空格的
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:  # 一旦该行的word满了，就开始考虑空格怎么加了
                for i in range(maxWidth - num_of_letters):     # maxWidth - num_of_letters是需要填的空格总数
                    # i%(len(cur)-1)，i从0遍历到空格总数，相当于把空格在前n-1个word后一遍一遍的加，直到加没了
                    # 也处理了只有一个单词的情况，i%1永远等于0，所以永远在第一个单词后加空格。
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))   #把该行填入res里
                cur, num_of_letters = [], 0 #为下一行做准备
            cur += [w]         #在该行继续加word，cur表示该行的所有word
            num_of_letters += len(w)   #num_of_letters只算word加起来的总长度，不考虑空格
        return res + [' '.join(cur).ljust(maxWidth)]  #[' '.join(cur).ljust(maxWidth)]是最后一行的处理


if __name__ == '__main__':
    s = Solution1()

    # words = ['a','b','c']
    # l = 1
    # print s.fullJustify(words,l)
    #
    #
    # words = ['']
    # l = 0
    # print s.fullJustify(words,l)

    words = ["This", "is", "an", "example", "of", "text", "justificat",'adadad']
    l = 16
    print s.fullJustify(words,l)


    # [
    #     "This    is    an",
    #     "example  of text",
    #     "justification.  "
    # ]
