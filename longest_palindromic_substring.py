def isPalindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        palindromes=[]
        for i in range(n):
            substr=s[i]
            palindromes.append(s[i])
            for j in range(i+1,n): 
                substr+=s[j]
                if isPalindrome(substr):
                    palindromes.append(substr)
                
        if palindromes!=[]:
            return max(palindromes, key=len)
        else:
            return ''

solve=Solution()
print(solve.longestPalindrome('a'))