#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy  as np

class Board:
    positions_array = np.array(np.arange(10))
    def __init__(self, token):
        self.token = token
        self.board_state = np.zeros([3,3], dtype=str)
        self.board_state[0,0] = "1"
        self.board_state[0,1] = "2"
        self.board_state[0,2] = "3"
        self.board_state[1,0] = "4"
        self.board_state[1,1] = "5"
        self.board_state[1,2] = "6"
        self.board_state[2,0] = "7"
        self.board_state[2,1] = "8"
        self.board_state[2,2] = "9"
        self.positions_dict = {}
        self.positions_dict[0,0] = "1"
        self.positions_dict[0,1] = "2"
        self.positions_dict[0,2] = "3"
        self.positions_dict[1,0] = "4"
        self.positions_dict[1,1] = "5"
        self.positions_dict[1,2] = "6"
        self.positions_dict[2,0] = "7"
        self.positions_dict[2,1] = "8"
        self.positions_dict[2,2] = "9"
        if token == 'X':
            self.other = 'O'
        else:
            self.other = 'X'
    def move(self, x, y):
        self.board_state[x][y] = self.token
    def aimove(self, x, y):
        self.board_state[x][y] = self.other
    def win_check(self):
        if self.board_state[0][0] == self.token and self.board_state[0][1] == self.token and self.board_state[0][2] == self.token:
            return True
        if self.board_state[1][0] == self.token and self.board_state[1][1] == self.token and self.board_state[1][2] == self.token:
            return True
        if self.board_state[2][0] == self.token and self.board_state[2][1] == self.token and self.board_state[2][2] == self.token:
            return True
        if self.board_state[0][0] == self.token and self.board_state[1][0] == self.token and self.board_state[2][0] == self.token:
            return True
        if self.board_state[0][1] == self.token and self.board_state[1][1] == self.token and self.board_state[2][1] == self.token:
            return True
        if self.board_state[0][2] == self.token and self.board_state[1][2] == self.token and self.board_state[2][2] == self.token:
            return True
        if self.board_state[0][0] == self.token and self.board_state[1][1] == self.token and self.board_state[2][2] == self.token:
            return True
        if self.board_state[0][2] == self.token and self.board_state[1][1] == self.token and self.board_state[2][0] == self.token:
            return True
        return False
    def AIwin_check(self):
        if self.board_state[0][0] == self.other and self.board_state[0][1] == self.other and self.board_state[0][2] == self.other:
            return True
        if self.board_state[1][0] == self.other and self.board_state[1][1] == self.other and self.board_state[1][2] == self.other:
            return True
        if self.board_state[2][0] == self.other and self.board_state[2][1] == self.other and self.board_state[2][2] == self.other:
            return True
        if self.board_state[0][0] == self.other and self.board_state[1][0] == self.other and self.board_state[2][0] == self.other:
            return True
        if self.board_state[0][1] == self.other and self.board_state[1][1] == self.other and self.board_state[2][1] == self.other:
            return True
        if self.board_state[0][2] == self.other and self.board_state[1][2] == self.other and self.board_state[2][2] == self.other:
            return True
        if self.board_state[0][0] == self.other and self.board_state[1][1] == self.other and self.board_state[2][2] == self.other:
            return True
        if self.board_state[0][2] == self.other and self.board_state[1][1] == self.other and self.board_state[2][0] == self.other:
            return True
        return False
    #makes list of all empty positions that ai can choose from at random, randomness is bad implementation of ai i know, will try to improve this
    def board_to_list(self):
        newlist = []
        for row in range(3):
            for col in range(3):
                if self.board_state[row][col] != self.token and self.board_state[row][col] != self.other:
                    pos = self.positions_dict[row, col]
                    newlist.append(pos)
        return newlist
    # def board_state_blanks(self):
    #     ipBoard = np.zeros([3,3], dtype=str)
    #     for row in range(3):
    #         for col in range(3):
    #             if self.board_state[row, col] == "O":
    #                 ipBoard[row,col] = 'O'
    #             if self.board_state[row, col] == "X":
    #                 ipBoard[row,col] = 'X'
    #             else:
    #                 ipBoard[row,col] = ''
    #     print(ipBoard)

def token_select():
    value = input("Choose your token, press X or O:")
    return value
def create_board(token):
    if token == "X":
        return Board("X")
    if token == "O":
        return Board("O")
def move_prompt():
    value = input("please select 1-9 to determine token position for move:")
    return value
def move(position):
    if position == 1:
       return 0, 0
    if position == 2:
       return 0, 1
    if position == 3:
       return 0, 2
    if position == 4:
       return 1, 0
    if position == 5:
       return 1, 1
    if position == 6:
       return 1, 2
    if position == 7:
        return 2, 0
    if position == 8:
       return 2, 1
    if position == 9:
       return 2, 2


# In[16]:


def main():
    positions_dict = {}
    positions_dict["1"] = [0,0]
    positions_dict["2"] = [0,1]
    positions_dict["3"] = [0,2]
    positions_dict["4"] = [1,0]
    positions_dict["5"] = [1,1]
    positions_dict["6"] = [1,2]
    positions_dict["7"] = [2,0]
    positions_dict["8"] = [2,1]
    positions_dict["9"] = [2,2]
    coords_to_num = {}
    coords_to_num
    value = token_select()
    board = Board(value)
    print(board.board_state)
    while True:
        # my turn
        value = move_prompt()
        coords = positions_dict[value]
        x = coords[0]
        y = coords[1]
        board.move(x, y)
        print(board.board_state)
        #check for 3 in a row
        if board.win_check():
            print("Congratulations, you won!")
            return 
        # AI turn
        position_coord = board.board_to_list()
        ai_selection = np.random.choice(position_coord)
        print("--------------------")
        print("--------------------")
        print("computer chooses " + ai_selection + "!")
        ai_coordList = positions_dict[ai_selection]
        x = ai_coordList[0]
        y = ai_coordList[1]
        board.aimove(x, y)
        print(board.board_state)
        #check for 3 in a row
        if board.AIwin_check():
            print("Uhoh, you lost to a computer!")
            return 
main()


# In[ ]:





# In[ ]:




