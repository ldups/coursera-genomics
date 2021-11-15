f = open("dna2.fasta", "r")

sequenceDict = {}
def numSequences():
	for line in f:
		line = line.rstrip()
		if line.startswith(">"):
			words = line.split()
			identifier = (words[0])[1:]
			if identifier in sequenceDict:
				raise ValueError()
			sequenceDict[identifier] = ''
		else:
			stringStart = sequenceDict[identifier]
			newString = stringStart + line
			sequenceDict[identifier] = newString
	return(len(sequenceDict))


def findLongest():
	longestVal = 0
	longestKey = ''
	for key in sequenceDict:
		if len(sequenceDict[key]) > longestVal:
			longestVal = len(sequenceDict[key])
			longestKey = key
	return(longestKey, longestVal)
	

def listLengths():
	listLengths = []
	for val in sequenceDict.values():
		listLengths.append(len(val))

def findShortest():
	keys = list(sequenceDict.keys())
	minLength = len(sequenceDict[keys[0]])
	lowestKey = ''
	for key in sequenceDict:
		value = sequenceDict[key]
		if len(value) < minLength:
			minLength = len(value)
			lowestKey = key
	return(lowestKey, minLength)


def findORFS(sequence, frame):
	orfs = []
	orf = ''
	position = -1
	startindex = frame - 1
	addTo = False
	for i in range(startindex, len(sequence), 3):
		if i + 2 < len(sequence):
			codon = sequence[i: i + 3]
			if codon == 'ATG' and addTo == False:
				position = i
				addTo = True
				orf = codon
			elif codon in ['TAA', 'TAG', 'TGA'] and addTo == True:
				orf = orf + codon
				addTo = False
				if len(orf) > 6:
					orfs.append([orf, position])
			elif addTo == True:
				orf = orf + codon
		#if orf != '' and addTo == False:
				
	return(orfs)

def findLongestORF(frame, direction):
	if direction == 'forward':
		orfs = findAllOrfsForward(frame)
	else:
		orfs = findAllOrfsBack(frame)
	longestLen = 0
	longestKey = ''
	longestPos = -1
	for list in orfs:
		key = list[0]
		sequence = list[1]
		if len(sequence) > longestLen:
			longestLen = len(sequence)
			longestKey = key
			longestPos = list[2]
	return(longestKey, longestLen, longestPos)

def findLongestORFofSequence(direction, identifier):
	orfs = []

	if identifier in sequenceDict:
		sequence = sequenceDict[identifier]
	else:
		raise ValueError

	if direction == 'forward':
		for i in range(1, 4):
				orfs.append(findORFS(sequence, i))
	else:
		for i in range(1, 4):
				orfs.append(findORFS(sequence, i))
	longestLen = 0
	longestPos = -1
	longestFrame = -1
	for i in range(0, len(orfs)):
		frame = orfs[i]
		for orf in frame:
			sequence = orf[0]
			if len(sequence) > longestLen:
				longestLen = len(sequence)
				longestPos = orf[1]
				longestFrame = i
	return(longestLen, longestPos, longestFrame)

def findAllOrfsForward(frame):
	allOrfs = []
	for key in sequenceDict:
		list = findORFS(sequenceDict[key], frame)
		for item in list:
			position = item[1]
			orfs = item[0]
			if orfs != None:
				allOrfs.append([key, orfs, position])
	return allOrfs

def findAllOrfsBack(frame):
	allOrfs = []
	for key in sequenceDict:
		sequence = (sequenceDict[key])[::-1]
		orfs = findORFS(sequence, frame)
		if orfs != None:
			allOrfs.append([key, orfs])
	return allOrfs

def findShortestORF(frame, direction):
	if direction == 'forward':
		orfs = findAllOrfsForward(frame)
	else:
		orfs = findAllOrfsBack(frame)
	shortestLen = len(orfs[0][1])
	shortestKey = orfs[0][0]
	shortestPos = orfs[0][2]
	for orf in orfs:
		if len(orf[1]) < shortestLen:
			shortestLen = len(orf[1])
			shortestKey = orf[0]
			shortestPos = orf[2]
	return (shortestKey, shortestLen, shortestPos)

def findNumRepeatinSequence(identifier, repeat):
	sequence = sequenceDict[identifier]
	return sequence.count(repeat)

def findTotalNumRepeat(repeat):
	numRepeat = 0
	for key in sequenceDict:
		sequence = sequenceDict[key]
		numRepeat += sequence.count(repeat)
	return numRepeat

def findRepeats(sequence, length):
	repeats = []
	listRepeats = []
	for i in range(0, len(sequence)):
		if i + length < len(sequence):
			repeat = sequence[i: i + length]
		if repeat not in listRepeats:
			repeats.append([repeat, 1])
			listRepeats.append(repeat)
		else:
			repeats[listRepeats.index(repeat)][1] +=1
	return repeats

def findMostRepeatTotal(length):
	repeats = []
	repeatList = []
	for key in sequenceDict:
		repeats.append(findRepeats(sequenceDict[key], length))
	highestNum = 0
	mostRepeat = ''
	for repeat in repeats:
		if repeat not in repeatList:
			repeats.append([repeat, 1])
			repeatList.append(repeat)
		else:
			repeats[repeatList.index(repeat)][1] += 1
	return repeats


#print(findAllOrfsForward(1))
#print('longest ORF:',findLongestORF(3, 'forward'))
#print('shortest ORF:', findShortestORF(2, 'forward'))
#print(findORFS(sequenceDict['gi|142022655|gb|EQ086233.1|16'], 1))
#print(findORFS(sequenceDict['gi|142022655|gb|EQ086233.1|16'], 2))
#print(findORFS(sequenceDict['gi|142022655|gb|EQ086233.1|16'], 3))
numSequences()
#print(findLongestORFofSequence('forward', 'gi|142022655|gb|EQ086233.1|16'))

#print(findTotalNumRepeat('CATCGCC'))
#print(findTotalNumRepeat('GCGCGCA'))
#print(findTotalNumRepeat('CGCGCCG'))
#print(findTotalNumRepeat('TGCGCGC'))
#print(findRepeats(sequenceDict['gi|142022655|gb|EQ086233.1|16'], 6))

print(findMostRepeatTotal(2))



	

