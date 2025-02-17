class Settings:
    """Class for game settings"""
    
    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = "Bubble Bluster"
        
        self.bubble_min_r = 10
        self.bubble_max_r = 50
        
        self.bonus_score = 1000
        
        self.bubble_speed_factor = 1.0
        self.speedup_scale = 1.1
        
    def increase_speed(self):
        self.bubble_speed_factor *= self.speedup_scale