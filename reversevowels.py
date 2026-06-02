class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in "aeiouAEIOU":
                vowels.append(i)
        result = []
        for i in s:
            if i not in "aeiouAEIOU":
                result.append(i)
            else:
                result.append(vowels.pop())
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    
    s = str(input("Enter string:"))
    result = sol.reverseVowels(s)
    
    print("Output:", result)