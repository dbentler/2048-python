import random

class Dice:
    def __init__(self):
        self.rolls = self.roll()
        
        self.result = self.calculate_result()

        self.visualize()
    
    def roll(self):
        rolls = []
        for i in range(5):
            rolls.append(random.randint(1,6))
        return rolls
    
    def calculate_result(self):
        # If you're looking at this you're cheating!
        result = 0
        for roll in self.rolls:
            if (roll % 2 == 1 and roll != 1):
                result += (roll - 1)
        return result

    def visualize(self):
        for roll in self.rolls:
            if roll == 1:
                print("===========\n"
                      "|         |\n"
                      "|    *    |\n"
                      "|         |\n"
                      "===========\n"
                )
            if roll == 2:
                print("===========\n"
                      "|*        |\n"
                      "|         |\n"
                      "|        *|\n"
                      "===========\n"
                )
            if roll == 3:
                print("===========\n"
                      "|*        |\n"
                      "|    *    |\n"
                      "|        *|\n"
                      "===========\n"
                )
            if roll == 4:
                print("===========\n"
                      "|*       *|\n"
                      "|         |\n"
                      "|*       *|\n"
                      "===========\n"
                )
            if roll == 5:
                print("===========\n"
                      "|*       *|\n"
                      "|    *    |\n"
                      "|*       *|\n"
                      "===========\n"
                )
            if roll == 6:
                print("===========\n"
                      "|*       *|\n"
                      "|*       *|\n"
                      "|*       *|\n"
                      "===========\n"
                )

