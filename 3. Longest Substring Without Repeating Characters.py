class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}

        if len(s)<=1:
            return len(s)
        for i in range(len(s)+1):
            longest = ""
            for j in range(i+1,len(s)+1):
                print("s[i:j]:%s"%s[i:j])
                print(i)
                print(j)
                print("j:%s"%s[j-1])
                try:
                    s[j]
                except:
                    j = len(s)
                if s[j-1] not in longest:
                    longest=s[i:j]
                    dic[len(longest)] = longest
                    print("longest if:%s"%longest)
                    print(dic)
                    print("_____")
                else:
                    dic[len(longest)] = longest
                    longest=s[j-1]
                    print("longest else %s"%longest)
                    print(dic)
                    print("_____")
                    break

        return list(dic.keys())[-1]
test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))

