import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="w",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s")
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def date(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        if self.money >= 70:
            self.money -= 60
            self.satiety += 10
            self.gladness += 5
        else:
            pass

    def relatives(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money -= 10
        self.gladness += 5

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            logging.info("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            logging.info("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            logging.info("Hooray! Delicious!")
            self.gladness += 5
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 5
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        logging.info(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        logging.info(f"{human_indexes:^50}")
        print(f"Money – {self.money}")
        logging.info(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        logging.info(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        logging.info(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        logging.info(f"{home_indexes:^50}")
        print(f"Food – {self.home.food}")
        logging.info(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        logging.info(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        logging.info(f"{car_indexes:^50}")
        print(f"Fuel – {self.car.fuel}")
        logging.info(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        logging.info(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.info("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.info("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            logging.info("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            logging.info("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
            logging.info(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
            logging.info(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 6)
        if self.satiety < 20:
            print("I'll go eat")
            logging.info("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                logging.info("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                logging.info("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                logging.info("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            logging.info("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            logging.info("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            logging.info("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            logging.info("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            logging.info("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            logging.info("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Went to relatives")
            logging.info("Went to relatives")
            self.relatives()
        elif dice == 6:
            print("I'm going on a date")
            logging.info("I'm going on a date")
            self.date()

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            logging.info("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(800):
    if nick.live(day) == False:
        break
