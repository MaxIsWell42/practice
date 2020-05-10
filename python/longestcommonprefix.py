class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # Edge cases
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        temp = strs[0]
        # start from 2nd word in list
        x = 1
        while (x < len(strs)):
            # Only check the length of the smallest string because it can't have any more in common after that
            temp = comp(temp, strs[x][:len(temp)])
            x = x + 1
        return temp
    

def comp(str1, str2):
    # Returns the largest common prefix
    # Find the smallest element in both strings
    length = min(len(str1), len(str2))
    for x in range(length):
        # Keep copying until the strings don't match, and return it up until it didn't
        if str1[x] != str2[x]:
            return str1[:x]
    # Return the smallest string
    return str1[:length]
        