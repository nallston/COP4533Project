import time

MaxX = 100
MaxY = 100
MaxHeight = 25
StationGrid = [[0 for x in range(MaxX)] for y in range(MaxY)]
GridSize = 0

def ImportGridSize(Line1):
    Line1.strip(" ")
    i =0
    x =""
    y = ""
    temp= ""
    while i<len(Line1):
        if Line1[i] != ",":
            temp += Line1[i]
        else:
            x = temp
            temp = ""
            i+=1
        i+=1
    y = temp
    size = int(int(x)*int(y))
    print(x + " + " + y + "Grid Lines = " + str(int(x)*int(y)))
    File.close()
    return size

def ImportGrid(line):
    x = ""
    y = ""
    height = ""
    i = 0; temp = ""; Number = 0
    while i<len(line):
        if (line[i] == ",") :
            if Number == 0:
                height = temp
                temp = ""
                Number+=1
            else:
                x = temp
                temp = ""
                Number +=1
        else:
            temp += line[i]
        if(Number == 2) & (i+1 == len(line)):
            y = temp
        i+=1
    StationGrid[int(x)][int(y)] = int(height)
    print("At (" + x + "," + y +") height = " + str(StationGrid[int(x)][int(y)]))

def ImportStations(line):

    return "(0,0)"

print("Main program")

File = open("grid.txt", "r")
Lines = File.readlines()
#print(StationGrid[10][0])
GridSize = ImportGridSize(Lines[0])
i = 1
while i <= GridSize:
    line = Lines[i]
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    ImportGrid(line)
    i+=1

StartStation = ImportStations(Lines[GridSize+2])
print(str(StationGrid[99][99]))
print(StartStation)

