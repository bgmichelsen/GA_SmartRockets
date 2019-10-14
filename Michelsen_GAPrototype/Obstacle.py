class Obstacle:
    def __init__(self, x, y, _w, _h):
        self.position = PVector(x, y)
        
        self.WIDTH = _w
        self.HEIGHT = _h
        
    def display(self):
        stroke(0)
        fill(175)
        strokeWeight(2)
        rectMode(CORNER)
        rect(self.position.x, self.position.y, self.WIDTH, self.HEIGHT)
        
    def contains(self, obj):
        return (obj.x > self.position.x and obj.x < (self.position.x + self.WIDTH)) and (obj.y > self.position.y and obj.y < (self.position.y + self.HEIGHT))
