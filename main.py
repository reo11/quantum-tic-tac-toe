import random
from collections import defaultdict
# 量子五目並べ
# 一旦10x10
# https://www.youtube.com/watch?v=mitAxA3f4U4
PLAYER_NAMES = ["White", "Black"]
BOARD_SIZE = 10

class Board:
    def __init__(self):
        self.init_board()

    def init_board(self):
        self.board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.winner = -1

    def print_header(self):
        print('  ', end='')
        for i in range(BOARD_SIZE):
            ci = chr(ord('A') + i)
            print(ci, end=' ')
        print()

    def print_body(self):
        for i in range(BOARD_SIZE):
            print(i + 1, end=' ')
            for j in range(BOARD_SIZE):
                if self.board[i][j] == -1:
                    print(' ', end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def print_body_obs(self, player_num):
        print("#### Observed Board ####")
        obs_board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == -1:
                    obs_board[i][j] = ' '
                else:
                    if random.random() * 10.0 < self.board[i][j]:
                        obs_board[i][j] = 'x' # Black
                    else:
                        obs_board[i][j] = 'o' # White
        for i in range(BOARD_SIZE):
            print(i + 1, end=' ')
            for j in range(BOARD_SIZE):
                print(obs_board[i][j], end=' ')
            print()
        print("#### Observed Board End ####")
        who_win = self.check_win(obs_board)
        if who_win == -1:
            print("Winner is not decided yet")

        if who_win == 0:
            print("White win")
            self.winner = 0
        elif who_win == 1:
            print("Black win")
            self.winner = 1
        elif who_win == 2:
            print(f"{PLAYER_NAMES[player_num]} win")

    def print_board(self, player_num, obs=False):
        print("x: Black, o: White")
        self.print_header()
        if obs:
            self.print_body_obs(player_num)
        else:
            self.print_body()

    def check_win(self, board):
        # 勝敗判定, 縦横斜めでoかxが5つ並んだら勝ち
        # 同時に存在している場合は現在の手番の勝ち
        # flag = -1: 未確定, 0: o, 1: x, 2: 手番の勝ち
        flag = -1
        bw = {"o": 0, "x": 1}
        streak = []
        # 横
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] in bw:
                    if len(streak) == 0:
                        streak.append(board[i][j])
                    else:
                        if board[i][j] == streak[-1]:
                            streak.append(board[i][j])
                        else:
                            streak = [board[i][j]]
                    if len(streak) == 5:
                        if streak[0] == bw["o"]:
                            if flag == 1:
                                return 2 # 手番の勝ち
                            else:
                                flag = 0
                        else:
                            if flag == 0:
                                return 2 # 手番の勝ち
                            else:
                                flag = 1
                else:
                    streak = []
            streak = []
        streak = []
        # 縦
        for j in range(BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if board[i][j] in bw:
                    if len(streak) == 0:
                        streak.append(board[i][j])
                    else:
                        if board[i][j] == streak[-1]:
                            streak.append(board[i][j])
                        else:
                            streak = [board[i][j]]
                    if len(streak) == 5:
                        if streak[0] == bw["o"]:
                            if flag == 1:
                                return 2 # 手番の勝ち
                            else:
                                flag = 0
                        else:
                            if flag == 0:
                                return 2 # 手番の勝ち
                            else:
                                flag = 1
                else:
                    streak = []
            streak = []
        # 斜め(左上から右下)
        streak = []
        start_pos = [[0, i] for i in range(BOARD_SIZE)] + [[i, 0] for i in range(1, BOARD_SIZE)]
        for start_y, start_x in start_pos:
            for i in range(BOARD_SIZE):
                if start_y + i >= BOARD_SIZE or start_x + i >= BOARD_SIZE:
                    break
                if board[start_y + i][start_x + i] in bw:
                    if len(streak) == 0:
                        streak.append(board[start_y + i][start_x + i])
                    else:
                        if board[start_y + i][start_x + i] == streak[-1]:
                            streak.append(board[start_y + i][start_x + i])
                        else:
                            streak = [board[start_y + i][start_x + i]]
                    if len(streak) == 5:
                        if streak[0] == bw["o"]:
                            if flag == 1:
                                return 2
            streak = []

        # 斜め(右上から左下)
        streak = []
        start_pos = [[0, i] for i in range(BOARD_SIZE)] + [[i, BOARD_SIZE - 1] for i in range(1, BOARD_SIZE)]
        for start_y, start_x in start_pos:
            for i in range(BOARD_SIZE):
                if start_y + i >= BOARD_SIZE or start_x - i < 0:
                    break
                if board[start_y + i][start_x - i] in bw:
                    if len(streak) == 0:
                        streak.append(board[start_y + i][start_x - i])
                    else:
                        if board[start_y + i][start_x - i] == streak[-1]:
                            streak.append(board[start_y + i][start_x - i])
                        else:
                            streak = [board[start_y + i][start_x - i]]
                    if len(streak) == 5:
                        if streak[0] == bw["o"]:
                            if flag == 1:
                                return 2
                        else:
                            if flag == 0:
                                return 2
            streak = []
        return flag

    def set_value(self, x, y, value):
        self.board[y][x] = value


class Game:
    def __init__(self):
        self.board = Board()
        self.turn_count = 0

    def valid_pos(self):
        while True:
            try:
                pos = input()
                if pos == "exit":
                    exit()
                col = ord(pos[0]) - ord('A')
                row = int(pos[1:]) - 1
                if col < 0 or col >= BOARD_SIZE or row < 0 or row >= BOARD_SIZE:
                    print("Invalid input")
                    continue
                return [col, row]
            except:
                print("Invalid input")
                continue

    def valid_value(self):
        while True:
            try:
                value = input()
                if value == "exit":
                    exit()
                value = int(value)
                if value < 1 or value > 9:
                    print("Invalid input")
                    continue
                return value
            except:
                print("Invalid input")
                continue

    def valid_obs(self):
        while True:
            try:
                obs = input()
                if obs == "exit":
                    exit()
                if obs != 'y' and obs != 'n':
                    print("Invalid input")
                    continue
                return obs
            except:
                print("Invalid input")
                continue


    def play(self):
        while True:
            player_num = self.turn_count % 2
            self.board.print_board(player_num)
            print(f"Player {PLAYER_NAMES[player_num]}'s turn")
            print("Enter the coordinates of the stone you want to place. (ex. A1)")
            col, row = self.valid_pos()
            print("Enter the value between 1 to 9 (White 1 ... 9 Black")
            value = self.valid_value()
            self.board.set_value(col, row, value)
            print(f"Player {PLAYER_NAMES[player_num]} placed {value} at {chr(ord('A') + col)}{row + 1}")
            print("Do you want to make an observation? (y/n)")
            obs = self.valid_obs()
            if obs == "y":
                # 観測
                self.board.print_board(player_num, obs=True)
                if self.board.winner != -1:
                    break
            self.turn_count += 1

def main():
    print('Start Quantum Gomoku')
    game = Game()
    game.play()

if __name__ == '__main__':
    main()