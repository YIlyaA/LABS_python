# You have to sum all positive even numbers provided on input. (-2 -1 1 2) -> 2
# 1 way:
import re
s = input()
print(sum(int(match.group()) for match in re.finditer(r'-?\b\d+(\.\d+)?\b', s) if float(match.group()) % 2 == 0 and float(match.group()) > 0))

# 2 way:
s = input()
print(sum(map(lambda x: int(x) if int(x) > 0 and int(x) % 2 == 0 else 0, s.split())))