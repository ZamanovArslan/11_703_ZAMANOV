import numpy as np
import matplotlib.pyplot as plt
from random import randrange

X = np.empty((0, 2), int)
for i in range(30):
    for j in range(30):
        element = np.array([[i, j]])
        X = np.append(X, element, axis=0)
color_list = np.array(['red', 'blue', 'green', 'yellow', '#377eb8', '#4daf4a', 'gray'])


class K_Means():
    def __init__(self, dataset, n_clusters=3, method_id=1):
        self.dataset = dataset
        self.n_clusters = n_clusters
        self.max_n_inter = 100
        self.tolerance = .01  # минимальное движение центров кластеров
        self.fitted = False
        self.labels = np.array([])
        self.method_id = method_id
        self.centroids = np.empty((0, 2), int)
        self.randomize_centroids()

    def randomize_centroids(self):
        i = 0
        while i < self.n_clusters:
            random_element = np.array([self.get_random_centroid()])
            if random_element not in self.centroids:
                self.centroids = np.append(self.centroids, random_element, axis=0)
                i += 1

    def get_random_centroid(self):
        x = randrange(min(self.dataset[:, 0]), max(self.dataset[:, 0]))
        y = randrange(min(self.dataset[:, 1]), max(self.dataset[:, 1]))
        centroid = np.array([x, y])
        return (centroid)

    def get_dist(self, list1, list2, method_id):
        if method_id == 1:
            return np.sqrt(sum((i - j) ** 2 for i, j in zip(list1, list2)))
        elif method_id == 2:
            return sum((i - j) ** 2 for i, j in zip(list1, list2))
        elif method_id == 3:
            return sum(abs(i - j) for i, j in zip(list1, list2))
        elif method_id == 4:
            return max(abs(i - j) for i, j in zip(list1, list2))

    def distribute_data(self):
        self.labels = np.array([])
        for elem in self.dataset:
            dist = [self.get_dist(elem, center, self.method_id) for center in self.centroids]
            self.labels = np.append(self.labels, [dist.index(min(dist))]).astype(int)

    def recalculate_centroids(self):
        for i in range(self.n_clusters):
            num = 0
            temp = np.zeros(len(self.dataset[0]))
            for k, label in enumerate(self.labels):
                if label == i:
                    num += 1
                    temp += self.dataset[k]
            self.centroids[i] = temp / num

    def fit(self):
        iter = 1
        while iter < self.max_n_inter:
            prev_centroids = np.copy(self.centroids)
            self.distribute_data()
            self.recalculate_centroids()
            if max([self.get_dist(i, j, self.method_id) for i, j in
                    zip(prev_centroids, self.centroids)]) < self.tolerance:
                break
        self.fitted = True

    def predict(self, dataset):
        labels = np.array([])
        for elem in dataset:
            dist = [self.get_dist(elem, center, self.method_id) for center in self.centroids]
            labels = np.append(labels, [dist.index(min(dist))]).astype(int)
        return labels


kmeans = K_Means(X, 7)
kmeans.fit()
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=color_list[kmeans.labels])
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='black', marker='p')
plt.show()
labels = kmeans.predict(X)
print(labels)
