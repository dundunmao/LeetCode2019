class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        temp = []
        start = 0
        # 找到有哪些word
        for i in range(1, len(S)):
            if S[i] == ' ' and S[i - 1] != ' ':
                temp.append(S[start: i])
            if S[i - 1] == ' ' and S[i] != ' ':
                start = i
        temp.append(S[start:]) # G 域 to F 域

        for i in range(len(temp)):            
            if temp[i][0] not in vowel:
                temp[i] = temp[i][1:] + temp[i][0]
            temp[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(temp)
