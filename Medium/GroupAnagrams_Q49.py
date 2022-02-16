"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
import collections
import unittest
from typing import List


class Solution:
    # Time Complexity: O(nklogk) ; Space complexity: O(nk) where n is the size strs and k is length of each string in strs
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        group_anagrams = {}
        for i in range(0, len(strs)):
            word = "".join(sorted(strs[i]))
            if word in group_anagrams.keys():
                group_anagrams[word].append(strs[i])
            else:
                temp = []
                temp.append(strs[i])
                group_anagrams[word] = temp

        for key in group_anagrams.keys():
            ans.append(group_anagrams[key])

        return ans

    # Time complexity: O(nk) and space complexity: O(nk)
    """
    Intuition

Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

Algorithm

We can transform each string \text{s}s into a character count, \text{count}count, consisting of 26 non-negative integers representing the number of \text{a}a's, \text{b}b's, \text{c}c's, etc. We use these counts as the basis for our hash map.

In Java, the hashable representation of our count will be a string delimited with '#' characters. For example, abbccc will be #1#2#3#0#0#0...#0 where there are 26 entries total. In python, the representation will be a tuple of the counts. For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.
    """
    def groupAnagrams_approach2(self,strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        for key in ans.keys():
            res.append(ans[key])
        return res




class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]),[["eat","tea","ate"],["tan","nat"],["bat"]])

    def test_case2(self):
        self.assertListEqual(self.obj.groupAnagrams([""]),[[""]])

    def test_case3(self):
        self.assertListEqual(self.obj.groupAnagrams(["a"]),[["a"]])

    def test_case1_approach2(self):
        self.assertListEqual(self.obj.groupAnagrams_approach2(["eat","tea","tan","ate","nat","bat"]),[["eat","tea","ate"],["tan","nat"],["bat"]])

    def test_case2_approach2(self):
        self.assertListEqual(self.obj.groupAnagrams_approach2([""]),[[""]])

    def test_case3_approach2(self):
        self.assertListEqual(self.obj.groupAnagrams_approach2(["a"]),[["a"]])