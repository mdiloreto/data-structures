class BadSolution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        letters_r = {}
        letters_m = {}
        can_const = False
        for i in ransomNote:
            if i in letters_r:
                letters_r[i] += 1
            else: 
                letters_r[i] = 1
        print(letters_r)
        for i in magazine:
            if i in letters_m:
                letters_m[i] += 1
            else: 
                letters_m[i] = 1
        print(letters_m)
        for i in letters_r: 
            if i in letters_m:
                if letters_m[i] >= letters_r[i]:
                    can_const = True
                else:
                    can_const = False
            else:
                can_const = False
        return can_const

class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        for letter in list(set(ransomNote)):
            if ransomNote.count(letter) > magazine.count(letter): return False
        return True

solve= Solution.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
print(solve)