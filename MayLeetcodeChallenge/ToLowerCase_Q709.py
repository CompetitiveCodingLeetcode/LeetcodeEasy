class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s=""
        for ch in s:
            if 65<=ord(ch)<=90:
                # ord -> integer representation of character |  chr -> character representation of integer
                new_s+=chr(ord(ch)+32)
            else:
                new_s+=ch
        return new_s

obj=Solution()
print(obj.toLowerCase("heLLo"))