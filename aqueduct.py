import time
import BFM
import Grid
import Pathfinder
import importer

MaxX = 100
MaxY = 100
MaxHeight = 25

# -1 height for unused location
EmptyVertex = Grid.Vertex(-1, -1, -1, False)
Nodes = [[EmptyVertex for x in range(MaxY)] for y in range(MaxY)]

print("---aqueduct begin---")
"""Test Locations
TestCases/Example1/grid.txt
TestCases/TestCase1/grid.txt
TestCases/TestCase2/grid.txt
"""
File = open("TestCases/TestCase1/grid.txt", "r")
Lines = File.readlines()

GridSize = importer.ImportGridSize(Lines[0])
StationsToVisit = []

iLine = 1
while iLine <= GridSize[0]:
    line = Lines[iLine]
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    importer.ImportGrid(line, Nodes)
    iLine += 1

StationsToVisit.append(importer.ImportStations(Lines[iLine]))
iLine += 1

while iLine < len(Lines):
    line = Lines[iLine]
    StationsToVisit.append(importer.ImportStations(line))
    iLine += 1

StartStation = StationsToVisit[0]
newGrid = Grid.Grid(GridSize[1], GridSize[2], Nodes, StartStation)
i3 = 0
while i3 < len(StationsToVisit):
    print(StationsToVisit[i3].x, StationsToVisit[i3].y, StartStation.height, StationsToVisit[i3].visited)
    i3 += 1

print("---Begin Algorithm---")
minTime = Pathfinder.MinimumDistance(newGrid, StationsToVisit)
print("Minimum cost supply path:", minTime)

with open("pathlength.txt", "w") as File:
    File.write(str(minTime))
print("---End aqueduct.py---")

