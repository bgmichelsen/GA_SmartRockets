class Poison:
    def __init__(self, position):
        self.position = position
        
        self.r = 30
        
    def display(self):
        fill(85, 205, 50)
        ellipse(self.position.x, self.position.y, self.r, self.r)
        
    def contains(self, obj):
        return (pow((obj.x - self.position.x), 2) + pow((obj.y - self.position.y), 2) <= pow(self.r, 2))

    def update(self):
        self.position.x = mouseX
        self.position.y = mouseY
