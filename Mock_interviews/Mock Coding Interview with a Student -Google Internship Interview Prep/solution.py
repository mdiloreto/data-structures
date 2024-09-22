class InneficientSolution: 
    """This is an inneficient solution. 
        O(n^2)
    """
    def re_dups(self, s):
        for i in range(len(s)-1): 
            if s[i] == s[i+1]:
                o = s.replace(s[i], "", 2)    
                return self.re_dups(o)
        return s
    
class Solution: 
    """
    "abbaca"
       ^
    list = [a,b,b ]    
    
    This solution is more efficient that the previous one. 
    O(n)
    """
    def re_dups(self, s):
        list = []
        for i in s:
            if len(list) and i == list[-1]:
                list.pop()
            else:
                list.append(i)
                
        return ''.join(list)    
    
# sol = Solution()
# s = "abbaxccwzx"
# print(sol.re_dups(s))

class FollowUpSolution:
    """
    What if instead of adjacent pairs (2) you would remove *k*-wise duplicates. 
        "deeedbbcccbdaa"
                    ^
    list = [aa]    
    k = x    
    """
    def re_dups(self, s, k):
        list = []
        for i in s:
            if len(list)>=k-1:
                eq = True
                j = 1
                while eq == True and j < k:
                    if i != list[-j]:
                        eq = False
                    j += 1
                if eq == True:
                    del list[-(k-1):]
                else: 
                    list.append(i)
            else:
                list.append(i)
                
        return ''.join(list)    

sol = FollowUpSolution()
s = "deeedbbcccbdaa"
k = 3
print(sol.re_dups(s,k))