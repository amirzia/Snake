import copy


FOOD = 9

class Game:
    
    def __init__(self, size=10):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.users = []
        self.foods = []
        
    def add_user(self, user):
        self.users.append(user)
    
    def update_board(self):
        for user in self.users:
            user.move()
            
            head = user.get_head()
            for food in self.foods:
                if (food[0] == head[0]) and (food[1] == head[1]):
                    user.eaten = True
                    self.foods.remove(food)
        

    def get_board(self):
        # board = list(reversed(copy.deepcopy(self.board)))
        board = copy.deepcopy(self.board)
        for user in self.users:
            pos = user.pos
            for p in pos:
                board[p[0]][p[1]] = user.name
            
            for food in self.foods:
                board[food[0]][food[1]] = FOOD
        # return list(reversed(board))
        return board
        
    
    def get_scores(self):
        scores = []
        for user in self.users:
            scores.append(len(user.pos))
        return scores

    def print_board(self):
        board = get_board()
                
        for row in board:
            print(row)
            
    def add_food(self, pos):
        self.foods.append(pos)
        
