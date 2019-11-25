class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hash_files = {}
        for ele in paths:
            ele_list = ele.split(' ')
            path = ele_list[0]
            for i in range(1, len(ele_list)):
                file_name, file_content = ele_list[i].split('(')
                if file_content in hash_files:
                    hash_files[file_content].append(path + '/' + file_name)
                else:
                    hash_files[file_content] = [path + '/' + file_name]

        return [ele for ele in hash_files.values() if len(ele) > 1]
