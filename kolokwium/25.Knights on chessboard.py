n = int(input())
board = [list(input()) for _ in range(n)]

moves = 0
chess = 0
vertical_pos = []
horizontal_pos = []
for line in range(n):
    for col in range(n):
        if board[line][col] == 's':
            chess += 1
            vertical_pos.append(col)
            horizontal_pos.append(line)

for i in range(chess):
    for j in range(chess):
        if abs(horizontal_pos[i] - horizontal_pos[j]) == 1 and abs(vertical_pos[i] - vertical_pos[j]) == 2:
            moves += 1
        if abs(horizontal_pos[i] - horizontal_pos[j]) == 2 and abs(vertical_pos[i] - vertical_pos[j]) == 1:
            moves += 1
print(moves)