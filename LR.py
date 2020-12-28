import plotly.graph_objects as gro
import numpy as np
from sklearn.svm import SVC
from sklearn.cluster import KMeans

n = 100
x = np.random.randint(0, 100, n)
y = np.random.randint(0, 100, n)
z = np.random.randint(0, 100, n)
points = []
for i in range(n):
    points.append([x[i], y[i], z[i]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(points)
clusters = kmeans.labels_
colors = ['black'] * n
for i in range(n):
    if clusters[i] == 1:
        colors[i] = 'blue'

fig = gro.Figure(data=[gro.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=colors))])

# fig.show()

x_new = np.random.randint(0, 100)
y_new = np.random.randint(0, 100)
z_new = np.random.randint(0, 100)

points.append([x_new, y_new, z_new])

fig.add_trace(gro.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=colors)))

svc = SVC(kernel='linear')
svc.fit(points[:n], clusters)

zz = lambda x, y: (-svc.intercept_[0] - svc.coef_[0][0] * x - svc.coef_[0][1] * y) / svc.coef_[0][2]

tmp = np.linspace(0, 100, 50)
xx, yx = np.meshgrid(tmp, tmp)

fig.add_trace(gro.Surface(x=xx, y=yx, z=zz(xx, yx)))
fig.show()
