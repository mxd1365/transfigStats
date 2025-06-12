import requests
import os
import itertools
import statistics
import numpy as np
import argparse

parser = argparse.ArgumentParser();
parser.add_argument('--league', help='The name of the league to search', type=str, default='Settlers')
parser.add_argument('--topGemListSize', help='The number of top gems to show', type=int, default='20')
parser.add_argument('--cheapestGemListSize', help='The number of cheapest gems to show', type=int, default='10')
args = parser.parse_args()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#import lists of gems
def importGems(fileName):
    gemList = {}
    with open(__location__ + '\\' + fileName) as file:
        for gemName in file:
            gemList[gemName.strip()] = None
    return gemList

redGems = importGems('redGems.txt')
redTransfiguredGems = importGems('redTransfiguredGems.txt')

greenGems = importGems('greenGems.txt')
greenTransfiguredGems = importGems('greenTransfiguredGems.txt')

blueGems = importGems('blueGems.txt')
blueTransfiguredGems = importGems('blueTransfiguredGems.txt')


#populate prices of gems
skillUrl = 'https://poe.ninja/api/data/itemoverview?league={}&type=SkillGem'.format(args.league)

response = requests.get(skillUrl)
allSkillGems = response.json()['lines']

def populateGemPrice(gemList):
    for key in gemList:
        #price of gem assumes level 20 with 20 quality. Ignore gems with "low confidence" in poe.ninja
        gemStats = next((gem for gem in allSkillGems if gem['name'] == key and gem['gemLevel'] == 20 and 'corrupted' not in gem.keys() and 'gemQuality' in gem.keys() and gem['gemQuality'] == 20 and len(gem['sparkline']['data']) > 0), None)
    
        if gemStats != None: #ignore if no one is selling level 20 uncorrupted version of this gem with 20 quality
            gemList[key] = gemStats['chaosValue']

    return {name: value for name, value in gemList.items() if value is not None}

redGems = populateGemPrice(redGems)
redTransfiguredGems = populateGemPrice(redTransfiguredGems)

greenGems = populateGemPrice(greenGems)
greenTransfiguredGems = populateGemPrice(greenTransfiguredGems)

blueGems = populateGemPrice(blueGems)
blueTransfiguredGems = populateGemPrice(blueTransfiguredGems)

#find the minimum value gems in each color
def getCheapestGem(gemList):
    minValue = min(gemList.values())
    return next(gemItem for gemItem in gemList.items() if gemItem[1] == minValue)

cheapestRedGem = getCheapestGem(redGems)
cheapestGreenGem = getCheapestGem(greenGems)
cheapestBlueGem = getCheapestGem(blueGems)

#calculate average rate of return on each color
def getTransfigGemStats(gemList):
    allRollPermutations = list(itertools.permutations(gemList.items(), 3)) #get all possible rolls from shrine
    maxValues = []
    #get the max value of each permuation
    for rollPermutation in allRollPermutations:
        values = map(lambda roll: roll[1], rollPermutation)
        maxValues.append(max(values))

    #get the average value of each permutation
    mean = statistics.mean(maxValues)

    normalizedMaxValues = maxValues / np.linalg.norm(maxValues)
    return [mean, statistics.median(maxValues), np.std(normalizedMaxValues)]

redGemStats = getTransfigGemStats(redTransfiguredGems)
greenGemStats = getTransfigGemStats(greenTransfiguredGems)
blueGemStats = getTransfigGemStats(blueTransfiguredGems)

def printStats(stats, transfigValueList, gemValueList, color, cheapestRegGem):
    print('\n\n--------------{} GEMS----------------'.format(color))
    print('{} gems: mean of profit: {}, median of profit: {}, normal standard deviation of gem values: {}'.format(color, stats[0] - cheapestRegGem[1], stats[1] - cheapestRegGem[1], stats[2]))
    
    print('\nTop 10 {} transfiguration gems'.format(color))
    sortedByValue = list(dict(sorted(transfigValueList.items(), key=lambda item: item[1], reverse=True)).items())
    for i in range(0,args.topGemListSize):
        print('\t{}. {}: {}'.format(i + 1, sortedByValue[i][0], sortedByValue[i][1]))

    print('\nTop 10 cheapest {} gems'.format(color))
    sortedByValue = list(dict(sorted(gemValueList.items(), key=lambda item: item[1])).items())
    for i in range(0,args.cheapestGemListSize):
        print('\t{}. {}: {}'.format(i + 1, sortedByValue[i][0], sortedByValue[i][1]))

printStats(redGemStats, redTransfiguredGems, redGems, 'RED', cheapestRedGem)
printStats(greenGemStats, greenTransfiguredGems, greenGems, 'GREEN', cheapestGreenGem)
printStats(blueGemStats, blueTransfiguredGems, blueGems, 'BLUE', cheapestBlueGem)





