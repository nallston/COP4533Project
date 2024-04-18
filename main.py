import time
import BFM
import Grid



MaxX = 100
MaxY = 100
MaxHeight = 25
GridSize = 0
# -1 height for unused location
EmptyVertex = Grid.Vertex(-1, -1, -1, False)
Nodes = [[EmptyVertex for x in range(MaxY)] for y in range(MaxY)]

def ImportGridSize(Line1):
    Line1.strip(" ")
    GridSize = []
    i = 0
    x = ""
    y = ""
    temp = ""
    while i < len(Line1):
        if Line1[i] != ",":
            temp += Line1[i]
        else:
            x = temp
            temp = ""
            i += 1
        i += 1
    y = temp
    GridSize.append(int(int(x) * int(y)))
    GridSize.append(int(x))
    GridSize.append(int(y))
    print(x + " + " + y + "Grid Lines = " + str(int(x) * int(y)))
    File.close()
    return GridSize


def ImportGrid(line):
    x = ""
    y = ""
    height = ""
    i2 = 0
    temp = ""
    Number = 0
    while i2 < len(line):
        if line[i2] == ",":
            if Number == 0:
                height = temp
                temp = ""
                Number += 1
            else:
                x = temp
                temp = ""
                Number += 1
        else:
            temp += line[i2]
        if (Number == 2) & (i2 + 1 == len(line)):
            y = temp
        i2 += 1

    newVertex = Grid.Vertex(int(x), int(y), int(height), False)
    Nodes[int(x)][int(y)] = newVertex
    print("At (" + str(Nodes[int(x)][int(y)].x) + "," + str(Nodes[int(x)][int(y)].y) + ") height = " + str(
        Nodes[int(x)][int(y)].height) + " Visited = " + str(Nodes[int(x)][int(y)].visited))


def ImportStations(line):
    line.strip(" ")
    i = 0
    x = ""
    y = ""
    temp = ""
    while i < len(line):
        if line[i] != ",":
            temp += line[i]
        else:
            x = temp
            temp = ""
            i += 1
        i += 1
    y = temp
    return Grid.Vertex(int(x), int(y), -1, False)


print("Main program")
"""Test Locations
TestCases/Example1/grid.txt
TestCases/TestCase1/grid.txt
TestCases/TestCase2/grid.txt

"""
File = open("TestCases/TestCase1/grid.txt", "r")
Lines = File.readlines()

GridSize = ImportGridSize(Lines[0])
StationsToVisit = []

iLine = 1
while iLine <= GridSize[0]:
    line = Lines[iLine]
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    ImportGrid(line)
    iLine += 1

StationsToVisit.append(ImportStations(Lines[iLine]))
iLine += 1

while iLine < len(Lines):
    line = Lines[iLine]
    StationsToVisit.append(ImportStations(line))
    iLine += 1

StartStation = StationsToVisit[0]
newGrid = Grid.Grid(GridSize[1], GridSize[2], Nodes, StartStation)
i3 = 0
while i3 < len(StationsToVisit):
    print(StationsToVisit[i3].x, StationsToVisit[i3].y,StartStation.height, StationsToVisit[i3].visited)
    i3 += 1

distance1 = BFM.BFM(newGrid, StationsToVisit[0], StationsToVisit[1])
print("Back to main:", distance1)
distance2 = BFM.BFM(newGrid, StationsToVisit[0], StationsToVisit[2])
print("Back to main:", distance2)

if distance1 < distance2:
    distance = distance1 + BFM.BFM(newGrid, StationsToVisit[1], StationsToVisit[2])
else:
    distance = distance1 + BFM.BFM(newGrid, StationsToVisit[2], StationsToVisit[1])
print(distance)
