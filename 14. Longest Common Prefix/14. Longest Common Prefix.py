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
        first_element = strs[0]  
        for i in strs[1:]:
            prefix = ""
            if i=="" or first_element=="": return ""
            if len(first_element)>len(i):
                small_len = len(i)
            else: small_len = len(first_element)
            for j in range(small_len):
                if first_element[:j+1] ==i[:j+1]:
                    prefix = first_element[:j+1]
                else: break
            if prefix=="": return ""
            if prefix_arr == [""]:
                prefix_arr = [prefix]
            else:
                if len(prefix)<len(prefix_arr[0]):
                    prefix_arr = [prefix]
                else: pass
        return prefix_arr[0] 
test = Solution()

print(test.longestCommonPrefix(["aa","aa","c"]))
