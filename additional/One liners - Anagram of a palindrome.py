s = input()
print(len([c for c in set(s) if s.count(c) % 2 != 0]) <= 1)