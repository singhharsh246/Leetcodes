from collections import deque
que_abc = deque(["a", "b", "c"])
print(que_abc)
print(deque(["a", "b", "c"]))

data = deque([{"data" : "a"}, {"data" : "b"}])
print(data)


llist = deque("abcde")
print(llist)
llist.append("f")
print(llist)

llist.pop()
print(llist)

llist.appendleft("z")
print(llist)

llist.popleft()
print(llist)


