import Grid
import copy


# Takes in *() and returns the shortest path and Nodes traversed
# B-F-M(Vertexes, Edges, (Statr?)c, (Destination) t)

def BFM(grid, start, end):
    """print("Bellman-Ford-Moore")"""

    numVertexes = int(grid.sizeX) * int(grid.sizeY)
    """Number of Edges in a M by N graph = (m-1)n + (n-1)m 
       I multiply this by 2 as each (x,y) vertex has 2 edges to an adjacent vertex based on heights"""
    numEdges = int(((int(grid.sizeX) - 1) * int(grid.sizeY)) + ((int(grid.sizeY) - 1) * int(grid.sizeX))) * 2

    # int distance to end vertex
    distanceList = []

    # vertex that this location goes to
    successorList = []

    #Populates these lists with 1.5mil as infinity and None as null vertex
    for i in range(numVertexes):
        distanceList.append(1500000)
        successorList.append(None)

    #set successor of end node to 0
    distanceList[CoordinateToInt(grid, end)] = 0

    operations = 1
    while operations < numEdges - 1:
        update = False
        """
        checks edges up, down, left, right
        for each 
            if distanceList > distance-nodeW + edge
                distanceList = distance-nodeW +edge
                successorList = nodeW
                update = True"""
        for i in range(numVertexes):
            nodeW = IntToCoordinate(grid, i)
            """up = 0, right = 1 down = 2 left = 3"""
            direction = 0

            """UP"""
            if ValidEdge(grid, nodeW, direction):
                up = grid.vertexes[nodeW.x][nodeW.y + 1]
                edgeTime = int(EdgeTime(grid, nodeW, up))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, up))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, up))] + edgeTime
                    successorList[i] = up
                    update = True
            direction += 1

            """Right"""
            if ValidEdge(grid, nodeW, direction):
                right = grid.vertexes[nodeW.x + 1][nodeW.y]
                edgeTime = int(EdgeTime(grid, nodeW, right))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, right))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, right))] + edgeTime
                    successorList[i] = right
                    update = True
            direction += 1

            """Down"""
            if ValidEdge(grid, nodeW, direction):
                down = grid.vertexes[nodeW.x][nodeW.y - 1]
                edgeTime = int(EdgeTime(grid, nodeW, down))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, down))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, down))] + edgeTime
                    successorList[i] = down
                    update = True
            direction += 1

            """Left"""
            if ValidEdge(grid, nodeW, direction):
                left = grid.vertexes[nodeW.x - 1][nodeW.y]
                edgeTime = int(EdgeTime(grid, nodeW, left))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, left))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, left))] + edgeTime
                    successorList[i] = left
                    update = True
        if not update:
            break
        operations += 1

    return int(distanceList[int(CoordinateToInt(grid, start))])


def CoordinateToInt(grid, vertex):
    listLocation = int(vertex.x + (vertex.y * grid.sizeX))
    return listLocation


def IntToCoordinate(grid, i):
    y = 0
    while i >= int(grid.sizeX):
        i -= int(grid.sizeX)
        y += 1
    vertex = grid.vertexes[i][y]
    return vertex


def ValidEdge(grid, node, direction):
    valid = True
    x = 0
    y = 0
    if direction == 0:
        y = 1
    elif direction == 1:
        x = 1
    elif direction == 2:
        y = -1
    elif direction == 3:
        x = -1
    if int(node.x) + x < 0 or int(node.y) + y < 0:
        valid = False
    if int(node.x) + x >= int(grid.sizeX) or int(node.y) + y >= int(grid.sizeY):
        valid = False
    return valid


def EdgeTime(grid, nodeW, nodeV):
    time = max(-1, 1 + (int(nodeV.height) - int(nodeW.height)))
    return time
