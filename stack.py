stack = []


stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after push:", stack)


removed = stack.pop()
print("Popped element:", removed)

print("Top element:", stack[-1])

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")