import numpy as np
from PIL import Image
from random import randint

colors = [
    (255, 255, 255, 255), #White
    (103, 62, 20, 255), #Trunk
    (133, 88, 35, 255), #Branches
    (78, 105, 26, 255), #Leaves
]

class Cell(object):
    color = (255, 255, 255, 255)
    t = 0

    def __init__(self, t=0):
        self.t = t
        self.color = colors[t]

lifeFormDNA = np.full((32, 16, 1), Cell())

class Plant(object):
    dna = np.full((32, 16, 1), Cell())
    fitness = 0

    def __init__(self, dna):
        self.dna = dna
        self.fitness = self.calcFitness(dna)

    def calcFitness(self, dna):
        nutrientsUsed = 0
        nutrients = 0
        energy = 0
        energyUsed = 0

        for i in range(0, 32):
            for j in range(0, 16):
                if dna[i, j][0].t == 1:
                    nutrients += 1.5
                    energyUsed += 0.1
                elif dna[i, j][0].t == 2:
                    nutrientsUsed += 0.5
                    energyUsed += 0.25
                elif dna[i, j][0].t == 3:
                    nutrientsUsed += 0.25
                    energy += 2

        energyDiff = energy - energyUsed
        nutrientDiff = nutrients - nutrientsUsed

        score = energyDiff**2 + nutrientDiff**2

        return score


def generateRandomPlant():
    for i in range(0, 32):
        for j in range(0, 16):
            if i > 8:
                lifeFormDNA[i,j][0] = Cell(randint(0, 1))
            else:
                lifeFormDNA[i,j][0] = Cell(randint(0, 3))

    plant = Plant(lifeFormDNA)

    return plant

def convertPlantToImage(plant):
    plantImage = np.zeros((32, 16, 3), dtype=np.uint8)
    plantImage.fill(255)

    for i in range(0, 32):
        for j in range(0, 16):
            plantImage[i, j][0] = plant[i, j][0].color

    return plantImage

plant = generateRandomPlant()
print(convertPlantToImage(plant.dna))

#image = Image.fromarray()
#image.show()