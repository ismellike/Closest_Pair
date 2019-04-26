import sys
import math

def distance(p1, p2):
	return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

def closest_pair(points):
	#sort points by x axis and y axis
	#python uses timsort Avg = O(nlogn)
	Px = sorted(points, key = lambda p: p[0])
	Py = sorted(points, key = lambda p: p[1])
	return closest_pair_xy(Px, Py)

def closest_pair_xy(Px, Py):
	N = len(Px)
	if N <= 3: #px and py lengths are the same
		lowest = math.inf
		index = 0
		for i in range(0, N):
			d = distance(Px[i], Px[(i+1) % N])
			if(d < lowest):
				lowest = d
				index = i
		return (Px[index], Px[(index+1)%N])

	#construct Q and R
	xBar = Px[math.ceil(N/2)]
	Qx, Qy, Rx, Ry = [], [], [], []
	for i in range(0, N):
		if Px[i] < xBar:
			Qx.append(Px[i])
		else:
			Rx.append(Px[i])
	Qy = sorted(Qx, key = lambda p: p[1])
	Ry = sorted(Rx, key = lambda p: p[1])

	#use Q and R
	(q0, q1) = closest_pair_xy(Qx, Qy)
	(r0, r1) = closest_pair_xy(Rx, Ry)

	#find delta
	delta = min([distance(q0, q1), distance(r0, r1)])

	#find max x coord in set Q
	xStar = Qx[-1][0]

	#construct S acting as Sy
	S = []
	for i in range(0, N):
		#simulate a line with xStar
		if distance((xStar, Py[i][1]), Py[i]) < delta:
			S.append(Py[i])

	#find distances to next 15
	minS = math.inf
	s, sPrime = None, None
	N = len(S)
	for i in range(0, N):
		for j in range(1, min([15, N])):
			d = distance(S[i], S[(i+j)%N])
			if d < minS:
				minS = d
				s = S[i]
				sPrime = S[(i+j)%N]

	#return result
	if(minS < delta):
		return (s, sPrime)
	if distance(q0, q1) < distance(r0, r1):
		return (q0, q1)
	return (r0, r1)

def read_file(path):
	nodes = []
	with open(path, "r") as file:
		for line in file.readlines():
			x = float(line.split()[0])
			y = float(line.split()[1])
			nodes.append((x,y))
	return nodes

def main():
	if(len(sys.argv) < 2):
		print("Usage: python closest_pair_2836796.py input > output")
		exit()
	points = read_file(sys.argv[1])
	pair = closest_pair(points)
	for point in pair:
		print(str(point[0])+' '+str(point[1]))

if __name__ == "__main__":
	main()