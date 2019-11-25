class Solution:
    def isPossible(self, nums) -> bool:
        hash_to_freq = {}
        wait_next_hash = {} # 等待的数
        for ele in nums:
            hash_to_freq[ele] = hash_to_freq.get(ele, 0) + 1

        for ele in nums:
            # 已经加入前面的group了
            if hash_to_freq[ele] == 0:
                continue
            # 有group在等这个ele,
            if ele in wait_next_hash and wait_next_hash[ele] > 0:

                # 在等的这个数，数量减一个
                wait_next_hash[ele] -= 1
                # 此数加入group了
                hash_to_freq[ele] -= 1

                # 开始等这个数的下一个数
                wait_next_hash[ele + 1] = wait_next_hash.get(ele + 1, 0) + 1

            # 如果group没等他，自己新开个group，如果自己往下找不到3个，就False
            elif hash_to_freq[ele] > 0 and \
                    ele + 1 in hash_to_freq and hash_to_freq[ele + 1] > 0 and \
                    ele + 2 in hash_to_freq and hash_to_freq[ele + 2] > 0:
                # 从ele往下数三个，都用掉
                hash_to_freq[ele] -= 1
                hash_to_freq[ele + 1] -= 1
                hash_to_freq[ele + 2] -= 1
                # 等待第四个
                wait_next_hash[ele + 3] = wait_next_hash.get(ele + 3, 0) + 1
            else:
                return False
        return True
