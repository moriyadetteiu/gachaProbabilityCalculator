import matplotlib
import matplotlib.pyplot as plt

def make_graph(probabilities: list):
    matplotlib.use('Agg')
    xAxis = []
    yAxis = []
    for index, probability in enumerate(probabilities):
        if (probability < 0.01) :
            continue;
        xAxis.append(index)
        yAxis.append(probability * 100)

    plt.plot(xAxis, yAxis, color = "blue", marker = "o", linewidth = 1)
    plt.grid(True)
    plt.savefig("/tmp/deliverable/result.png")
