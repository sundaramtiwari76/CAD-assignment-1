queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue after enqueue:", queue)
removed = queue.pop(0)
print("Dequeued element:", removed)
print("Front element:", queue[0])
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")