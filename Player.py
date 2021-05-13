class Player:
    def __init__(self):
        self.currentRoll = 1
        self.correctGuess = 0
        self.streak = 0
        self.potentate = False
    
    def __repr__(self):
        return f"Current Roll: {self.currentRoll} | Correct Guesses: {self.correctGuess} | Streak: {self.streak} | Potentate: {self.potentate}"