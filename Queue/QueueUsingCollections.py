from collections import deque

customQ = deque(maxlen=3)
print(customQ)
customQ.append(1)
customQ.append(2)
customQ.append(3)
print(customQ)
customQ.popleft()
print(customQ)
customQ.clear()
print(customQ)
