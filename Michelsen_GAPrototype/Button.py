class Button:
    def __init__(self, label, _x, _y, _w, _h):
        self.label = label
        self.position = PVector(_x, _y)
        
        self.WIDTH = _w
        self.HEIGHT = _h
        
    def display(self):
        fill(218)
        stroke(0)
        
        rect(self.position.x, self.position.y, self.WIDTH, self.HEIGHT, 10)
        
        textAlign(CENTER, CENTER)
        fill(0)
        text(self.label, self.position.x + (self.WIDTH/2), self.position.y + (self.HEIGHT/2))
        
    def mouse_over(self):
        return (mouseX > self.position.x and mouseX < (self.position.x + self.WIDTH)) and (mouseY > self.position.y and mouseY < (self.position.y + self.HEIGHT))
