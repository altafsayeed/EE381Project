import numpy as np
from matplotlib import pyplot as plt
from matplotlib import axes as ax

fname = 'sales.csv'
data = np.loadtxt(fname, delimiter=',', skiprows=1)
np.set_printoptions(suppress=True)

years = []
means = []
stds = []
housesSoldPerYear200_300 = []
totalHousesSoldPerYear = []
prbs = []


def means_graph():
    for i in range(2001, 2021):
        years.append(str(i))
        means.append(np.mean(data[:, 1][np.where(data[:, 0] == i)]))

    plt.bar(years, means)
    plt.yticks(np.arange(0, 600000, 50000))

    plt.title("Mean Sale Prices per Year")
    plt.xlabel("Year")
    plt.ylabel("Mean Sale Price")
    plt.tight_layout()
    plt.show()


def stds_graph():
    for i in range(2001, 2021):
        years.append(str(i))
        stds.append(np.std(data[:, 1][np.where(data[:, 0] == i)]))

    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False, style='plain')

    plt.bar(years, stds)
    plt.yticks(np.arange(0, 6000000, 500000))
    plt.title("Std. Deviations of Sale Prices Per Year")
    plt.xlabel("Year")
    plt.ylabel("Standard Deviation")
    plt.tight_layout()
    plt.show()


def prb_graph():
    for i in range(2001, 2021):
        years.append(str(i))
        totalHousesSoldPerYear.append(len(data[np.where(data[:, 0] == i)]))
        housesSoldPerYear200_300.append(
            len(data[np.where(np.logical_and(data[:, 0] == i, (data[:, 1] <= 300000) & (data[:, 1] >= 200000)))]))

    for i in range(0, 20):
        prbs.append(housesSoldPerYear200_300[i] / totalHousesSoldPerYear[i])

    plt.bar(years, prbs)
    plt.yticks(np.arange(0, 0.30, 0.02))

    plt.title("Probability of Sale Price being between 200,000 and 300,000 Per Year")
    plt.xlabel("Year")
    plt.ylabel("Probability")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    choice = (
        input('Enter 1 for Yearly Means Graph, 2 for Yearly Standard Deviation Graph, or 3 for Probability Graph: '))
    if choice == '1':
        means_graph()
    elif choice == '2':
        stds_graph()
    elif choice == '3':
        prb_graph()
