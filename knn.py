import random
import math
import pylab as pl
import numpy as np
from matplotlib.colors import listed_colormap


def gen_points(number_of_class_el, number_of_classes):
    data = []
    for class_num in range(number_of_classes):
        center_x, center_y = random.random() * 5.0, random.random() * 5.0
        for row_num in range(number_of_class_el):
            data.append([[random.gauss(center_x, 0.5), random.gauss(center_y, 0.5)], class_num])
    return data


def show_data(classes, items_in_class):
    train_data = gen_points(items_in_class, classes)
    class_colormap = listed_colormap(['red', 'blue', 'green'])
    pl.scatter([train_data[i][0][0] for i in range(len(train_data))],
               [train_data[i][0][1] for i in range(len(train_data))],
               c=[train_data[i][1] for i in range(len(train_data))],
               cmap=class_colormap)
    pl.show()


def clastKNN(train_data, test_data, k, number_of_classes):
    def dist(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    test_labels = []
    for test_point in test_data:
        test_dist = [[dist(test_point, train_data[i][0]), train_data[i][1]] for i in range(len(train_data))]
        stat = [0 for i in range(number_of_classes)]
        for d in sorted(test_dist)[0:k]:
            stat[d[1]] += 1
        test_labels.append(sorted(zip(stat, range(number_of_classes)), reverse=True)[0][1])
    return test_labels


def show_data_on_class(classes, items_in_class, k):
    def generate_test_mesh(train_data):
        x = []
        y = []
        for i in range(len(train_data)):
            x.append(train_data[i][0][0])
            y.append(train_data[i][0][1])

        x_min = min(x)
        x_max = max(x)-min(x)
        y_min = min(y)
        y_max = max(y)-min(y)
        new_X, new_Y = np.meshgrid(np.arange(x_min, x_max),
                                   np.arange(y_min, y_max))
        return [new_X, new_Y]

    train_data = gen_points(items_in_class, classes)
    test_mesh = generate_test_mesh(train_data)
    test_mesh_labels = clastKNN(train_data, zip(test_mesh[0].ravel(), test_mesh[1].ravel()), k, classes)
    class_colormap = listed_colormap(['red', 'blue', 'green'])
    test_colormap = listed_colormap(['grey', 'black', 'yellow'])

    pl.pcolormesh(test_mesh[0],
                  test_mesh[1],
                  np.asarray(test_mesh_labels).reshape(test_mesh[0].shape),
                  cmap=test_colormap)
    pl.scatter([train_data[i][0][0] for i in range(len(train_data))],
               [train_data[i][0][1] for i in range(len(train_data))],
               c=[train_data[i][1] for i in range(len(train_data))],
               cmap=class_colormap)
    pl.show()


show_data(4, 20)
show_data_on_class(4, 20, 4)
