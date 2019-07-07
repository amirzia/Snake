
import random
import copy
import sys
import os

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class User:
    num = 1
    
    def __init__(self, board_size):
        self.name = User.num
        User.num += 1
        self.board_size = board_size
        self.pos = [12, 12]
        self.last_move = random.randint(0, 3)
        self.eaten = False
    
    def move(self):
        head = copy.copy(self.pos[len(self.pos) - 1])
        if self.last_move == DOWN:
            if head[0] == self.board_size - 1:
                print("Lost! 1")
                return True
            else:
                head[0] += 1
            self.pos.append(head)
        elif self.last_move == RIGHT:
            if head[1] == self.board_size - 1:
                print("Lost! 2")
                return True
            else:
                head[1] += 1
            self.pos.append(head)
        elif self.last_move == UP:
            if head[0] == 0:
                print("Lost! 3")
                return True
            else:
                head[0] -= 1
            self.pos.append(head)
        elif self.last_move == LEFT:
            if head[1] == 0:
                print("Lost! 4")
                return True
            else:
                head[1] -= 1
            self.pos.append(head)
        else:
            print("Error")
            exit()
        
        if not self.eaten:
            self.pos.pop(0)
        else:
            self.eaten = False
        return False
        
    def go(self, direction):
        self.last_move = direction
        
        
    def get_head(self):
        return self.pos[len(self.pos) - 1]