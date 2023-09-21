def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()  # 用於儲存當前子字串中出現過的字符
    max_length = 0  # 記錄最長子字串的長度
    left = 0  # 當前子字串的左邊界

    for right in range(len(s)):
        while s[right] in char_set:  # 如果當前字符已經在子字串中出現過
            char_set.remove(s[left])  # 移除左邊界字符，並向右移動左邊界
            left += 1
        char_set.add(s[right])  # 將當前字符添加到子字串中
        max_length = max(max_length, right - left + 1)  # 更新最長子字串的長度

    return max_length

s = "asdadddada"
result = Solution().lengthOfLongestSubstring(s)
print(result)
