class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for i in stones:
            if i in jewels: 
                    jewels_count += 1
        return jewels_count