import random


class mom():
    agem = 45
    hairm = "Blec"
    eyesm = "Blue"
    floorm = "Woman"

class dad():
    aged = 52
    haird = "Brown"
    eyesd = "Grey"
    floord = "Man"

class child(dad, mom):

    def ifo(self):
        self.floor = random.randint(1, 2)
        if self.floor == 1:
            self.floor = self.floord

        elif self.floor == 2:
            self.floor = self.floorm
        if self.floor == self.floord:
            self.name = random.randint(1, 4)
            if self.name == 1:
                self.name = "Max"
            elif self.name == 2:
                self.name = "Kirill"
            elif self.name == 3:
                self.name = "Alexander"
            elif self.name == 4:
                self.name = "Anton"
        elif self.floor == self.floorm:
            self.name = random.randint(1, 4)
            if self.name == 1:
                self.name = "Alexandra"
            elif self.name == 2:
                self.name = "Olivia"
            elif self.name == 3:
                self.name = "Sofia"
            elif self.name == 4:
                self.name = "Diana"

        print(self.name)
        print(f"Age {self.aged - self.agem}")
        self.hair = random.randint(1, 2)
        if self.hair == 1:
            self.hair = self.haird

        elif self.hair == 2:
            self.hair = self.hairm
        print(f"Hair {self.hair}")
        self.eyes = random.randint(1, 2)
        if self.eyes == 1:
            self.eyes = self.eyesd

        elif self.eyes == 2:
            self.eyes = self.eyesm
        print(f"Eyes {self.eyes}")
        print(f"Floor {self.floor}")





V = child()
V.ifo()