import numpy as np

#calculate euclidean distance
def euclidean_distance(a,b):
	return np.sqrt(np.dot(b-a,b-a))

#Assign cluster to all the points 
def assign_clusters(points, centroids):
	clusters=[]
	distances =[]

	for p in points:
		for c in centroids:
			distances.append(euclidean_distance(p,c))
		min_distance=min(distances)
		clusters.append(distances.index(min_distance))
		distances.clear()
	return np.array(clusters)

#make new centroids using mean of clusters
def move_centroids(cluster, points,k):
	centroids=[]
	for t in range(k):
		centroids.append(points[cluster==t].mean(axis=0))
	return np.array(centroids)

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:

	points = np.array(points)
	initial_centroids = np.array(initial_centroids)

	new_centroids=initial_centroids
	for i in range(max_iterations):
		#assign clusters
		old_centroids = new_centroids
		clusters = assign_clusters(points,new_centroids)

		#move centroids
		new_centroids = move_centroids(clusters, points,k)


		#check for end condition
		if (old_centroids==new_centroids).all():
			break
		new_centroids = np.round(new_centroids,4)
	return [tuple(centroids) for centroids in new_centroids]
