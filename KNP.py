import numpy as np
import matplotlib.pyplot as plt
import networkx as nw


def first_connection():
    minim = matrix[0][1]
    i_min, j_min = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if minim > matrix[i][j]:
                minim = matrix[i][j]
                i_min, j_min = i, j
    connection[i_min][j_min] = connection[j_min][i_min] = 1
    connection[i_min][i_min] = connection[j_min][j_min] = -1


def connect_all():
    minim = None
    i_min, j_min = 0, 1
    for i in range(n):
        if connection[i][i] == -1:
            for j in range(n):
                if connection[j][j] == 0:
                    if (minim == None or minim > connection[i][j]):
                        minim = connection[i][j]
                        i_min, j_min = i, j
    connection[i_min][j_min] = connection[j_min][i_min] = 1
    connection[i_min][i_min] = connection[j_min][j_min] = -1


def delete_connection():
    maxim = 0
    i_max, j_max = -1, -1
    for i in range(n):
        for j in range(i + 1, n):
            if connection[i][j] == 1:
                if matrix[i][j] > maxim:
                    maxim = matrix[i][j]
                    i_max, j_max = i, j
    connection[i_max][j_max] = 0
    connection[j_max][i_max] = 0


n, k = 5, 2
matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = matrix[j][i] = np.random.randint(1, 100)
print(matrix)
connection = np.zeros((n, n))
first_connection()
for i in range(n - 2):
    connect_all()
for i in range(k - 1):
    delete_connection()

print("мин ост дер")
print(connection)
G = nw.from_numpy_matrix(matrix, create_using=nw.DiGraph)
layout = nw.spring_layout(G)
nw.draw(G, layout)
nw.draw_networkx_edge_labels(G, pos=layout)
plt.show()

new_graph = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if connection[i][j] != -1:
            new_graph[i][j] = connection[i][j] * matrix[i][j]
        else:
            new_graph[i][j] = -1
print(new_graph)
G = nw.from_numpy_matrix(new_graph, create_using=nw.DiGraph)
pos = nw.spring_layout(G)
nw.draw(G, pos)
nw.draw_networkx_edge_labels(G, pos=pos)
plt.show()
