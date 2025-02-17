class GameStats():
    def __init__(self):
        self.game_active = False
        self.high_score = self.load_high_score()
        self.reset_stats()
        
    
    def reset_stats(self):
        self.level = 1
        self.score = 0
        self.bonus = 0
        
    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except FileNotFoundError:
                return 0
            
    def save_high_score(self):
        with open("highscore", "w") as f:
            f.write(str(self.high_score))
            
            
            