import copy


FOOD = 9
OBSTACLE = 8

class Game:
    
    def __init__(self, size=32):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.users = []
        self.foods = []
        self.obstacles = []
        self.lost = False
        
    def add_user(self, user):
        self.users.append(user)
    
    def update_board(self):
        for user in self.users:
            self.lost = user.move()

            head = user.get_head()
            if self.get_board()[head[0]][head[1]] in [3 - user.name, 8]:
                print(user.name, "game over")
                return True
            for food in self.foods:
                if (food[0] == head[0]) and (food[1] == head[1]):
                    user.eaten = True
                    self.foods.remove(food)
        print("in update board: ", self.lost)
        return self.lost
        

    def get_board(self):
        # board = list(reversed(copy.deepcopy(self.board)))
        board = copy.deepcopy(self.board)
        for user in self.users:
            pos = user.pos
            for p in pos:
                board[p[0]][p[1]] = user.name
            
            for food in self.foods:
                board[food[0]][food[1]] = FOOD
            for obstacle in self.obstacles:
                board[obstacle[0]][obstacle[1]] = OBSTACLE
        # return list(reversed(board))
        return board
        
    
    def get_scores(self):
        scores = []
        for user in self.users:
            scores.append(len(user.pos) - 1)
        return scores

    def print_board(self):
        board = get_board()
                
        for row in board:
            print(row)
            
    def add_food(self, pos):
        self.foods.append(pos)

    def add_obstacle(self, pos):
        self.obstacles.append(pos)
