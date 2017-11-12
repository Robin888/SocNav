import numpy as np
from Move import Move_Object 

#note this depends on integration with the IO integration
#"moves" refers to the list of the 10 move objects returned by CogSciK
#the Move object has been modified to include a risk and probability

def assign_probabilities(moves):
	n = len(moves)
	mu = 1/n
	sigma = np.random.uniform()
	samples = np.random.normal(mu, sigma, n)
	for i in range(n):
		moves[i].probability = samples[i]

def calculate_risks(end_state, moves):
	distances = []
	for move in moves:
		distance = euclidean_distance(end_state, move.IO) 
		random_error = np.random.normal(0, 1)
		distance_errored = distance + random_error
		distances.append(distance_errored)
		move.risk = move.probability * distance_errored
	return distances

def resource_encoding(moves):
	''
	f = open("resource_vocab.txt", "r")
	resource_vocab = f.readlines()
	f.close()
	vocab_map_indices = {}
	n = len(resource_vocab)
	for move in moves:
		for i in range(n):
			vocab_map_indices[move[i]] = i
	for move in moves:
		one_hot = [0]*n
		for resource in move.resources["low"]:
			one_hot[vocab_map_indices[resource]] = 1
		for resource in move.resources["med"]:
			one_hot[vocab_map_indices[resource]] = 1
		for resource in move.resources["high"]:
			one_hot[vocab_map_indices[resource]] = 1
		move.one_hot = one_hot

def generate_resource_vocab(moves):
	resource_vocab = set()
	for move in moves:
		for resource in move.resources["low"]:
			resource_vocab.add(resource)
		for resource in move.resources["med"]:
			resource_vocab.add(resource)
		for resource in move.resources["high"]:
			resource_vocab.add(resource)
	f = open("resource_vocab.txt", "w")	
	for resource in resource_vocab:
		f.write(resource)
	f.close()

def euclidean_distance(a, b):
	distance = 0.0
	for i in xrange(0, len(a)):
		distance += np.linalg.norm(a[i] - b[i])
	return np.sqrt(distance)

if __name__ == "__main__":
	generate_resource_vocab(moves)