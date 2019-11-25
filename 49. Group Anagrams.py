class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for ele in strs:
            temp = sorted(ele)
            temp = tuple(temp)
            if temp in hash:
                hash[temp].append(ele)
            else:
                hash[temp] = [ele]
        return [value for value in hash.values()]


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_to_group = {}
        for ele in strs:
            seria = self.serialize_string(ele)
            if seria in word_to_group:
                word_to_group[seria].append(ele)
            else:
                word_to_group[seria] = [ele]
        return [ele for ele in word_to_group.values()]

    def serialize_string(self, strs):
        char_to_freq = [None for i in range(26)]
        for char in strs:
            if char_to_freq[ord(char) - 97]:
                char_to_freq[ord(char) - 97] += 1
            else:
                char_to_freq[ord(char) - 97] = 1
        res = []
        for i in range(len(char_to_freq)):
            if char_to_freq[i]:
                res.append(chr(i + 97))
                res.append(str(char_to_freq[i]))
        return ''.join(res)



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating","aware","outfield","marlborough","guardrooms","roast","wattage","shortcuts","confidential","reprint","foxtrot","dispossession","floodgate","unfriendliest","semimonthlies","dwellers","walkways","wastrels","dippers","engrossing","undertakings","unforeseen","oscilloscopes","pioneers","geller","neglects","cultivates","mantegna","elicit","couriered","shielded","shrew","heartening","lucks","teammates","jewishness","documentaries","subliming","sultan","redo","doer","recopy","flippancy","rothko","conductor","e","carolingian","outmanoeuvres","gewgaw","saki","sarah","snooping","hakka","highness","mewling","spender","blockhead","detonated","cognac","congaing","prissy","loathes","bluebell","involuntary","aping","sadly","jiving","buffalo","chided"]
    s = Solution1()
    print(s.groupAnagrams(strs))
