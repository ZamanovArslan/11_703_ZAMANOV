import matplotlib.pyplot as plt
import numpy as np

n = 100
x = [np.random.randint(1, n) for i in range(n)]
y = [np.random.randint(1, n) for i in range(n)]

x_average = np.mean(x)
y_average = np.mean(y)


def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cluster(x, y, x_cc, y_cc, k):
    clust = []
    for i in range(0, n):
        d = distance(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if distance(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = distance(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        clust.append(numb)
    return clust


def k_means(k):
    radius = 0
    for i in range(0, n):
        r = distance(x_average, y_average, x[i], y[i])
        if r > radius:
            radius = r

    x_cc = [radius * np.cos(2 * np.pi * i / k) + x_average for i in range(k)]
    y_cc = [radius * np.sin(2 * np.pi * i / k) + y_average for i in range(k)]

    clust = cluster(x, y, x_cc, y_cc, k)

    sum = 0
    for i in range(0, n):
        subsum = 0
        for k_count in range(0, k):
            if clust[i] == k_count:
                subsum += (x_cc[k_count] - x[i]) ** 2
        sum += subsum
    return sum


sums = []
min_k = 999998
for i in range(2, 8):
    sums.append(k_means(i))
for i in range(0, 6):
    if sums[i] < min_k:
        min_k = i

print("Sums:", sums)
print("Min sum:", min(sums))
print("with k:", min_k + 5)


def calculate_d(sums):
    d = 555555
    k_temp = 0
    sum = 0
    for i in range(1, 5):
        temp = (sums[i] - sums[i + 1]) / (sums[i - 1] - sums[i])
        if temp < d:
            d = temp
            k_temp = i
            sum = sums[i]
        print(temp)
    print("D:", d, ", k:", k_temp + 1, ", sum:", sum)


calculate_d(sums)
