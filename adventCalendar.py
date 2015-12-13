import md5 
import re
import numpy as np
import copy
import json

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

def fifthDayB():
    f = open("day5.txt", 'r')
    nrOfNice = 0
    for word in f:
        if len(re.findall("(\w\w).*\\1", word)) < 1:
            continue
        if len(re.findall("(\w)\w\\1", word)) < 1:
            continue
        nrOfNice += 1
    print nrOfNice

def sixthDayA():
    f = open("day6.txt", 'r')
    grid = np.zeros((1000, 1000),  dtype=bool)
    for line in f:
        ranges = re.findall("\d+\d*", line)
        ranges = [(int(ranges[0]), int(ranges[1])), (int(ranges[2]), int(ranges[3]))]
        if "turn on" in line:
            grid[ranges[0][0]:ranges[1][0] + 1, ranges[0][1]:ranges[1][1] + 1] = np.ones((ranges[1][0] + 1- ranges[0][0], ranges[1][1] + 1 - ranges[0][1]), dtype=bool)
        if "turn off" in line:
            grid[ranges[0][0]:ranges[1][0] + 1, ranges[0][1]:ranges[1][1] + 1] = np.zeros((ranges[1][0] + 1 - ranges[0][0], ranges[1][1] + 1 - ranges[0][1]), dtype=bool)
        if "toggle" in line:
            for i in range(ranges[0][0], ranges[1][0] + 1):
                for j in range(ranges[0][1], ranges[1][1] + 1):
                    grid[i, j] = not grid[i,j]
    print len( [element for line in grid for element in line if element == True])

def sixthDayB():
    f = open("day6.txt", 'r')
    grid = np.zeros((1000, 1000))
    for line in f:
        ranges = re.findall("\d+\d*", line)
        ranges = [(int(ranges[0]), int(ranges[1])), (int(ranges[2]), int(ranges[3]))]

        for i in range(ranges[0][0], ranges[1][0] + 1):
            for j in range(ranges[0][1], ranges[1][1] + 1):
                if "turn on" in line:
                    grid[i, j] += 1
                if "turn off" in line:
                    if grid[i,j] > 0:
                        grid[i, j] -= 1
                if "toggle" in line:
                    grid[i, j] += 2
    total = 0
    print np.sum(grid)


def negateAssignment(line, variables, evaluated, i):
    variable1 = line[1]
    variable2 = line[-1]
    if variable1 in variables:
        value = variables[variable1]
        variables[variable2] = ~value & 0xFFFF
        evaluated.append(i)
        print line


def andOrAssignment(line, variables, evaluated, i):
    variable1 = line[0]
    variable2 = line[2]
    variable3 = line[4]
    try:
        variable1 = int(variable1)
    except ValueError:
        pass
    try:
        variable2 = int(variable2)
    except ValueError:
        pass
    if variable1 in variables:
        variable1 = variables[variable1]
    if variable2 in variables:
        variable2 = variables[variable2]
    if type(variable1) == int and type(variable2) == int:
        if line[1] == "AND":
            variables[variable3] = (variable1 & variable2) & 0xFFFF
        else:
            variables[variable3] = (variable1 | variable2) & 0xFFFF
        evaluated.append(i)
        print line


def  shiftAssignment(line, variables, evaluated, i):
    variable1 = line[0]
    variable2 = line[2]
    variable3 = line[4]
    try:
        variable1 = int(variable1)
    except ValueError:
        pass
    try:
        variable2 = int(variable2)
    except ValueError:
        pass
    if variable1 in variables:
        variable1 = variables[variable1]
    if type(variable1) == int and type(variable2) == int:
        if line[1] == "LSHIFT":
            variables[variable3] = (variable1 << variable2) & 0xFFFF
        else:
            variables[variable3] = (variable1 >> variable2) & 0xFFFF
        evaluated.append(i)
        print line


def  assignment(line, variables, evaluated, i):
    variable1 = line[0]
    variable2 = line[2]
    try:
        variable1 = int(variable1)
    except ValueError:
        pass
    if variable1 in variables:
        variable1 = variables[variable1]
    if type(variable1) == int:
        variables[variable2] = variable1 
        evaluated.append(i)
        print line

def seventhDayA():
    variables = dict([])
    lines = 339
    evaluated = []
    while(len(evaluated) < lines):
        f = open("day7.txt", 'r')
        for i, l in enumerate(f):
            print i
            if i in evaluated:
                continue
            line = l.split()
            if "NOT" in line:
                negateAssignment(line, variables, evaluated, i)
            elif ("AND" in line) or ("OR" in line):
                andOrAssignment(line, variables, evaluated, i)
            elif ("LSHIFT" in line) or ("RSHIFT" in line):
                shiftAssignment(line, variables, evaluated, i)
            else:
                assignment(line, variables, evaluated, i)
    print variables['a']


def seventhDayB():
    variables = dict([])
    lines = 339
    evaluated = []
    while(len(evaluated) < lines):
        f = open("day7.txt", 'r')
        for i, l in enumerate(f):
            print i
            if i in evaluated:
                continue
            line = l.split()
            if "NOT" in line:
                negateAssignment(line, variables, evaluated, i)
            elif ("AND" in line) or ("OR" in line):
                andOrAssignment(line, variables, evaluated, i)
            elif ("LSHIFT" in line) or ("RSHIFT" in line):
                shiftAssignment(line, variables, evaluated, i)
            else:
                assignment(line, variables, evaluated, i)
    print variables['a']


def eigthDayA():
    f = open("day8.txt", 'r')
    totalStringCharacters = 0
    totalCharactersInMemory = 0
    for line in f:
        line = line.rstrip()
        totalStringCharacters += len(line)
        if len(line) > 2:
            stringInterpreted = line[1:-1]
            stringInterpreted = str(stringInterpreted).decode('string_escape')
            totalCharactersInMemory += len(stringInterpreted)
    print totalStringCharacters - totalCharactersInMemory

def eigthDayB():
    f = open("day8.txt", 'r')
    totalStringCharacters = 0
    totalCharactersEncoded = 0
    for line in f:
        line = line.rstrip()
        totalStringCharacters += len(line)
        print totalStringCharacters
        re.replace(line, "\\\\"", ")
        print re.findall('\\\\"', line)
        print re.findall('\\\\x', line)
        totalCharactersEncoded += len(line) + 4 + len(re.findall('\\\\"', line)) * 2 + len(re.findall('\\\\.', line))
        print totalCharactersEncoded
        print "\n"
    print totalCharactersEncoded - totalStringCharacters 

def getVisitableCities(visited, distances, allNodes):
    visitableCities = []
    for node in allNodes:
        if node not in visited and (visited[-1], node) in distances:
            visitableCities.append(node)
    return visitableCities

def shortestPath(current, distances, allNodes, bestCost, bestPath):
#    print "current path " + str(current[0])
#    print "current cost " + str(current[1])
#    print "current best cost + " + str(bestCost)
    if len(current[0]) == len(allNodes):
#        print "Finished path"
        return current[1]   , current[0]
    visableCities = getVisitableCities(current[0], distances, allNodes)
    if len(visableCities) == 0:
        return -1, []
    for city in visableCities:
#        print "add city " + city + "To current path " + str(current[0])
        newPath = copy.deepcopy(current[0])
        newPath.append(city)
#        print "newPath = " + str(newPath)
        newCost = current[1] + distances[(newPath[-2], city)]
        cost, path = shortestPath((newPath, newCost), distances, allNodes, bestCost, bestPath)
#        print " Returned value : " + str(cost)
        if cost < bestCost and cost > 0:
#            print "new best coth: " + str(cost)
            bestCost = cost
            bestPath = path
    return bestCost, path

def ninthDayA():
    f = open("day9.txt", 'r') 
    distances = dict([])
    allNodes = []
    for line in f:
        words = line.split(" ")
        distances[(words[0], words[2])] = int(words[4])
        distances[(words[2], words[0])] = int(words[4])
        if words[0] not in allNodes:
            allNodes.append(words[0])    
        if words[2] not in allNodes:
            allNodes.append(words[2])  
    currentPath = []
    bestPath = []
    bestCost = 9999
    for city in allNodes:
        print city
        cost, path = shortestPath(([city], 0), distances, allNodes, 9999, bestPath)
        if cost < bestCost and cost > 0:
            bestCost = cost
            bestPath = path
    print bestCost
    print bestPath

def longestPath(current, distances, allNodes, bestCost, bestPath):
    if len(current[0]) == len(allNodes):
        return current[1]   , current[0]
    visableCities = getVisitableCities(current[0], distances, allNodes)
    if len(visableCities) == 0:
        return -1, []
    for city in visableCities:
        newPath = copy.deepcopy(current[0])
        newPath.append(city)
        newCost = current[1] + distances[(newPath[-2], city)]
        cost, path = longestPath((newPath, newCost), distances, allNodes, bestCost, bestPath)
        if cost > bestCost and cost > 0:
            bestCost = cost
            bestPath = path
    return bestCost, path

def ninthDayB():
    f = open("day9.txt", 'r') 
    distances = dict([])
    allNodes = []
    for line in f:
        words = line.split(" ")
        distances[(words[0], words[2])] = int(words[4])
        distances[(words[2], words[0])] = int(words[4])
        if words[0] not in allNodes:
            allNodes.append(words[0])    
        if words[2] not in allNodes:
            allNodes.append(words[2])  
    currentPath = []
    bestPath = []
    bestCost = 0
    for city in allNodes:
        print city
        cost, path = longestPath(([city], 0), distances, allNodes, 0, bestPath)
        if cost > bestCost and cost > 0:
            bestCost = cost
            bestPath = path
    print bestCost
    print bestPath

def tenthDayA():
    sequence = '1321131112'
    counter = 0
    while counter < 50:
        currentCharacter = ""
        currentCharacterCount = 0
        newSequence = []
        for i in sequence:
            if currentCharacter == "":
                currentCharacter = i
                currentCharacterCount = 1
            elif i == currentCharacter:
                currentCharacterCount += 1
            else:
                newSequence.append(str(currentCharacterCount) + currentCharacter)
                currentCharacter = i
                currentCharacterCount = 1
        # make sure that the last characters are also put in the list
        newSequence.append(str(currentCharacterCount) + currentCharacter)
        sequence = "".join(newSequence)
        counter += 1
    print len(sequence)

def addOne(asciiValue):
    for i in range(len(asciiValue) - 1, -1, -1):
        if asciiValue[i] == 122:
            asciiValue[i] = 97
            if i == 0:
                addOne(asciiValue)
        else:
            asciiValue[i]  += 1
            break

def threeIncremental(asciiValue):
    for i in range(0, len(asciiValue) - 2):
        if(asciiValue[i + 1] - asciiValue[i] == 1):
            if(asciiValue[i + 2] - asciiValue[i + 1] == 1):
                return True
    return False

def twoPairs(string):
    pairs = re.findall("(\w)\\1.*(\w)\\2", string)
    for pair in pairs:
        if pair[0] is not pair[1]:
            return True
    return False

def eleventhDay():
    puzzleInput = "hepxxyzz"
    puzzleList  = list("")
    asciiValue = []
    for character in puzzleInput:
        asciiValue.append(ord(character))
    while (True):
        addOne(asciiValue)
        newString = ""
        for character in asciiValue:
            newString += chr(character)
        #check for each condition
        if threeIncremental(asciiValue):
            if len(re.findall('[iol]', newString)) == 0:
                if twoPairs(newString):
                    print newString
                    break

def twelthDayA():
    f = open("day12.txt", 'r') 
    total = 0
    for line in f:
        minusNumbers = [int(x) for x in re.findall("-\d+", line)]
        numbers = [int(x) for x in re.findall("[^-\d](\d+)", line)]
        print numbers
        print sum(minusNumbers)
        print sum(numbers)
        total += sum(minusNumbers) + sum(numbers)
    print total



def sumTreeIgnoringRed(data, s):
    print "\n"
    print data
    if type(data) == str or type(data) == unicode:
        return 0
    if type(data) == int:
        return data
    if type(data) == dict:
        keys = data.keys()
        if "red" in data.values():
            return 0
        for i in range(0, len(keys)):
            r = sumTreeIgnoringRed(data[keys[i]], 0)
            s +=  r
    if type(data) == list:
        for i in range(0, len(data)):
            r =  sumTreeIgnoringRed(data[i], 0)
            s += r
    return s

def twelthDayB():
    data_file = open('day12.txt')
    data = json.load(data_file)
    s = sumTreeIgnoringRed(data, 0)
    print s