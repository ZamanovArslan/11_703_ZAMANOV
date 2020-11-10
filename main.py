import pandas as pd
import matplotlib.pyplot as plt


def draw(dataset):
    numb = list(data.PassengerId)
    p_class = list(dataset.Pclass)
    ages = list(dataset.Age)
    colors = []

    for i in range(0, len(numb)):
        if p_class[i] == 1:
            colors.append('r')
        elif p_class[i] == 2:
            colors.append('g')
        else:
            colors.append('b')

    fig, ax = plt.subplots()
    ax.bar(numb, ages, color=colors)
    plt.show()


data = pd.read_csv("titanic/test.csv")
draw(data)
