from collections import deque

def reverse_first(queue, k):
    if k < 0 or k > len(queue):
        return queue

    stack = []

    # Step 1: Remove the first k items and push them onto the stack
    for i in range(k):
        stack.append(queue.popleft())

    # Step 2: Add the items back in reversed order
    while stack:
        queue.append(stack.pop())

    # Step 3: Move the remaining items behind the reversed items
    for i in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue

##example
from collections import deque

queue1 = deque([10, 20, 30, 40, 50])
print(reverse_first(queue1, 3))


queue2 = deque([1, 2, 3, 4])
print(reverse_first(queue2, 2))

queue3 = deque([1, 2, 3])
print(reverse_first(queue3, 1))


queue4 = deque([1, 2, 3])
print(reverse_first(queue4, 0))


