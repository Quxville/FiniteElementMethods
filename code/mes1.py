# imports
from element import Element
from node import Node
from print import printing

iterator = 0
globalDataLines = []

# reading from a file
with open("Test2_4_4_MixGrid.txt", "r") as f:
    stringMesh = f.read()

# throwing file data to a table
tableMesh = stringMesh.split('\n')

# getting global data from a file table
for iterator in range(10):
    globalDataLines.append(tableMesh[iterator])

# getting pure global data from global data table
globalData = []
for elements in globalDataLines:
    globalData.append(elements.split(' ')[1])

# getting nodes to a table
iterator += 2
tableNode = []
while tableMesh[iterator] != "*Element, type=DC2D4":
    output = tableMesh[iterator].split(", ")
    node = Node(float(output[1]), float(output[2]), 0, 0)
    tableNode.append(node)
    iterator += 1

# getting elements to a table
iterator += 1
tableElement = []
while tableMesh[iterator] != "*BC":
    output = tableMesh[iterator].split(", ")
    tableElement.append(Element(int(output[1]), int(output[2]), int(output[3]), int(output[4])))
    iterator += 1

# getting BC flags table from a line
iterator += 1
arrayBC = tableMesh[iterator].split(", ")
arrayBClen = len(arrayBC)

# assigning BC flags to correct nodes
for i in range(len(tableNode)):
    for j in range(arrayBClen):
        if (i+1) == float(arrayBC[j]):
            tableNode[i].BC = 1

# printing data with a custom functions
# print("Global data: \n")
# printing(globalData)
#
# print("Nodes: \n")
# printing(tableNode)
#
# print("ELements:")
# printing(tableElement)

SimulationTime = int(globalData[0])
SimulationStepTime = int(globalData[1])
Conductivity = int(globalData[2])
Alfa = int(globalData[3])
Tot = int(globalData[4])
InitialTemp = int(globalData[5])
Density = int(globalData[6])
SpecificHeat = int(globalData[7])
NodesNumber = int(globalData[8])
ElementsNumber = int(globalData[9])