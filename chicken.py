import random
import directions
from entity import Entity
from sprite import Sprite
from tiles import Wheat

class Chicken(Entity):
    def __init__(self, x, y):
        sprite = Sprite.get('CHICKEN')
        super(Chicken, self).__init__(x, y, 'chicken', sprite)
        self.owner = None

    def update(self):
        if self.owner != None:
            x_distance = abs(self.owner.x - self.x)
            y_distance = abs(self.owner.y - self.y)
            if x_distance > 1 or y_distance > 1:
                if x_distance > y_distance:
                    if (self.owner.x > self.x):
                        self.move(directions.EAST)
                    elif (self.owner.x < self.x):
                        self.move(directions.WEST)
                else:
                    if (self.owner.y > self.y):
                        self.move(directions.SOUTH)
                    elif (self.owner.y < self.y):
                        self.move(directions.NORTH)
                return
        self.move(random.choice([0, 1, 2, 3, 4]))
