import random

class Ant:
    def __init__(self, ant_id, speed):
        self.id = ant_id
        self.life = 'alive'
        self.mode = 'looking'
        self.speed = speed
        self.x = 50
        self.y = 50
        self.has_food = False

    def move(self):
        if self.mode == 'looking':
            self.x += random.randint(-1, 1) * self.speed
            self.y += random.randint(-1, 1) * self.speed
        elif self.mode == 'bringing' and self.has_food:
            dx = 50 - self.x
            dy = 50 - self.y
            self.x += 1 if dx > 0 else -1 if dx < 0 else 0
            self.y += 1 if dy > 0 else -1 if dy < 0 else 0

        if self.x < 0: self.x = 0
        if self.x > 100: self.x = 100
        if self.y < 0: self.y = 0
        if self.y > 100: self.y = 100

    def check_food(self, foods):
        for food in foods:
            if abs(self.x - food[0]) <= 2 and abs(self.y - food[1]) <= 2:
                self.mode = 'bringing'
                self.has_food = True
                return True
        return False

    def check_nest(self):
        if abs(self.x - 50) <= 1 and abs(self.y - 50) <= 1 and self.has_food:
            self.mode = 'looking'
            self.has_food = False
            return True
        return False

class Colony:
    def __init__(self):
        self.ants = [
            Ant('0001', 2),
            Ant('0002', 4),
            Ant('0003', 1)
        ]
        self.foods = [(10, 10), (11, 10), (10, 11), (11, 11)]
        self.nest_food = 0

    def simulate(self, seconds):
        for second in range(1, seconds + 1):
            print(f"\n=== Second {second} ===")
            for ant in self.ants:
                if ant.life == 'alive':
                    ant.move()
                    if ant.mode == 'looking':
                        ant.check_food(self.foods)
                    elif ant.mode == 'bringing':
                        if ant.check_nest():
                            self.nest_food += 1
                    print(f"Ant {ant.id} at ({ant.x},{ant.y}) Mode: {ant.mode}")

        print(f"\nTotal food collected: {self.nest_food}")

colony = Colony()
colony.simulate(1000)