"""
There is a N player tournament. Players have rank 1 to N and each player has a unique rank. Assume that the best player always wins.

The tournament is a knockout tournament. This means if we have 8 players [a b c d e f g h] with their ranks [1 2 3 4 5 6 7 8], the tournament will look like this:
1st round: [a b] [c d] [e f] [g h]
2nd round: [a c] [e g]

3rd round: [a e]
champion : [a]

We are calling [a b c d e f g h] or [1 2 3 4 5 6 7 8] a "draw" where in the 1st round: first two players meet in the first match, the next two players meet in the second match and so on.

In the 2nd round: in the first match, the winner of the first match of the 1st round and the winner of the second match of the 1st round will play together. And similarly in the second match, the winner of the third match of the 1st round and the winner of the fourth match of 1st round will play together.

In short: given a draw, if we don't change the order of the players, players will meet in their order on the draw, and of course the winner moves to the next round. The tournament ends when there is only a single player remaining.

A draw is a valid draw when in each round, the best (based on rank) player plays with the worst player, the second best player plays with the second worst player and so on.

Problem:
Given a draw, find out whether it is a valid draw.

Rank of players [3, 2, 1, 4] == 1
[3 2] [1 4]

[2 1] == n =2 , sum = 3

[1] === n=1 , the lowest (1)
N 1 == n+1
N-1 2
N-2 3


n>=2, 1..n, n%2==0
Def is_valid_draw(ranks): [1, 6, 2, 5, 3, 4]
n = len(ranks)
Possible_pairs = []
Valid_input = is_valid_input(n)
If valid_input
For i in range(0,n,2):
	Pair = [ranks[i],ranks[i+1]]
	possible_pairs.append(pair)
While len(possible_pairs) > 1:
	Next_round_pairs = []
	New_pair = []
For pair in possible_pairs:
	Pair_rank_sum = sum(pair)
	If pair_rank_sum != n+1:
		Return False
	Else:
		If len(new_pair) != 2:
			new_Pair.append(min(pair[0],pair[1]))
		Elif len(new_pair) ==2:
			next_round_pairs.append(new_pair)
			New_pair = []
Possible_pairs = next_round_pairs
N = 2*len(possible_pairs)

Return True



Round 1:
'''
We have a service that streams sequentially-numbered work items to a cluster of workers.
The workers receive an item, process it, and upon success, acknowledge (ack) the item's sequence number to mark it complete.

Because all of the servers and the datacenter are unreliable, we need to store the workers' progress.
To do this, the workers send their acks to an accounting server.
The accounting server is periodically asked for the lowest sequence number that has not been acknowledged (the "lowest unacked"), and this number is stored reliably by another system.

getLowestUnacked():
 * returns the lowest unacknowledged sequence number


acknowledge(sequenceNumber):
 * worker server calls this function when it completes a work item

start(lowestUnacknowledged):
 * called exactly once when the accounting server starts
 * argument is the lowest un-acknowledged sequence number


12,
20,14,16,12,
unacknowledged: 12,
acknowledged(sorted): 12,13,14,15,16,17,19


len = 6
a = 12
d = 1

max = 17
sum = 87


'''
unacknowledged_val: int, acknowledged: List[int]
def getLowestUnacked():
  val = unacknowledged_val
  idx = find_unacknowledged_val(val,acknowledged) # binary search on acknowledged
  if idx == -1:
    unacknowledged_val = val
  else:
    while idx != -1: #
      val += 1
      idx = find_unacknowledged_val(val,acknowledged)
    unacknowledged_val = val
  return unacknowledged_val

def acknowledge(sequenceNumber: int):
  acknowledge.append(unacknowledged_val)
  acknowledge = sorted(acknowledge)

def start(lowestUnacknowledged: int):
    acknowledged = []
    unacknowledged_val = lowestUnacknowledged














"""