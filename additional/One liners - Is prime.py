s = input()
print(all(int(s) > 1 and int(s) % d != 0 for d in range(2, int(s))))
