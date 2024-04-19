"""Class Objects I made for the grid and vertexes that populate it"""

class Grid:
    def __init__(self, sizeX, sizeY, vertexes, startStation):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.vertexes = vertexes
        self.startStation = startStation

    def __str__(self):
        return str(self.vertexes)


class Vertex:
    def __init__(self, x, y, height, visited):
        self.x = x
        self.y = y
        self.height = height
        self.visited = visited


"""
string = ""
j = 0
i = 0
while i < xmax:
    while j < ymax:
        print("(" + str(i) + "," + str(j) + ") height = " + str(Nodes[i][j].height))
        j += 1
    j = 0
    i += 1

"""
