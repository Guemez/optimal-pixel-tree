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

tracker = numpy.zeros((32, 16, 1), dtype=numpy.uint8)
possibilities = ["white", "trunk", "branch", "leaf"]

trunk = [103, 62, 20]
branch = [133, 88, 35]
leaf = [78, 105, 26]
white = [255, 255, 255]
energyProduced = 0
energyConsumed = 0
nutrientsStored = 0
nutrientsConsumed = 0

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
    p=[0.3, 0.6, 0.1, 0]
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
            print(p)
            tree[x, y] = choosePixel(numpy.random.choice(possibilities, 1, 1, p))

    
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