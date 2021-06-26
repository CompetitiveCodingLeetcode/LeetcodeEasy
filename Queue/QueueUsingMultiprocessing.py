from multiprocessing import Queue

customQ = Queue(maxsize=3)
customQ.put(1)
customQ.put(2)
customQ.put(3)
print(customQ.get())
print(customQ)