class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for letter in list(set(s)):
                if s.count(letter) != t.count(letter):
                    return False
            return True
