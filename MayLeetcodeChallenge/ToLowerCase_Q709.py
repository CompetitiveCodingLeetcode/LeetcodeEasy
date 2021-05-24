import time

class Solution:
    def toLowerCase(self, s: str) -> str:
        start=time.time()
        new_s=""
        # new_s= "".join(chr(ord(ch)+32) if 'A'<=ch<='Z' else ch for ch in s)
        for ch in s:
            if 65<=ord(ch)<=90:
                # ord -> integer representation of character |  chr -> character representation of integer
                new_s+=chr(ord(ch)+32)
            else:
                new_s+=ch
        end=time.time()
        print("time taken=",end-start)
        return new_s

obj=Solution()

# 7.486343383789062e-05 ---- commented approach time
# 6.413459777832031e-05 --- current approach time

print(obj.toLowerCase("heLLovkzsfbjsbegrjsgbsjdbjabfbglsdbvljsgenfkKJSBRGRNWGKSBVJADBVLBAAGKRNGJDBflrnsbjvbgslgbA"))