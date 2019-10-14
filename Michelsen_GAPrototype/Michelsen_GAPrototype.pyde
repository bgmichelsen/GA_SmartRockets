"""
This code shows a basic example of a Genetic Algorithm. It contains several rockets that attempt to search for a target, with rockets evolving based on Darwinian evolution.

This code is based on code written by Daniel Shiffman in his excellent book "The Nature of Code"

"""

from Population import Population
from Obstacle import Obstacle
from Poison import Poison
from Button import Button

life_time = 0
life_counter = 0

targets = []

obstacles = []

poison = None

population = None


obs_width = 50
obs_height = 50

button = None
button_clicked = False

def generate_maze():
    global obs_width
    global obs_height
    global obstacles
    
    obstacles.append(Obstacle(0, 100, obs_width, obs_height + (height-100)))
    obstacles.append(Obstacle(width-obs_width, 100, obs_width, obs_height + (height-100)))
    obstacles.append(Obstacle((width/2)-((obs_width+100)/2), (height/2), obs_width + 100, obs_height))
    obstacles.append(Obstacle(obs_width, 100, obs_width+50, obs_height - 30))
    obstacles.append(Obstacle(width-((obs_width*2)+100), 100, (obs_width+100), obs_height - 30))
    
def setup():
    global life_time
    global targets
    global poison
    global population
    global button
    
    size(640, 360)
    
    life_time = height
    
    targets.append(PVector(200, 24))
    targets.append(PVector(width-200, 24))
    
    poison = Poison(PVector(width/2, height/2 + obs_height + 25))
    
    generate_maze()
    
    m_rate = 0.05
    
    population = Population(m_rate, 50, life_time, targets, poison, obstacles)
    
    button = Button("Run", width/2 - 50, height/2 + 100, 100, 50)
    
def draw():
    global life_time
    global life_counter
    global targets
    global poison
    global population
    global button
    global button_clicked
    
    background(255)
    
    if not button_clicked:
        fill(0)
        text("This is a basic example of Genetic Algorithms (GA) using smart rockets.", width/2, 50)
        text("In the example, a bunch of 'rockets' try to navigate to a given target.", width/2, 68)
        text("Each rocket has some 'DNA', each of which consists of a list of vectors that a rocket can travel on.", width/2, 86)
        text("After several frames, the population of rockets regenerates.", width/2, 104)
        text("The DNA of each rocket changes according to Darwin's laws of evolution.", width/2, 122)
        text("This eventually allows a population of rockets to find the target.", width/2, 140)
        text("In this case, there are two targets: orange (for food) and blue (for water).", width/2, 158)
        text("The population will converge on one or the other, depending on which is closer.", width/2, 176)
        text("There is also a poison object, which the user can use to manipulate how the population evolves.", width/2, 194)
        
        button.display()
    else:
        fill(255, 128, 0)
        ellipse(targets[0].x, targets[0].y, 24, 24)
        fill(0, 128, 255)
        ellipse(targets[1].x, targets[1].y, 24, 24)
        
        poison.update()
        poison.display()
        
        if life_counter < life_time:
            population.live()
            life_counter = life_counter + 1
        else:
            life_counter = 0
            population.fitness()
            population.selection()
            population.reproduction()
        
        for obs in obstacles:
            obs.display()
        
        fill(0)
        text("Generation #: " + str(population.get_generations()), 50, 18)
        text("Cycles Left: " + str((life_time - life_counter)), 50, 36)
        
def mousePressed():
    global button_clicked
    
    if button.mouse_over():
        button_clicked = True
