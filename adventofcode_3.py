import math
import copy

### Attention! This code is extremely bad and was not intended to be fast or nice to read :D

inputVal = 368078

blocks = []

directions = ['right', 'top', 'left', 'bottom']

currentBlock = {'coordinates': [0, 0], 'value': 1}
blockRadius = 0
blockDiameter = 1
blockMaxIndex = 1
currentDirectionIndex = 0

valueLargerThenInput = 0

def getBlockValueByPos(x, y):
	for index in range(len(blocks)):
		coords = blocks[index]['coordinates']
		if coords[0] == x and coords[1] == y:
			return blocks[index]['value']
	return 0

for index in range(inputVal):
	currentCoords = currentBlock['coordinates']

	if index > 0 and valueLargerThenInput == 0:
		# get new value through neighbours
		x = currentCoords[0]
		y = currentCoords[1]
		nb1 = getBlockValueByPos(x + 1, y)
		nb2 = getBlockValueByPos(x + 1, y + 1)
		nb3 = getBlockValueByPos(x, y + 1)
		nb4 = getBlockValueByPos(x + 1, y - 1)
		nb5 = getBlockValueByPos(x - 1 , y + 1)
		nb6 = getBlockValueByPos(x - 1 , y - 1)
		nb7 = getBlockValueByPos(x - 1 , y)
		nb8 = getBlockValueByPos(x, y - 1)

		value = nb1 + nb2 + nb3 + nb4 + nb5 + nb6 + nb7 + nb8
		if value > inputVal:
			valueLargerThenInput = value

		currentBlock['value'] = value

	# add block to array
	blocks.append(copy.deepcopy(currentBlock))
	blockNumber = index + 1

	currentAbsX = abs(currentCoords[0])
	currentAbsY = abs(currentCoords[1])

	# turn top; we are on number 2
	if currentCoords[0] == 1 and currentCoords[1] == 0:
		currentDirectionIndex = 1
	else:
		# every corner except we're leaving current Radius
		if (blockNumber != blockMaxIndex):
			# we're at the most left or most right side of the current radius
			if (currentAbsX == blockRadius and (currentDirectionIndex != 1 and currentDirectionIndex != 3)):
				currentDirectionIndex = (currentDirectionIndex + 1) % 4
			elif (currentAbsY == blockRadius and (currentDirectionIndex != 0 and currentDirectionIndex != 2)):
				currentDirectionIndex = (currentDirectionIndex + 1) % 4

	currentDirection = directions[currentDirectionIndex]
	if (currentDirection == 'right'):
		currentCoords[0] = currentCoords[0] + 1
	elif (currentDirection == 'top'):
		currentCoords[1] = currentCoords[1] + 1
	elif (currentDirection == 'left'):
		currentCoords[0] = currentCoords[0] - 1
	elif(currentDirection == 'bottom'):
		currentCoords[1] = currentCoords[1] - 1

	if (blockNumber >= blockMaxIndex):
		blockDiameter += 2
		blockRadius += 1

	blockMaxIndex = int(math.pow(blockDiameter, 2))

def manhattanDistance(a, b):
	x1 = a[0]
	y1 = a[1]
	x2 = b[0]
	y2 = b[1]

	return abs(x1 - x2) + abs(y1 - y2)

print "Part 1: Distance from input Block to center: ", manhattanDistance(blocks[inputVal - 1]['coordinates'], blocks[0]['coordinates'])
print "Part 2: First Value larger than input: ", valueLargerThenInput
