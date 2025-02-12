"""
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

(0,0) -> (2,1) -> (4,2) -> (3,4)

possible first move:
U(x-1,y),d(x+1,y),l(x,y-1),r(x,y+1)
orthogonal move:


resultant moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
start = (0,0)

queue =

(0,0)
(2,1),1;(1,2),1


target_pos

resultant moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
if start == target:
	return 0

visited = set()
visisted.add(start)
q = deque([(start[0],satrt[1],0)])

while !(q.empty):
	x,y,steps = q.popleft()

  for dx,dy in resultant_moves:
  	nx = x+dx
    ny = y+dy


    if (nx,ny) == target:
    	return steps+1


    if (nx,ny) not in visited:
    	visited.add((nx,ny))
      queue.append((nx,ny,steps+1))


===========================================================================

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
prices = [7,1,5,3,6,4]
Output: 7

7,1
1,5 = 4
5,3 =
3,6 = 3

1 -> 5 = 4
3 -> 6 = 3
7

[1,2,3,4,5] => 4


max_profit = 0

for i in range(0,n-1):
	if price[i+1] > price[i]:
  	max_profit += (price[i+1]-price[i])

return max_profit















"""