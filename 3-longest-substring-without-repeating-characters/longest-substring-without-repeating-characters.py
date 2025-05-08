class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        result = set()
        len_longest_substring = 0
        for right_ptr in range(len(s)):
            # window size shrinks, as duplicate found, remove the value from the set
            while s[right_ptr] in result:
                result.remove(s[left_ptr])
                # move the left ptr forward
                left_ptr += 1
            # add to the result set
            result.add(s[right_ptr])
            len_longest_substring = max(len_longest_substring, right_ptr - left_ptr + 1)
        #print(f"longest substring found from max {len_longest_substring}")
        return len_longest_substring
