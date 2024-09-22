class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    def gcd(self, A, B):
        r = A % B
        if r==0:
            return B
        return self.gcd(B,r)