import csv
import random

def generateRandomSteps(moves, numIterations = 1000):
	randomSteps = []
	randomMoves=[]
	for i in range(numIterations):
		randomMoves = []
		for move_level in moves:
			randomMoves.append(move_level[random.randint(0,len(move_level)-1)][random.randint(0, len(move_level[0])-1)])
		randomSteps.append(randomMoves)
	return randomSteps

def writeCSV(randomSteps, filename):
	with open(filename, "w") as csvf:
		writer = csv.writer(csvf)
		writer.writerows(randomSteps)

def findCounts(randomSteps):
	move_counts = {}
	step_counts = {}
	for steps in randomSteps:
		for step in steps:
			if step not in step_counts:
				step_counts[step] = 1
			else:
				step_counts[step] += 1
			parts = step.split("|")
			move = parts[1]
			if move not in move_counts:
				move_counts[move] = 1
			else:
				move_counts[move] += 1
	return step_counts, move_counts

def findProbabilities(step_counts, move_counts):
	step_probs = step_counts
	move_weights = findConditionalWeights(move_counts)
	for step,count in step_counts.iteritems():
		move = step.split("|")[1]
		if move in move_counts: 
			step_probs[step] = float(count)/move_counts[move] * move_weights[move]
	return step_probs

def findConditionalWeights(move_counts):
	move_weights = {}
	layer_counts = {}
	for move in move_counts:
		layer = move[:2]
		if layer not in layer_counts:
			layer_counts[layer] = 1
		else:
			layer_counts[layer] += 1
	for move in move_counts:
		layer = move[:2]
		move_weights[move] = 1.0 / layer_counts[layer]
	print move_weights
	return move_weights


def formattedPrint(dic):
	lst = []
	for key,value in dic.iteritems():
		lst.append(list((key,value)))
	sortlst = sorted(lst, key=lambda x: x[0].split("|")[1])
	for l in sortlst:
		print l[0],":",l[1]
	return l
	


if __name__ == "__main__":
	moves11 = ["s1|m11", "s2|m11", "s3|m11"]
	moves12 = ["s1|m12", "s2|m12", "s3|m12"]
	moves21 = ["s1|m21", "s2|m21", "s3|m21"]
	moves = [[moves11, moves12], [moves21]]
	randomSteps = generateRandomSteps(moves)
	#writeCSV(randomSteps, "randomsteps.csv")
	step_counts, move_counts = findCounts(randomSteps)
	formattedPrint(findProbabilities(step_counts, move_counts))
