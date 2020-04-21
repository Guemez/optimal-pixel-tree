import numpy
from PIL import Image
from random import randint

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

data = numpy.zeros((32, 16, 3), dtype=numpy.uint8)
data.fill(255)

trunk = [103, 62, 20]
branch = [133, 88, 35]
leaf = [78, 105, 26]
energyProduced = 0
energyConsumed = 0
nutrientsStored = 0
nutrientsConsumed = 0

def createRandomLifeform():
    tree = numpy.zeros((32, 16, 3), dtype=numpy.uint8)
    tree.fill(255)
    print(len(tree[1]))
    for i in range(0, len(tree[0])):
        # Favors some empty space for starting generation
        if randint(0, 1) > 0.5:
            tree[31, i] = trunk
    return tree

data = createRandomLifeform()

#data[0, 0] = trunk
#data[0, 1] = branch
#data[0, 2] = leaf

for row in data:
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

score = ((energyProduced - energyConsumed) ** 2) + ((nutrientsStored - nutrientsConsumed) ** 2)
print(score)

image = Image.fromarray(data)
image.show()