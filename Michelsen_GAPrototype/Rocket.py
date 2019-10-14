class Rocket:
    def __init__(self, l, _dna, targets, obstacles=[]):
        self.position = l.get()
        self.velocity = PVector()
        self.acceleration = PVector()
        
        self.radius = 4
        
        self.gene_counter = 0
        self.hit_target = False
        self.hit_obs = False
        
        self.dna = _dna
        
        self.colors = [128, 128, 128]
        
        self.fitness_score = 0
        self.record_dist = 10000
        self.finish_time = 1
        
        self.targets = targets
        
        self.obstacles = obstacles
        
        self.hit_poison = False
        
    def fitness(self):
        self.fitness_score = (1/(self.finish_time*self.record_dist))
        self.fitness_score = pow(self.fitness_score, 2)
        
        if self.hit_obs:
            self.fitness_score = self.fitness_score * 0.1
            
        if self.hit_poison:
            self.fitness_score = self.fitness_score * 0.01
        
    def run(self, p):
        self.check_target()
        if not self.hit_target and not self.hit_obs and not self.hit_poison:
            self.apply_force(self.dna.genes[self.gene_counter])
            self.gene_counter = (self.gene_counter + 1) % len(self.dna.genes)
            self.update()
            self.obstacle()
            self.poison(p)
            
    def check_target(self):
        d1 = None
        d2 = None
        
        d1 = dist(self.position.x, self.position.y, self.targets[0].x, self.targets[0].y)
        if len(self.targets) > 1:
            d2 = dist(self.position.x, self.position.y, self.targets[1].x, self.targets[1].y)
        
        if d1 < self.record_dist or d2 < self.record_dist:
            if d1 < d2:    
                self.record_dist = d1
                self.colors[0] = self.colors[0] + 40
                self.colors[2] = self.colors[2] - 30
            else:
                self.record_dist = d2
                self.colors[2] = self.colors[2] + 40
                self.colors[0] = self.colors[0] - 30
        
        if d1 < 12 or d2 < 12:
            self.hit_target = True
        else:
            self.finish_time = self.finish_time + 1
                
    def obstacle(self):
        for obs in self.obstacles:
            if obs.contains(self.position):
                self.hit_obs = True
    
    def poison(self, p):
        if p.contains(self.position):
            self.hit_poison = True
        
    def apply_force(self, force):
        self.acceleration.add(force)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.display()
    
    def display(self):
        theta = self.velocity.heading2D() + PI/2
        fill(200, 100)
        stroke(0)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)
        
        rectMode(CENTER)
        fill(0)
        rect(-self.radius/2, self.radius*2, self.radius/2, self.radius)
        rect(self.radius/2, self.radius*2, self.radius/2, self.radius)
        
        fill(self.colors[0], self.colors[1], self.colors[2])
        beginShape(TRIANGLES)
        vertex(0, -self.radius*2)
        vertex(-self.radius, self.radius*2)
        vertex(self.radius, self.radius*2)
        endShape()
        
        popMatrix()
        
    def get_fitness(self):
        return self.fitness_score
    
    def get_dna(self):
        return self.dna
