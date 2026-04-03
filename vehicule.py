import random

class Vehicle:
    def __init__(self, vid):
        self.id = vid
        self.position = random.uniform(0, 100)
        self.speed = random.uniform(10, 30)
        self.braking = False

    def move(self):
        self.position += self.speed * 0.1

    def brake(self):
        self.braking = True
        self.speed = max(0, self.speed - 10)
