import copy

inputVal = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
test = "0	2	7	0"
blockArray = inputVal.split("\t")

blocks = []

for index in range(len(blockArray)):
	blocks.append(int(blockArray[index]))

def getIndexDiff(blocks, states, steps):
	firstOccurenceIndex = 0
	for index in range(len(states)):
		if (states[index] == blocks):
			firstOccurenceIndex = index

	return steps - firstOccurenceIndex

def getAllocationSteps(blocks):
	step = 0
	states = []

	while blocks not in states:
		states.append(copy.deepcopy(blocks))
		reAllocate(blocks)
		step += 1

	double = 0
	for index in range(len(states)):
		if (states[index] == blocks):
			double = index

	cyclesUntilReoccurence = getIndexDiff(blocks, states, step)
	return [step, cyclesUntilReoccurence]

def reAllocate(blocks):
	highest = getHighest(blocks)
	highestIndex = highest["index"]
	highestAmount = highest["val"]

	blocks[highestIndex] = 0
	pointer = highestIndex + 1
	while highestAmount > 0:
		currentIndex = pointer % len(blocks)
		blocks[currentIndex] = int(blocks[currentIndex]) + 1
		highestAmount -= 1
		pointer += 1

	return blocks


def getHighest(blocks):
	highest = {"val": 0, "index": 0}
	for index in range(len(blocks)):
		if blocks[index] > highest["val"]:
			highest["val"] = int(blocks[index])
			highest["index"] = index

	return highest

print getAllocationSteps(blocks)
