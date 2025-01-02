from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
print("Please wait while the code is being executed...")
#1.2.1
image1 = Image.open('image1.png')
image2 = Image.open('image2.png')
image1_np = np.array(image1)
image2_np = np.array(image2)

image1_2D = image1_np.reshape(-1, 3)
image2_2D = image2_np.reshape(-1, 3)
image1_2D.shape
#I have commented it out since it takes a long time to run and we had to ditermine the k manually
# wcss = []
# K = range(1, 15)
# print("Finding optimal k using the Elbow Method...")
# for k in K:
#     kmeans = KMeans(n_clusters=k, n_init=10)
#     kmeans.fit(image1_2D)
#     wcss.append(kmeans.inertia_)
    
# plt.plot(K, wcss, 'bx-')
# plt.xlabel('Number of clusters(k)')
# plt.ylabel('wcss')
# plt.title('Elbow Method for Optimal k')
# plt.show()


optimal_k = 4 
print(f"Optimal k found: {optimal_k}. Applying K-means to compress image1...")
kmeans = KMeans(n_clusters=optimal_k, n_init=10)
kmeans.fit(image1_2D)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

image1_done = centroids[labels].reshape(image1_np.shape).astype(np.uint8)


Image.fromarray(image1_done).save('image1_done.png')
print("image1_done is ready to be viewed!")
#1.2.2
print("Applying KNN to recolor image2 using the centroids from image1...")
knn = NearestNeighbors(n_neighbors=1)
knn.fit(centroids)

_, labels_2 = knn.kneighbors(image2_2D)

image2_done = centroids[labels_2].reshape(image2_np.shape).astype(np.uint8)


Image.fromarray(image2_done).save('image2_done.png')
print("image2_done is ready to be viewed!")