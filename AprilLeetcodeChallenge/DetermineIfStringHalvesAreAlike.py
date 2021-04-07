"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:

Input: s = "MerryChristmas"
Output: false

Example 4:

Input: s = "AbCdEfGh"
Output: true



Constraints:

    2 <= s.length <= 1000
    s.length is even.
    s consists of uppercase and lowercase letters.


"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length_s=len(s)
        # print(length_s)
        first_half_vowel_count = second_half_vowel_count = 0
        for i in range(0,length_s//2):
            # print(s[i])
            # print("___",s[length_s-1-i])
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                first_half_vowel_count += 1
                # print(first_half_vowel_count)
            if s[length_s-1-i] in ['a','e','i','o','u','A','E','I','O','U']:
                second_half_vowel_count +=1
                # print(second_half_vowel_count)
        if first_half_vowel_count == second_half_vowel_count:
            return True
        else:
            return False

    def halvesAreAlike2(self,s:str) -> bool:
        s, n, cand = s.lower(), len(s), set("aeiou")
        return sum(i in cand for i in s[:n // 2]) == sum(i in cand for i in s[n // 2:])


obj=Solution()
print(obj.halvesAreAlike("AbCdEfGh"))
print(obj.halvesAreAlike("MerryChristmas"))
print(obj.halvesAreAlike2("AbCdEfGh"))

