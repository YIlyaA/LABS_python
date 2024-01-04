# Please compute the sum of squares for the given numbers (ex: 1 4 -> 30)
# Exp: 1^2 + 2^2 + 3^2 + 4^2 = 30
s = input()
print(sum([i**2 for i in range(int(s.split()[0]), int(s.split()[1]) + 1)]))