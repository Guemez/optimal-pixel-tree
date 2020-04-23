import numpy
from PIL import Image
import random
#from random import randint

"""
A pixel tree must comply with the following characteristics:

All the tree trunk pixels must be connected.
The pixels of a tree branch must be connected. 
The branches must be connected to the tree trunk.
The pixels of a leaf must be connected.
A leaf cannot have more than 8 pixels.
The leaves must be connected to a tree branch.
The bottom eight pixels only can be tree trunk pixels or white spaces.

"""

possibilities = ["white", "trunk", "branch", "leaf"]
trunk = [103, 62, 20]
branch = [133, 88, 35]
leaf = [78, 105, 26]
white = [255, 255, 255]

def score(tree):
    energyProduced = 0
    energyConsumed = 0
    nutrientsStored = 0
    nutrientsConsumed = 0
    for row in tree:
        for pixel in row:
            if pixel[0] == leaf[0] and pixel[1] == leaf[1] and pixel[2] == leaf[2]:
                energyProduced = energyProduced + 2
                nutrientsConsumed = nutrientsConsumed + 0.25
            if pixel[0] == trunk[0] and pixel[1] == trunk[1] and pixel[2] == trunk[2]:
                energyConsumed = energyConsumed + 0.25
                nutrientsConsumed = nutrientsConsumed + 0.5
            if pixel[0] == branch[0] and pixel[1] == branch[1] and pixel[2] == branch[2]:
                nutrientsStored = nutrientsStored + 1.5
                energyConsumed = energyConsumed + 0.1
    #ORIGINAL
    score = ((energyProduced - energyConsumed) ** 2) + ((nutrientsStored - nutrientsConsumed) ** 2)
    #MODIFICATION
    #score = ((energyProduced - energyConsumed)) + ((nutrientsStored - nutrientsConsumed))
    return score



def isSomething(p):
    if p[0] != 255:
        return True

def choosePixel(s):
    #print(s)
    if s == "leaf":
        #print("=======")
        return leaf
    elif s == "branch":
        #print("=======")
        return branch
    elif s == "trunk":
        #print("=======")
        return trunk
    else:
        #print("=======")
        return white

def choose(w, t, b, l):
    #print(w)
    #print(t)
    #print(b)
    #print(l)
    if w == 3:
        return [1,0,0,0]
    if t == 3:
        return [0,1,0,0]
    if b == 3:
        return [0,0,1,0]
    if l == 3:
        return [0,0,0,1]
    if w == 2 and t == 1:
        return [.6, .3, .1, 0]
    if w == 2 and b == 1:
        return [.6, 0, .3, .1]
    if w == 2 and l == 1:
        return [.7, .0, .0, .3]
    if t == 2 and w == 1:
        return [.4, .5, .1, 0]
    if t == 2 and b == 1:
        return [.1, .5, .3, .1]
    if t == 2 and l == 1:
        return [.1, .6, .0, .3]
    if b == 2 and w == 1:
        return [.2, .0, .5, .3]
    if b == 2 and t == 1:
        return [.3, .2, .3, .2]
    if b == 2 and l == 1:
        return [.3, .0, .3, .4]
    if l == 2 and w == 1:
        return [.6, .0, .0, .4]
    if l == 2 and t == 1:
        return [.6, .0, .0, .4]
    if l == 2 and b == 1:
        return [.5, .0, .2, .3]
    if w == 1 and t == 1 and b == 1:
        return [.5,.2,.2,.1]
    if w == 1 and t == 1 and l == 1:
        return [.5,.2,.2,.1]
    if w == 1 and b == 1 and l == 1:
        return [.5,.0,.3,.2]
    if t == 1 and b == 1 and l == 1:
        return [.1,.3,.3,.3]

#choosePixel(numpy.random.choice(possibilities, 1, p))

def createRandomLifeform():
    tree = numpy.zeros((32, 16, 3), dtype=numpy.uint8)
    tree.fill(255)
    #p=[0.3, 0.6, 0.1, 0]
    t = numpy.random.randint(low=4, high=8)
    r = numpy.random.randint(low=0, high=16-t)
    for i in range(r, r+t):
        tree[31, i] = trunk 

    for x in range(30, 1, -1):
        for y in range(1, 14):
            w = 0
            t = 0
            b = 0
            l = 0
            if tree[x+1, y-1][0] == leaf[0]:
                l+=1
            if tree[x+1, y-1][0] == trunk[0]:
                t+=1
            if tree[x+1, y-1][0] == branch[0]:
                b+=1
            if tree[x+1, y-1][0] == white[0]:
                w+=1
            if tree[x+1, y][0] == leaf[0]:
                l+=1
            if tree[x+1, y][0] == trunk[0]:
                t+=1
            if tree[x+1, y][0] == branch[0]:
                b+=1
            if tree[x+1, y][0] == white[0]:
                w+=1
            if tree[x+1, y+1][0] == leaf[0]:
                l+=1
            if tree[x+1, y+1][0] == trunk[0]:
                t+=1
            if tree[x+1, y+1][0] == branch[0]:
                b+=1
            if tree[x+1, y+1][0] == white[0]:
                w+=1
            p = choose(w,t,b,l)
            #print(p)
            tree[x, y] = choosePixel(numpy.random.choice(possibilities, 1, 1, p))
    return tree



def generate_population(size):
    population = []
    for i in range(size):
        individual = createRandomLifeform()
        population.append(individual)
    return population


def sort_population_by_fitness(population):
    #print("population")
    #print(population)
    score_population = []
    order = []
    for t in range(len(population)):
        score_population.append(score(population[t]))
        order.append([t, score(population[t])])
    sorted_population = []
    score_population.sort()
    for s in score_population:
        for o in order:
            if s == o[1]:
                i = o[0]
                sorted_population.append(population[i])
                break
    return sorted_population


def choice_by_roulette(population, fitness_sum):
    sorted_population = sort_population_by_fitness(population)
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = score(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = score(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual

def crossover(individual_a, individual_b):
    tree = numpy.zeros((32, 16, 3), dtype=numpy.uint8)
    tree.fill(255)
    for x in range(0, 32):
        for y in range(0, 8):
            tree[x,y] = individual_a[x,y]
    for x in range(0, 32):
        for y in range(8, 16):
            tree[x,y] = individual_b[x,y]
    return tree


def mutate(individual):
    x = 0
    y = 0
    while isSomething(individual[x,y]) != True:
        x = random.randint(0,31)
        y = random.randint(0,15)

    r = random.randint(0,3)
    if r == 0:
        individual[x,y] = trunk
    elif r == 1:
        individual[x,y] = branch
    elif r == 2:
        individual[x,y] = leaf

    return individual

def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(score(individual) for individual in population)

    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        second_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        """image = Image.fromarray(first_choice)
        image.show()
        image = Image.fromarray(second_choice)
        image.show()"""
        individual = crossover(first_choice, second_choice)
        #image = Image.fromarray(individual)
        #image.show()
        individual = mutate(individual)
        next_generation.append(individual)
        

    return next_generation


size = 8
generations = 10
population = generate_population(size)
optimal = population[0]

i = 1
while True:
    print(f"🧬 GENERATION {i}")

    for individual in population:
        if score(individual) > score(optimal):
            optimal = individual
    if i == generations:
        break
    i += 1
    # Make next generation...
    population = make_next_generation(population)

print("\n🔬 FINAL RESULT")
print(score(optimal))
image = Image.fromarray(optimal)
image.show()