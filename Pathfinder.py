import Grid
import time
import BFM
import copy
BFMCount = 0

def addCount():
    global BFMCount
    BFMCount +=1

def MinimumDistance(grid, Stations):
    """OPT(T,B) = min( for all in B: OPT(T,B) + remaining OPT(T,B))"""
    startStation = Stations.pop(0)
    minTime = 15000000

    minTime = BFMRecursion(grid, Stations, startStation)
    #print("BFMCount =", BFMCount)
    return minTime


def BFMRecursion(grid, Stations, start):
    minTime = 15000000
    if len(Stations) == 0:
        return 0
    for i in range(len(Stations)):
        newTime = BFM.BFM(grid, start, Stations[i])
        newStations = copy.deepcopy(Stations)
        newStart = newStations.pop(i)
        #addCount()
        newTime = newTime + BFMRecursion(grid, newStations, newStart)
        minTime = min(minTime, newTime)
    return minTime