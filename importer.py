import Grid

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
    print("Dimensions: x=" + x + " " + "y=" + y + "Grid Lines = " + str(int(x) * int(y)))
    return GridSize


def ImportGrid(line, Nodes):
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
