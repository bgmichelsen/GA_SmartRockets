class DNA:
    def __init__(self, new_genes=[], life_time=100):
        self.genes = new_genes
        
        self.max_force = 0.1
        
        if len(new_genes) == 0:
            for i in range(life_time):
                angle = random(TWO_PI)
                self.genes.append(PVector(cos(angle), sin(angle)))
                self.genes[i].mult(random(0, self.max_force))
    
    def cross_over(self, partner):
        child = []
        
        crossover = int(random(len(self.genes)))
        
        for i in range(len(self.genes)):
            if i > crossover:
                child.append(self.genes[i])
            else:
                child.append(partner.genes[i])
        
        new_genes = DNA(child)
        return new_genes
    
    def mutate(self, m_rate):
        for i in range(len(self.genes)):
            if random(1) < m_rate:
                angle = random(TWO_PI)
                self.genes[i] = PVector(cos(angle), sin(angle))
                self.genes[i].mult(random(0, self.max_force))
