def decimat_to_binary(num):
    temp_num=num
    binary = ""
    while temp_num/2 != 0:
        d = temp_num%2
        d = str(d)
        binary = d + binary
        temp_num=temp_num//2
    return binary

def check_for_consecutive1s(s:str):
    for i in range(len(s)-1):
        ch1 = s[i]
        ch2 = s[i+1]
        if ch1 == '1' and ch2 == '1':
            return True
    return False

num = 2
count=0
for i in range(num+1):
    binary = decimat_to_binary(i)
    if check_for_consecutive1s(binary):
        count+=1

print(num+1 - count)
# print("binary=",decimat_to_binary(3))