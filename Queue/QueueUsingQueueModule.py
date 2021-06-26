import queue as q

customQ = q.Queue(maxsize=3)
print(customQ.empty())
customQ.put(1)
customQ.put(2)
customQ.put(3)
print(customQ.full())
print(customQ.qsize())
print(customQ.get())
print(customQ.qsize())
