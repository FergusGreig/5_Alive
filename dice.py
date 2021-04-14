import random
class gamedie(sides):
    def __init__(self):
        self.alive = True
        self.score = 6

    def roll(self):
        if self.alive:
            self.score = random.randint(1, sides)

    def toside(self):
        self.alive = False

    def togame(self):
        self.alive = True


class dice(ndie,nsides):
    def __init__(self):
        dielist = []
        for x in range(ndie):
            dielist.append(gamedie(nsides))

    def roll(self):
        for die in dielist:
            die.roll()
    
    def setaside(self,dienum):
        dielist[dienum].toside()
    
    def refresh(self):
        for die in dielist:
            die.togame()



if __name__=='__main__':
    die = gamedie()
    for x in range(3):
        die.roll()
        print(die.score)