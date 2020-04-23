import numpy as np
from PIL import Image


# Función que calcula el score y hace las elecciones según sea el caso
def plantSelections(options, nC, nP, eC, eP):
    scores = []
    population = np.random.choice(options,len(options), replace=True)
    for option in population:
        if option == 0:
            energyProduced = eP + 0.0
            energyConsumed = eC + 0.0
            nutrientsProduced = nP + 0.0
            nutrientsConsumed = nC + 0.0
        if option == 1:
            energyProduced = eP + 0.0
            energyConsumed = eC + 0.1
            nutrientsProduced = nP + 1.5
            nutrientsConsumed = nC + 0.0
        if option == 2:
            energyProduced = eP + 0.0
            energyConsumed = eC + 0.25
            nutrientsProduced = nP + 0.5
            nutrientsConsumed = nC + 0.5
        if option == 3:
            energyProduced = eP + 2.0
            energyConsumed = eC + 0.0
            nutrientsProduced = nP + 0.0
            nutrientsConsumed = nC + 0.25
        scores.append((energyProduced - energyConsumed)**2 + (nutrientsProduced - nutrientsConsumed)**2)
    
    #fitness = np.arrray(scores)
    #print("The total scores are: ")
    #print(scores)
    selection = scores.index(max(scores))
    #print("And the selected is: ")
    #print(selection)
    if population[selection] == 0:
        energyProduced = eP + 0.0
        energyConsumed = eC + 0.0
        nutrientsProduced = nP + 0.0
        nutrientsConsumed = nC + 0.0
    if population[selection] == 1:
        energyProduced = eP + 0.0
        energyConsumed = eC + 0.1
        nutrientsProduced = nP + 1.5
        nutrientsConsumed = nC + 0.0
    if population[selection] == 2:
        energyProduced = eP + 0.0
        energyConsumed = eC + 0.25
        nutrientsProduced = nP + 0.5
        nutrientsConsumed = nC + 0.5
    if population[selection] == 3:
        energyProduced = eP + 2.0
        energyConsumed = eC + 0.0
        nutrientsProduced = nP + 0.0
        nutrientsConsumed = nC + 0.25

    return [population[selection],nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced]

# Significado de cada índice
# blanco 0, tronco 1, rama 2, hoja 3

optionsTrunk=[0,1]
optionsTrunkBranch=[0,1,2]
optionsBranchLeaf=[0,2,3]
optionsLeaf=[0,3]
# Inicialización de la imagen para RGB y 16x32 pixeles
img=Image.new('RGB',(16,32),(255, 255, 255))
# En la raíz tenemos tronco al centro, lo agregamos a la planta y contamos con esta línea como la línea anterior
line=[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]
plant=[line]
prevLine=line
# Inicializamos la energía y los nutrientes en 100
energyProduced = 0.0
nutrientsProduced = 0.0
energyConsumed = 0.0
nutrientsConsumed = 0.0
# Para los primeros 8 pixeles sólo crearemos tronco o nada
for i in range(7):
    # Inicializamos una nueva línea
    line=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lineIndexes=list(filter(lambda x: prevLine[x] != 0, range(len(prevLine))))
    for index in lineIndexes:
        print("En el índice: " + str(index))
        if index+1<16:
            '''print("Para el derecho")
            selection = plantSelections(optionsTrunk,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
            nutrientsConsumed=selection[1]
            nutrientsProduced=selection[2]
            energyConsumed=selection[3]
            energyProduced=selection[4]
            print(selection)
            line[index+1]=selection[0]'''
            line[index+1]=np.random.choice(optionsTrunk)
        if index-1>0:
            '''print("Para el izquierdo")
            selection = plantSelections(optionsTrunk,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
            nutrientsConsumed=selection[1]
            nutrientsProduced=selection[2]
            energyConsumed=selection[3]
            energyProduced=selection[4]
            print(selection)
            line[index-1]=selection[0]'''
            line[index-1]=np.random.choice(optionsTrunk)
        '''print("Para el de en medio")
        selection = plantSelections(optionsTrunk,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
        nutrientsConsumed=selection[1]
        nutrientsProduced=selection[2]
        energyConsumed=selection[3]
        energyProduced=selection[4]
        print(selection)
        line[index]=selection[0]'''
        line[index]=np.random.choice(optionsTrunk)
    plant.append(line)
    print(line)
    prevLine=line

# Para los últimos 24 pixeles, crearemos de lo que sea
for i in range(24):
    line=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lineIndexes=list(filter(lambda x: prevLine[x] != 0, range(len(prevLine))))
    for index in lineIndexes:
        if index+1<16:
            if prevLine[index]==1:
                selection = plantSelections(optionsTrunkBranch,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index+1]=selection[0]
                #line[index+1]=np.random.choice(optionsTrunkBranch)
            if prevLine[index]==2:
                selection = plantSelections(optionsBranchLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index+1]=selection[0]
                #line[index+1]=np.random.choice(optionsBranchLeaf)
            if prevLine[index]==3:
                selection = plantSelections(optionsLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index+1]=selection[0]
                #line[index+1]=np.random.choice(optionsLeaf)
        if index-1>0:
            if prevLine[index]==1:
                selection = plantSelections(optionsTrunkBranch,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index-1]=selection[0]
                #line[index-1]=np.random.choice(optionsTrunkBranch)
            if prevLine[index]==2:
                selection = plantSelections(optionsBranchLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index-1]=selection[0]
                #line[index-1]=np.random.choice(optionsBranchLeaf)
            if prevLine[index]==3:
                selection = plantSelections(optionsLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
                nutrientsConsumed=selection[1]
                nutrientsProduced=selection[2]
                energyConsumed=selection[3]
                energyProduced=selection[4]
                print(selection)
                line[index-1]=selection[0]
                #line[index-1]=np.random.choice(optionsLeaf)
        if prevLine[index]==1:
            selection = plantSelections(optionsTrunkBranch,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
            nutrientsConsumed=selection[1]
            nutrientsProduced=selection[2]
            energyConsumed=selection[3]
            energyProduced=selection[4]
            print(selection)
            line[index]=selection[0]
            #line[index]=np.random.choice(optionsTrunkBranch)
        if prevLine[index]==2:
            selection = plantSelections(optionsBranchLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
            nutrientsConsumed=selection[1]
            nutrientsProduced=selection[2]
            energyConsumed=selection[3]
            energyProduced=selection[4]
            print(selection)
            line[index]=selection[0]
            #line[index]=np.random.choice(optionsBranchLeaf)
        if prevLine[index]==3:
            selection = plantSelections(optionsLeaf,nutrientsConsumed,nutrientsProduced,energyConsumed,energyProduced)
            nutrientsConsumed=selection[1]
            nutrientsProduced=selection[2]
            energyConsumed=selection[3]
            energyProduced=selection[4]
            print(selection)
            line[index]=selection[0]
            #line[index]=np.random.choice(optionsLeaf)
    plant.append(line)
    prevLine=line
for line in plant:
    print(line)

for y in range(len(plant)):
    for x in range(len(plant[y])):
        if plant[y][x]==0:
            img.putpixel((x,y),(255,255,255))
        if plant[y][x]==1:
            img.putpixel((x,y),(112,59,2))
        if plant[y][x]==2:
            img.putpixel((x,y),(166,108,46))
        if plant[y][x]==3:
            img.putpixel((x,y),(55,166,46))

img.save("sqr.jpg")
img.show()