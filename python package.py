coins = 100
print(“-- -- -- -- -- -- -- -- -- -- -- -- -- --MENU-- -- -- -- -- -- -- -- -- -- -- -- -- -- --”)
while a == 1:
    print("-----------------Welcome to the 3 in 1 fun city gaming Zone!!-----------------")
print("\n Total coins earned: ", coins)
print("\n 1)Sudoku game")
print(" 2)2048 game")
print(" 3)Tic Tac Toe game")
print(" 4)Exit")
ch = int(input(" Enter your choice..."))
if ch == 1:

    N = 9
UNASSIGNED = 0
row = 0
col = 0
def is_exist_row(grid, row, num):
    for col in range(0, 9):
    if (grid[row][col] == num):
        return 1;
return 0;
def is_exist_col(grid, col, num):
    for row in range(0, 9):
    if (grid[row][col] == num):
        return 1;
return 0;
def is_exist_box(grid, startRow, startCol, num):
    for row in range(0, 3):
    for col in range(0, 3):
    if (grid[row + startRow][col + startCol] == num):
        return 1;
return 0;
def is_safe_num(grid, row, col, num):
    if not(is_exist_row(grid, row, num)):
    if not(is_exist_col(grid, col, num)):
    if not(is_exist_box(grid, row - (row % 3), col - (col % 3), num)):
    return 1, row, col;
else :
    return 0, row, col;
else :
    return 0, row, col;
else :
    return 0, row, col;
def find_unassigned(grid, row, col):
    for row in range(0, N):
    for col in range(0, N):
    if (grid[row][col] == 0):
        return 1, row, col;
return 0, row, col;
def solve(grid):
    row = 0
col = 0
a, row, col = find_unassigned(grid, row, col)
if not a:
    return 1;
for num in range(1, N + 1):
    b, row, col = is_safe_num(grid, row, col, num)
if b:
    grid[row][col] = num;
if (solve(grid)):
    return 1;
grid[row][col] = UNASSIGNED;
return 0;
def print_grid(grid):
    i = 0
j = 0
print('\n\t\t %2d%2d%2d  %2d%2d%2d  %2d%2d%2d\n' % (1, 2, 3, 4, 5, 6, 7, 8, 9))
print("\t\t-------------------------\n")
for i in range(0, 9):
    print("\t")
for j in range(0, 9):
    if (j == 0):
        print(i + 1, "\t| ", end = "")
if (grid[i][j] == 0):
    print(". ", end = "")
else :
    print(grid[i][j], ' ', end = "")
if ((j + 1) % 3 == 0):
    print("| ", end = "")
if ((i + 1) % 3 == 0):
    print("\n\t\t-------------------------", end = "")
print("\n", end = "")
print("\n***************************************************************\n", end = "")# -- -- -- -- -- -- -- -- --MAIN PROGRAM-- -- -- -- -- -- -- -- -- --
    ans = [0]
grid = []
ans = []
print("\n***************************************************************\n")
print("\n                           WELCOME\n")
print("\n***************************************************************\n")

print("\n\n Are you ready for a fun game of sudoku?\n")
print(" Press y for yes(^.^) \n")
ch = input()
print("\nxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox\n")
str = input("\n Enter your name:\n")
print("\n HELLO PLAYER,", str, " !!!!\n")
print("\n Let's get started......\n")
print("\n##################################################################\n")
print("\n Which category do you want to play in?\n")
print("\n 1.Easy\n")
print("\n 2.Medium\n")
print("\n 3.Hard\n")
print("\n 4.Expert\n")
print("\n Enter your choice now:\n")
choice = int(input())
print("\n***************************************************************\n")

if (choice == 1):
    grid = [
        [4, 0, 9, 0, 0, 8, 0, 3, 0],
        [7, 5, 0, 0, 3, 2, 0, 1, 8],
        [0, 0, 0, 5, 0, 0, 2, 0, 6],
        [8, 0, 0, 0, 0, 3, 9, 0, 0],
        [0, 3, 0, 0, 4, 0, 0, 7, 5],
        [0, 0, 1, 2, 0, 7, 0, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 9],
        [0, 1, 0, 0, 0, 9, 0, 4, 0],
        [2, 0, 0, 7, 1, 0, 8, 5, 0]
    ]
f = 0;
ans = [
    [4, 0, 9, 0, 0, 8, 0, 3, 0],
    [7, 5, 0, 0, 3, 2, 0, 1, 8],
    [0, 0, 0, 5, 0, 0, 2, 0, 6],
    [8, 0, 0, 0, 0, 3, 9, 0, 0],
    [0, 3, 0, 0, 4, 0, 0, 7, 5],
    [0, 0, 1, 2, 0, 7, 0, 0, 0],
    [0, 0, 8, 4, 0, 0, 0, 0, 9],
    [0, 1, 0, 0, 0, 9, 0, 4, 0],
    [2, 0, 0, 7, 1, 0, 8, 5, 0]
]
print_grid(grid)
solve(grid)
while (f != 81):
    print("\n Enter the row no. :\n")
r = int(input())
r = r - 1
print("\n Enter the column no.:\n")
c = int(input())
c = c - 1
print("\n Enter the element:\n")
sol = int(input())
if (grid[r][c] == sol):
    ans[r][c] = sol;
print("\n Correct\n")
print("\n Play on !!!\n")
print("\n***************************************************************\n");
print_grid(ans);
for i in range(0, 9):
    for j in range(0, 9):
    if (ans[i][j] == 0):
        f = 0;
    else :
        f = f + 1;
else :
    print("\n Wrong answer\n")
print("\n Don't give up !!\n")
print("\n Continue Playing\n")
print("\n***************************************************************\n")
print_grid(ans);
elif(choice == 2):
    grid = [
        [0, 7, 0, 0, 2, 0, 9, 0, 0],
        [0, 4, 0, 8, 0, 6, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 7, 0],
        [0, 6, 0, 9, 7, 2, 0, 5, 0],
        [0, 2, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 2, 9, 0],
        [0, 0, 0, 5, 0, 4, 0, 3, 0],
        [0, 0, 7, 0, 6, 0, 0, 1, 0]
    ]
f = 0;
ans = [
    [0, 7, 0, 0, 2, 0, 9, 0, 0],
    [0, 4, 0, 8, 0, 6, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 7, 0],
    [0, 6, 0, 9, 7, 2, 0, 5, 0],
    [0, 2, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 2, 9, 0],
    [0, 0, 0, 5, 0, 4, 0, 3, 0],
    [0, 0, 7, 0, 6, 0, 0, 1, 0]
]
print_grid(grid);
solve(grid);
while (f != 81):
    print("\n Enter the row no. :\n")
r = int(input())
r = r - 1;
print("\n Enter the column no.:\n")
c = int(input())
c = c - 1;
print("\n Enter the element:\n")
sol = (input())
if (grid[r][c] == sol):
    ans[r][c] = sol;
print("\n Correct\n")
print("\n Play on !!!\n")
print("\n***************************************************************\n");
print_grid(ans);
for i in range(0, 9):
    for j in range(0, 9):
    if (ans[i][j] == 0):
        f = 0;
    else :
        f = f + 1;
else :
    print("\n Wrong answer\n")
print("\n Don't give up !!\n")
print("\n Continue Playing\n")
print("\n***************************************************************\n")
print_grid(ans);
elif(choice == 3):
    grid = [
        [0, 8, 0, 7, 0, 1, 0, 3, 0],
        [4, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 6, 0, 4, 1, 8],
        [7, 0, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 6, 1, 0, 5, 0, 0],
        [0, 3, 5, 0, 0, 0, 0, 2, 9],
        [0, 6, 0, 4, 0, 7, 0, 9, 0],
        [1, 0, 0, 0, 0, 8, 0, 0, 4],
        [0, 2, 0, 0, 5, 0, 0, 7, 0]
    ]
f = 0;
ans = [
    [0, 8, 0, 7, 0, 1, 0, 3, 0],
    [4, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 6, 0, 4, 1, 8],
    [7, 0, 0, 0, 0, 9, 0, 0, 0],
    [8, 0, 0, 6, 1, 0, 5, 0, 0],
    [0, 3, 5, 0, 0, 0, 0, 2, 9],
    [0, 6, 0, 4, 0, 7, 0, 9, 0],
    [1, 0, 0, 0, 0, 8, 0, 0, 4],
    [0, 2, 0, 0, 5, 0, 0, 7, 0]
]
print_grid(grid);
solve(grid);
while (f != 81):
    print("\n Enter the row no. :\n")
r = int(input())
r = r - 1;
print("\n Enter the column no.:\n")
c = int(input())
c = c - 1;
print("\n Enter the element:\n")
sol = int(input())
if (grid[r][c] == sol):
    ans[r][c] = sol;
print("\n Correct\n")
print("\n Play on !!!\n")
print("\n***************************************************************\n");
coins += 500
print_grid(ans);
for i in range(0, 9):
    for j in range(0, 9):
    if (ans[i][j] == 0):
        f = 0;
    else :
        f = f + 1;
else :
    print("\n Wrong answer\n")
print("\n Don't give up !!\n")
print("\n Continue Playing\n")
print("\n***************************************************************\n")
print_grid(ans);
else :
    print("INVALID CHOICE!!")
a = 0


elif ch == 2:
    from random
import randint
import numpy
def fill_rand_pos(game, rand_1 = 1):
    x_range = []
y_range = []
for i in range(len(game)):
    for j in range(len(game[0])):
    if game[i][j] == 0:
    x_range.append(i)
y_range.append(j)
if not x_range:
    return None
for i in range(rand_1):
    if not x_range:
    break
rand_pos = randint(0, len(x_range) - 1)
game[x_range[rand_pos]][y_range[rand_pos]] = 1
del x_range[rand_pos]
del y_range[rand_pos]
return game
def generate_board(m, n):
    board = [
        [0
            for x in range(n)
        ]
        for y in range(m)
    ]
for i in range(m):
    for j in range(n):
    board[i][j] = 0
return board
def generate_fib_cache(m, n):
    term = m * n
fib = []
fib.append(1)
fib.append(1)# reverse map
fib_term_num_map = {}
for i in range(2, term):
    fib.append(fib[i - 1] + fib[i - 2])
fib_term_num_map[fib[i]] = i
return {
    "fib_series": fib,
    "fib_map": fib_term_num_map
}
def print_board(board):
    for i in range(len(board)):
    col = ""
for j in range(len(board[0])):
    col += str(board[i][j]) + " "
print(col)
def get_sum_list(arr, fib_dict):
    adj1 = -1
sum_list = []
for elem in arr:
    if elem:
    if adj1 == -1:
    adj1 = elem
else :
    if (adj1 + elem) in fib_dict["fib_map"]:
        sum_list.append(adj1 + elem)
adj1 = -1
else :
    sum_list.append(adj1)
adj1 = elem
if adj1 != -1:
    sum_list.append(adj1)
return sum_list
def update_board(board, strp, upd_list, dir):
    k = 0
rows = len(board)
cols = len(board[0])
upd_len = len(upd_list)
if dir == "down":
    rowctr = rows - 1
while rowctr >= 0:
    if k < upd_len:
    board[rowctr][strp] = upd_list[k]
k += 1
else :
    board[rowctr][strp] = 0
rowctr -= 1
elif dir == "up":
    rowctr = 0
while rowctr < rows:
    if k < upd_len:
    board[rowctr][strp] = upd_list[k]
k += 1
else :
    board[rowctr][strp] = 0
rowctr += 1
elif dir == "right":
    colctr = cols - 1
while colctr >= 0:
    if k < len(upd_list):
    board[strp][colctr] = upd_list[k]
k += 1
else :
    board[strp][colctr] = 0
colctr -= 1
if dir == "left":
    colctr = 0
while colctr < cols:
    if k < len(upd_list):
    board[strp][colctr] = upd_list[k]
k += 1
else :
    board[strp][colctr] = 0
colctr += 1
def mov_dir(dir, board, fib_dict):
    cols = len(board[0])
rows = len(board)
if dir == "up"
or dir == "down":
    for j in range(cols):
    col_arr = []
for i in range(rows):
    col_arr.append(board[i][j])
if dir == "down":
    col_arr.reverse()
upd_list = get_sum_list(col_arr, fib_dict)
update_board(board, j, upd_list, dir)
elif dir == "left"
or dir == "right":
    for i in range(rows):
    col_arr = []
for j in range(cols):
    col_arr.append(board[i][j])
if dir == "right":
    col_arr.reverse()# print col_arr
upd_list = get_sum_list(col_arr, fib_dict)
update_board(board, i, upd_list, dir)
def check_win(board, fib_dict):
    for i in range(len(board)):
    for j in range(len(board[0])):
    if board[i][j] == fib_dict["fib_series"][-1]:
    return 1
return 0
m = int(input("Please enter the number of rows(m)"))
n = int(input("Please enter the number of cols(n)"))
board = generate_board(m, n)
fib_dict = generate_fib_cache(m, n)
fill_rand_pos(board, 2)
print("Initial board state")
print_board(board)
dir_moves = ["up", "down", "left", "right"]
if check_win(board, fib_dict):
    print("You won")
exit()
while True:
    dir = input("Please enter the direction(up/down/left/right). For exiting, enter exit.")
dir = dir.lower()
if dir == "exit":
    break
elif dir in dir_moves:
    mov_dir(dir, board, fib_dict)
else :
    print("Please enter a valid move")
print_board(board)
continue
if check_win(board, fib_dict):
    print("You won")
coins += 500
break
if not fill_rand_pos(board):
    print("Game lost")
break
print_board(board)
print_board(board)
print("You earned ", coins, " coins")
a = 0




elif ch == 3:

    import random
import sys
import numpy
board = [i
    for i in range(0, 9)
]
player, computer = '', ''#
Corners, Center and Others, respectively
moves = ((1, 7, 3, 9), (5, ), (2, 4, 6, 8))# Winner combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))# Table
tab = range(1, 10)# to print the board...
def print_board():
    x = 1
for i in board:
    end = ' | '
if x % 3 == 0:
    end = ' \n'
if i != 1: end += '---------\n';
char = ' '
if i in ('X', 'O'): char = i;
x += 1
print(char, end = end)# assigning the charactor / variable
def select_char():
    chars = ('X', 'O')
if random.randint(0, 1) == 0:
    return chars[::-1]
return chars
def can_move(brd, player, move):
    if move in tab and brd[move - 1] == move - 1:
    return True
return False
def can_win(bd, player, move):
    places = []
x = 0
for i in bd:
    if i == player: places.append(x);
x += 1
win = True
for tup in winners:
    win = True
for ix in tup:
    if bd[ix] != player:
    win = False
break
if win == True:
    break
return win
def make_move(bd, player, move, undo = False):
    if can_move(bd, player, move):
    bd[move - 1] = player
win = can_win(bd, player, move)
if undo:
    bd[move - 1] = move - 1
return (True, win)
return (False, False)#
def computer_move():
    move = -1# If I can win, others don 't matter.
for i in range(1, 10):
    if make_move(board, computer, i, True)[1]:
    move = i
break
if move == -1: #Blocking player from winning...
for i in range(1, 10):
    if make_move(board, player, i, True)[1]:
    move = i
break
if move == -1: #Choosing the right position.
for tup in moves:
    for mv in tup:
    if move == -1 and can_move(board, computer, mv):
    move = mv
break
return make_move(board, computer, move)
def space_exist():
    return board.count('X') + board.count('O') != 9
player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result = 'Match tie'
while space_exist():
    print_board()
print('# Make your move ! [1-9] : ', end = '')
move = int(input())
moved, won = make_move(board, player, move)
if not moved:
    print(' Invalid number ! Try again !')
continue#
if won:
    result = '*** You won ! ***'
coins += 500
break
elif computer_move()[1]:
    result = '***You lose !***'
break;
print_board()
print(result)
print("Total coins=", coins)

else :
    print("CONGRATS ON WINNING", coins, "coins")
print("Thank you")