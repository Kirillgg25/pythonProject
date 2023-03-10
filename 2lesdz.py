import random


class Student:
    def __init__(self, name):

        self.name = name
        self.gladness = 58
        self.progress = 8
        self.alive = True
        self.mone = 20

    def to_study (self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3
        if self.progress >= 8:
            self.work()
        elif self.mone >= 40:
            self.progress += 0.2
            self.mone -= 15
    # def to_sleep(self):
    #     print("I will sleep")
    #     self.gladness += 3
    def to_chill(self):
        print("Rest time")
        if self.gladness <= 50:
            self.gladness += 5
            self.progress -= 0.1
            self.mone -= 5
        else:
            self.to_study()

    def work(self):
        print("The work is done")
        self.gladness -= 1
        self.progress -= 0.1
        self.mone += 7

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress < 5:
            print("Passed externally...")
            self.alive = False
        elif self.mone <= -50:
            print("Duty")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money ={self.mone}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        # elif live_cube == 2:
        #     self.to_sleep()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
