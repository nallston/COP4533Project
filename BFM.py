import Grid
import copy


# Takes in *() and returns the shortest path and Nodes traversed
# B-F-M(Vertexes, Edges, (Statr?)c, (Destination) t)

def BFM(grid, start, end):
    """print("Bellman-Ford-Moore")"""

    numVertexes = int(grid.sizeX) * int(grid.sizeY)
    #distanceStart = copy.deepcopy(grid.vertexes)

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
    while operations < numVertexes:
        update = False
        print("operations", operations)
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
                    #print("new distance: " + str(distanceList[i]) + " (" + str(nodeW.x) + "," + str(nodeW.y) + ") to: (" + str(up.x) + "," + str(up.y) + ") Calc: " + str(distanceList[i] - int(edgeTime)) + " + " + str(edgeTime))
                    successorList[i] = up
                    update = True
            direction += 1

            """Right"""
            if ValidEdge(grid, nodeW, direction):
                right = grid.vertexes[nodeW.x + 1][nodeW.y]
                edgeTime = int(EdgeTime(grid, nodeW, right))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, right))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, right))] + edgeTime
                    #print("new distance: " + str(distanceList[i]) + " (" + str(nodeW.x) + "," + str(nodeW.y) + ") to: (" + str(right.x) + "," + str(right.y) + ") Calc: " + str(distanceList[i] - int(edgeTime)) + " + " + str(edgeTime))
                    successorList[i] = right
                    update = True
            direction += 1

            """Down"""
            if ValidEdge(grid, nodeW, direction):
                down = grid.vertexes[nodeW.x][nodeW.y - 1]
                edgeTime = int(EdgeTime(grid, nodeW, down))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, down))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, down))] + edgeTime
                    #print("new distance: " + str(distanceList[i]) + " (" + str(nodeW.x) + "," + str(nodeW.y) + ") to: (" + str(down.x) + "," + str(down.y) + ") Calc: " + str(distanceList[i] - int(edgeTime)) + " + " + str(edgeTime))
                    successorList[i] = down
                    update = True
            direction += 1

            """Left"""
            if ValidEdge(grid, nodeW, direction):
                left = grid.vertexes[nodeW.x - 1][nodeW.y]
                edgeTime = int(EdgeTime(grid, nodeW, left))
                if distanceList[i] > (distanceList[int(CoordinateToInt(grid, left))] + edgeTime):
                    distanceList[i] = distanceList[int(CoordinateToInt(grid, left))] + edgeTime
                    #print("new distance: " + str(distanceList[i]) + " (" + str(nodeW.x) + "," + str(nodeW.y) + ") to: (" + str(left.x) + "," + str(left.y) + ") Calc: " + str(distanceList[i] - int(edgeTime)) + " + " + str(edgeTime))
                    successorList[i] = left
                    update = True
        if not update:
            break
        operations += 1

    print("Bellman-Ford-Moore End")
    print("End Vertex =", end.x, ",", end.y, "Start Vertex =", start.x, ",", start.y)
    print(successorList[int(CoordinateToInt(grid, start))].x, ",", successorList[int(CoordinateToInt(grid, start))].y)
    print("Distance at End -> End:", distanceList[int(CoordinateToInt(grid, end))], "Distance at Start -> End:", distanceList[int(CoordinateToInt(grid, start))])
    return int(distanceList[int(CoordinateToInt(grid, start))])


def CoordinateToInt(grid, vertex):
    listLocation = int(vertex.x + (vertex.y * grid.sizeX))
    return listLocation


def IntToCoordinate(grid, i):
    y = 0
    #print("size =", grid.sizeX, "i =", i)
    while i >= int(grid.sizeX):
        #print(i, y)
        i -= int(grid.sizeX)
        y += 1
    #print("i =", i, "y =", y)
    vertex = grid.vertexes[i][y]
    #print("vertex = (", vertex.x, ",", vertex.y, ")")
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
    #print("vertex = (", nodeSide.x, ",", nodeSide.y, ")")
    if int(node.x) + x < 0 or int(node.y) + y < 0:
        valid = False
    if int(node.x) + x >= int(grid.sizeX) or int(node.y) + y >= int(grid.sizeY):
        valid = False
    return valid


def EdgeTime(grid, nodeW, nodeV):
    time = max(-1, 1 + (int(nodeV.height) - int(nodeW.height)))
    return time


"""#print("(0,0) is", CoordinateConverter(grid, grid.vertexes[0][0]))
#print("(2,0) is", CoordinateConverter(grid, grid.vertexes[2][0]))
#print("(0,2) is", CoordinateConverter(grid, grid.vertexes[0][2]))
#print("(2,2) is", CoordinateConverter(grid, grid.vertexes[2][2]))"""
