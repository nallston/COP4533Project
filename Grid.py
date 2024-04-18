class GridPath:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])
        self.visited = [False in range(self.width * self.height)]

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

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeight(self):
        return self.height

    def getVisited(self):
        return self.visited

    def newHeight(self, height):
        self.height = height

    def newVisit(self, visited):
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
