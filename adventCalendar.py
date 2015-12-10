import md5 
import re

def firstDayA():
    f = open('day1.txt', 'r')
    a = f.read()
    i = [x for x in a if x == '(']
    j = [x for x in a if x == ')']
    print 'he is on floor' + str(len(i) - len(j))
    
    
def firstDayB():
    f = open('day1.txt', 'r')
    a = f.read()
    floor = 0;
    for i in range(0, len(a)):
        if a[i] == '(':
            floor += 1
        else: 
            floor -= 1
        if floor == -1:
            print i + 1
            break
            

def secondDayA():
    f = open('day2.txt', 'r')
    total = 0
    for line in f:
        dimensions = [int(x) for x in line.split('x')]
        side1 = dimensions[0] * dimensions[1]
        side2 = dimensions[0] * dimensions[2]
        side3 =  dimensions[1] * dimensions[2] 
        total += 2 * side1 + 2 * side2 + 2 * side3 + min(side1 , side2, side3)
    print total
    
def secondDayB():
    f = open('day2.txt', 'r')
    ribbon = 0
    for line in f:
        dimensions = [int(x) for x in line.split('x')]
        nonMaxValues = []
        if len([x for x in dimensions if x is max(dimensions)]) == 1:
            nonMaxValues = [x for x in dimensions if x is not max(dimensions)]
        else:
            nonMaxValues.append(min(dimensions))
            nonMaxValues.append(max(dimensions))
        ribbon += 2 * nonMaxValues[0] + 2 * nonMaxValues[1]        
        ribbon += dimensions[0] * dimensions[1] * dimensions[2]
    print ribbon
   
def thirdDayA():
    f = open('day3.txt', 'r')
    currentPosition = (0, 0)
    allCommands = f.read()
    visitedHouses = dict([(currentPosition, 1)])
    for command in allCommands:
        if command == '^': 
            currentPosition = (currentPosition[0], currentPosition[1] + 1)
        if command == 'v': 
            currentPosition = (currentPosition[0], currentPosition[1] - 1)
        if command == '<':
            currentPosition = (currentPosition[0] - 1, currentPosition[1])
        if command == '>':
            currentPosition = (currentPosition[0] + 1, currentPosition[1])
        dictEntryValue = visitedHouses.get(currentPosition, 0)
        visitedHouses[currentPosition] = dictEntryValue + 1
    print len(visitedHouses.keys())

def thirdDayB():
    f = open('day3.txt', 'r')
    currentPositionSanta = (0, 0)
    currentPositionRobot = (0, 0)
    allCommands = f.read()
    visitedHouses = dict([(currentPositionSanta, 1)])
    i = 0
    for command in allCommands:
        if command == '^': 
            currentMovement = (0, 1)
        if command == 'v': 
            currentMovement = (0, - 1)
        if command == '<':
            currentMovement = (- 1, 0)
        if command == '>':
            currentMovement = (1,0)
        if i % 2 == 0:
            currentPositionSanta = (currentPositionSanta[0] + currentMovement[0], currentPositionSanta[1] + currentMovement[1])
            dictEntryValue = visitedHouses.get(currentPositionSanta, 0)
            visitedHouses[currentPositionSanta] = dictEntryValue + 1
        else:
            currentPositionRobot = (currentPositionRobot[0] + currentMovement[0], currentPositionRobot[1] + currentMovement[1])
            dictEntryValue = visitedHouses.get(currentPositionRobot, 0)
            visitedHouses[currentPositionRobot] = dictEntryValue + 1
        i += 1
    print len(visitedHouses.keys())
    
def fourthDayA():
    i = 0
    key = "ckczppom"
    while True:
        m = md5.new()
        m.update(key + str(i))
        if m.digest()[0:3] <= '\x00\x00\x0f':
            print key + str(i)
            break
        else:
            i+=1
            
def fourthDayB():
    i = 0
    key = "ckczppom"
    while True:
        m = md5.new()
        m.update(key + str(i))
        if m.digest()[0:3] == '\x00\x00\x00':
            print key + str(i)
            break
        else:
            i+=1
            
def fifthDayA():
    f = open("day5.txt", 'r')
    nrOfNice = 0
    for word in f:
        if len(re.findall('[aeuio]', word)) < 3:
            continue
        repeats = False
        for i in range (0, len(word)-1):
            if word[i] == word[i+1]:
                repeats = True
                break
        if repeats == False:
            continue
        if len(re.findall('ab|cd|pq|xy', word)) > 0:
            continue
        nrOfNice += 1
        
    print nrOfNice