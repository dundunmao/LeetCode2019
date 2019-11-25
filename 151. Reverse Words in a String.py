# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
class Solution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # array = s.strip().split()[::-1]
        # if s == '' or s == ' ':
        #     return ''
        s = s.strip()  # 去掉前后的空格
        if s == '':
            return ''
        array = s.split()  # 用空格把它分成array
        array.reverse()
        return ' '.join(array)

#     推荐
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        i, j = 0, 0
        temp = []
        while j < len(s):
            while i < len(s) and s[i] == ' ':  # i指向第一个不是空格的
                i += 1
            j = i
            while j < len(s) and s[j] != ' ':  # j指向接下来的第一个空格
                j += 1
            if i == j:
                break
            temp.append(self.reverse(s[i:j]))
            i = j
        ans = ' '.join(temp)
        return self.reverse(ans)

    def reverse(self, s):
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
if __name__ == '__main__':
    s = Solution()
    a = "a "  #'a'
    print s.reverseWords(a)
    a = "the sky is blue"  #"blue is sky the".
    print s.reverseWords(a)
