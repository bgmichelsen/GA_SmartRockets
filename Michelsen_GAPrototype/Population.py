from DNA import DNA
from Rocket import Rocket

class Population:
    def __init__(self, m_rate, pop_size, l_time, targets, poison, obstacles=[]):
        self.mutation_rate = m_rate
        self.population = []
        self.mating_pool = []
        
        self.life_time = l_time
        self.generations = 0
        
        self.targets = targets
        
        self.obstacles = obstacles
        
        self.poison = poison
        
        for i in range(pop_size):
            position = PVector(width/2, height+20)
            dna = DNA(life_time=self.life_time)
            self.population.append(Rocket(position, dna, self.targets, self.obstacles))
        
    def live(self):
        for i in range(len(self.population)):
            self.population[i].run(self.poison)
            
    def fitness(self):
        for i in range(len(self.population)):
            self.population[i].fitness()
            
    def selection(self):
        self.mating_pool = []
        
        max_fitness = self.get_max_fitness()
        
        for i in range(len(self.population)):
            fitness_normal = map(self.population[i].get_fitness(), 0, max_fitness, 0, 1)
            n = int(fitness_normal * 100)
            for j in range(n):
                self.mating_pool.append(self.population[i])
                
    def reproduction(self):
        for i in range(len(self.population)):
            m = int(random(len(self.mating_pool)))
            f = int(random(len(self.mating_pool)))
            
            mother = self.mating_pool[m]
            father = self.mating_pool[f]
            
            mother_genes = mother.get_dna()
            father_genes = father.get_dna()
            
            child = mother_genes.cross_over(father_genes)
            child.mutate(self.mutation_rate)
            
            position = PVector(width/2, height+20)
            self.population[i] = Rocket(position, child, self.targets, self.obstacles)
            
        self.generations = self.generations + 1
        
    def get_generations(self):
        return self.generations
    
    def get_max_fitness(self):
        record = 0
        
        for i in range(len(self.population)):
            if self.population[i].get_fitness() > record:
                record = self.population[i].get_fitness()
        return record
