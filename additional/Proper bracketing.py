line = input()
stack = []
for char in line:
    if char in "{[(":
        stack.append(char)
    elif char in ")]}":
        if not stack or abs(ord(char) - ord(stack.pop())) > 2:
            print(False)
            break
else:
    if len(stack) == 0:
        print(True)
    else:
        print(False)
