from random import randint

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = 0
        
    def change_name(self, name):
        self.name = name
        print(self.name)

    def show_score(self):
        print(self.name, "has a score of ", self.score) 

    def dice_roll(self):
        dice_r = randint(1,6)
        print(self.name, "landed on", dice_r)
        self.score = self.score + dice_r
        print(self.name, "is up to number", self.score, "on the board. \n")
        return(self.score)

    def snake(self):
        if self.score % 9 == 0:
            self.score = self.score - 4
            print("OUCH!-YOU HAVE LANDED ON A SNAKE!")
            print(self.name, "has gone down the board by 4 points.")
            print(self.name, "is upto", self.score, "on the board \n")
        return(self.score)

    def ladders(self):
        if self.score % 10 == 0:
            self.score = self.score + 8
            print("NICE!- YOU HAVE LANDED ON A LADDER!")
        
            print(self.name, "has gone up the board by 8 points.")
            print(self.name, "is upto", self.score, "on the board \n")
        return(self.score)    

    def winner(self):
        if self.score >= 100:
            print(self.name, "HAS WON!---END OF GAME")       
            self.score = 0    
            
def play_game(player):
    player.dice_roll()
    player.snake()
    player.ladders()
    player.winner()
    roll = (input("Press Enter to roll."))
    
player1 = Player("Dino", 0)
player2 = Player("Abby", 0)
          
print("LET'S PLAY SNAKES AND LADDERS \nThe first to reach up to 100 on the board is the winner \n")
while True:
  choose_player = int(input("Enter either 1 for first player, or 2 for second player:"))
  if choose_player == 1:
    play_game(player1)
  elif choose_player == 2:
  	play_game(player2)
