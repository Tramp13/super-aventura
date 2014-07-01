import math
from point import Point

class Camera:
    def __init__(self, width, height, right_boundry, bottom_boundry):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.half_width = int(math.floor((float(width) / 2)))
        self.half_height = int(math.floor((float(height) / 2)))
        self.right_boundry = right_boundry
        self.bottom_boundry = bottom_boundry

    def center_on(self, target_x, target_y):
        self.x = target_x - self.half_width
        self.y = target_y - self.half_height
        if (target_x < self.half_width):
            self.x = 0
        if (target_y < self.half_height):
            self.y = 0
        if (target_x + self.half_width >= self.right_boundry):
            self.x = self.right_boundry - self.width
        if (target_y + self.half_height >= self.bottom_boundry):
            self.y = self.bottom_boundry - self.height

    # This function iterates through all cells that are visible to the camera
    def __iter__(self):
        cells = []
        for y in range(self.y, self.y + self.height):
            for x in range(self.x, self.x + self.width):
                cells.append(Point(x, y))
        return iter(cells)
