"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).


Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.


Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.


Follow up: What if the number of hits per second could be huge? Does your design scale?

APPROACH:
Approach #1: Using Queue
Intuition

A key observation here is that all the timestamps that we will encounter are going to be in increasing order. Also as the timestamps' value increases we have to ignore the timestamps that occurred previously (having a difference of 300 or more with the latest timestamp). This is the case of considering the elements in the FIFO manner (First in first out) which is best solved by using the "queue" data structure.

Algorithm

We will add each timestamp to the queue in the hit method and will remove all the timestamps with difference greater than or equal to 300 from the queue inside getHits. The answer returned from the getHits method is then simply the size of the queue.

Below is the implementation of this approach.

Complexity Analysis

Time Complexity

hit - Since inserting a value in the queue takes place in O(1)O(1) time, hence hit method works in O(1)O(1).

getHits - Assuming a total of nn values present in the queue at a time and the total number of timestamps encountered throughout is NN. In the worst case scenario, we might end up removing all the entries from the queue in getHits method if the difference in timestamp is greater than or equal to 300. Hence in the worst case, a "single" call to the getHits method can take O(n)O(n) time. However, we must notice that each timestamp is processed only twice (first while adding the timestamp in the queue in hit method and second while removing the timestamp from the queue in the getHits method). Hence if the total number of timestamps encountered throughout is NN, the overall time taken by getHits method is O(N)O(N). This results in an amortized time complexity of O(1)O(1) for a single call to getHits method.

Space Complexity: Considering the total timestamps encountered throughout to be NN, the queue can have upto NN elements, hence overall space complexity of this approach is O(N)O(N).

Approach #2: Using Deque with Pairs
Consider the follow up, where we have multiple hits arriving at the "same" timestamps. We can optimize Approach 1 even further. In this approach, we'll not only keep the timestamps but will also keep the count of the timestamps as well. For example, if we call hit method 5 times for timestamp = 1, the queue in case of Approach 1 will look like [1, 1, 1, 1, 1]. This will lead to 5 removals in the getHits method when we remove the value 1 from the queue. To avoid this repetitive removals of the same value, in Approach 2, we'll store the value as (1, 5) where the first value 1 is the timestamp and the second value 5 is the count. For this, we'll use the "deque" data structure which allows us to insert and delete values from both the ends of the queue.

Algorithm

The updated algorithm in Approach 2 is as follows.

If we encounter the hit for the same timestamp, instead of appending a new entry in the deque, we simply increment the count of the latest timestamp.

In order to keep the track of total number of elements (for the last 300 seconds), we also use a variable total which we initialize to 0 and keep updating as we add or remove the elements from the queue. We increment the value of total by 1 when hit method is called and we decrement by the value of total by the count of the timestamp that we remove from the queue.

Below is the implementation of this approach.
Complexity Analysis

In the worst case, when there are not many repetitions, the time complexity and space complexity of Approach 2 is the same as Approach 1. However in case we have repetitions (say k repetitions of a particular ith timestamp), the time complexity and space complexities are as follows.

Time Complexity:

hit - O(1).

getHits - If there are a total of nn pairs present in the deque, worst case time complexity can be O(n)O(n). However, by clubbing all the timestamps with same value together, for the ith timestamp with k repetitions, the time complexity is O(1)O(1) as here, instead of removing all those k repetitions, we only remove a single entry from the deque.

Space complexity: If there are a total of NN elements that we encountered throughout, the space complexity is O(N)O(N) (similar to Approach 1). However, in the case of repetitions, the space required for storing those k values O(1).
"""
import collections
import unittest
from collections import deque


class HitCounter:

    def __init__(self):
        # approach0
        # self._hits = {}
        # approach 1,2
        self.deq = collections.deque()
        # approach 2
        self.total = 0

    # approach 0 -- Time complexity O(1), space: O(1)
    def hit(self, timestamp: int) -> None:
        if timestamp in self._hits.keys():
            self._hits[timestamp] += 1
        else:
            self._hits[timestamp] = 1

    # approach 0: time complexity: O(no of items in dict), space complexity: O(n)
    def getHits(self, timestamp: int) -> int:
        count = 0
        for key, val in self._hits.items():
            if 0 <= timestamp - key < 300:
                count += val
        return count

    #approach 1:
    def hit_1(self,timestamp):
        self.deq.append(timestamp)

    def get_hits_1(self,timestamp):
        while self.deq and timestamp-self.deq[0] >= 300:
            self.deq.popleft()
        return len(self.deq)

    # approach 2
    def hit_2(self,timestamp):
        if len(self.deq) == 0 or self.deq[-1][0] != timestamp:
            self.deq.append((timestamp,1))
        else:
            prev_val = self.deq[-1][1]
            self.deq.pop()
            self.deq.append((timestamp,prev_val+1))
        self.total += 1

    def get_hits_2(self,timestamp):
        while len(self.deq) != 0:
            diff = abs(self.deq[0][0] - timestamp)
            if diff >= 300:
                self.total -= self.deq[0][1]
                self.deq.popleft()
            else:
                break
        return self.total


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = HitCounter()

    def test_case1(self):
        self.obj.hit(1)
        self.obj.hit(2)
        self.obj.hit(3)
        self.assertEqual(self.obj.getHits(4),3)
        self.obj.hit(300)
        self.assertEqual(self.obj.getHits(300),4)
        self.assertEqual(self.obj.getHits(301),3)

    def test_case2(self):
        self.obj.hit_1(1)
        self.obj.hit_1(2)
        self.obj.hit_1(3)
        self.assertEqual(self.obj.get_hits_1(4),3)
        self.obj.hit_1(300)
        self.assertEqual(self.obj.get_hits_1(300),4)
        self.assertEqual(self.obj.get_hits_1(301),3)

    def test_case3(self):
        self.obj.hit_2(1)
        self.obj.hit_2(2)
        self.obj.hit_2(3)
        self.assertEqual(self.obj.get_hits_2(4),3)
        self.obj.hit_2(300)
        self.assertEqual(self.obj.get_hits_2(300),4)
        self.assertEqual(self.obj.get_hits_2(301),3)