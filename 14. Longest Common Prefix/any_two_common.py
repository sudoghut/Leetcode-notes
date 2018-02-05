class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<=1:
            if strs == []: return ""
            return strs[0]
        prefix_arr = [""]
        count = 0
        for i in strs:
            count+=1
            for j in strs[count:]:
                current_prefix = ""
                loop_num = 0
                if len(i)>len(j):
                    loop_num = len(j)
                else:
                    loop_num = len(i)
                for k in range(loop_num):
                    if i[k]==j[k]:
                        current_prefix+=i[k]
                if len(current_prefix)> len(prefix_arr[0]):
                    prefix_arr = [current_prefix]
                elif len(current_prefix)== len(prefix_arr[0]):
                    prefix_arr.append(current_prefix)
                else: pass
        return prefix_arr[0]
test = Solution()
#print(test.longestCommonPrefix(["abdcd","abd","abcx","ccccccx","ccccccccx","ddddddx","dddddddddddddddb"]))
print(test.longestCommonPrefix(["a","a","b"]))
