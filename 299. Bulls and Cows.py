class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res_a = 0
        res_b = 0
        freq_of_unmatched_char_in_secret = [0] * 256
        freq_of_unmatched_char_in_guess = [0] * 256
        # 同步遍历两个str
        for i in range(len(guess)):
            secret_char = ord(secret[i])
            guess_char = ord(guess[i])
            # 如果一模一样，直接加一个A
            if secret_char == guess_char:
                res_a += 1
            else:
                # 如果guess跟之前的secret(hash) match上了，加一个B，之前的secret(hash)减一个
                if freq_of_unmatched_char_in_secret[guess_char] > 0:
                    res_b += 1
                    freq_of_unmatched_char_in_secret[guess_char] -= 1
                else:
                    freq_of_unmatched_char_in_guess[guess_char] += 1
                # 如果secret跟之前的guess(hash) match上了，加一个B，之前的guess(hash)减一个
                if freq_of_unmatched_char_in_guess[secret_char] > 0:
                    res_b += 1
                    freq_of_unmatched_char_in_guess[secret_char] -= 1
                else:
                    freq_of_unmatched_char_in_secret[secret_char] += 1

        return str(res_a) + 'A' + str(res_b) + 'B'


class Solution1:
    def getHint(self, secret: str, guess: str) -> str:
        char_to_index_hash = {}
        for i in range(len(secret)):
            if secret[i] in char_to_index_hash:
                char_to_index_hash[secret[i]].add(i)
            else:
                char_to_index_hash[secret[i]] = set([i])
        res_a = 0
        res_b = 0
        for j in range(len(guess)):
            if guess[j] in char_to_index_hash:
                if j in char_to_index_hash[guess[j]]:
                    res_a += 1
                    char_to_index_hash[guess[j]].remove(j)
                else:
                    res_b += 1
        return str(res_a) + 'A' + str(res_b) + 'B'

s = Solution()
secret = "1807"
guess =  "7810"
print(s.getHint(secret, guess))
