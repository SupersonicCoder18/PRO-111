import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("Marks.csv")
data = df["Math_score"].to_list()

Mean = statistics.mean(data)
Stdev = statistics.stdev(data)

#print("Mean and Stdev of Population Data are {} and {} respectively".format(Mean, Stdev))

def RandomSetOfMean(counter):
    DataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        DataSet.append(value)
    mean = statistics.mean(DataSet)
    return mean

mean_list = []
for i in range(0, 1000):
    setOfMeans = RandomSetOfMean(100)
    mean_list.append(setOfMeans)

mean = statistics.mean(mean_list)

Stdev2 = statistics.stdev(mean_list)
#print("Mean of the sampling distribution is ", mean)

DataStd1Start, DataStd1End = Mean - Stdev2, Mean + Stdev2
DataStd2Start, DataStd2End = Mean - ( 2* Stdev), Mean + (2 * Stdev2)
DataStd3Start, DataStd3End = Mean - (3* Stdev2), Mean + (3* Stdev2)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [DataStd1Start, DataStd1Start], y = [0, 0.17], mode = "lines", name = "First Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [DataStd1End, DataStd1End], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [DataStd2Start, DataStd2Start], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [DataStd2End, DataStd2End], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [DataStd3Start, DataStd3Start], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [DataStd3End, DataStd3End], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation End"))
fig.show()

df = pd.read_csv("MarksData1.csv")
data = df["Math_score"].to_list()
Mean1 = statistics.mean(data)
print("Mean and of Sample1 is {}".format(Mean1))

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [Mean1, Mean1], y = [0, 0.17], mode = "lines", name = "Mean of Sampling Data"))
fig.add_trace(go.Scatter(x = [DataStd1End, DataStd1End], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.show()

df = pd.read_csv("MarksData2.csv")
data = df["Math_score"].to_list()
Mean2 = statistics.mean(data)
print("Mean and of Sample2 is {}".format(Mean2))

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [Mean2, Mean2], y = [0, 0.17], mode = "lines", name = "Mean of Sampling Data"))
fig.add_trace(go.Scatter(x = [DataStd1End, DataStd1End], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [DataStd2End, DataStd2End], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.show()

df = pd.read_csv("MarksData3.csv")
data = df["Math_score"].to_list()
Mean3 = statistics.mean(data)
print("Mean and of Sample3 is {}".format(Mean3))

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [Mean3, Mean3], y = [0, 0.17], mode = "lines", name = "Mean of Sampling Data"))
fig.add_trace(go.Scatter(x = [DataStd1End, DataStd1End], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [DataStd2End, DataStd2End], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [DataStd3End, DataStd3End], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation End"))
fig.show()

zscore3 = (Mean3 - mean)/Stdev2
print("Z-Score for Sample3 is ", zscore3)
zscore2 = (Mean2 - mean)/Stdev2
print("Z-Score for Sample2 is ", zscore2)
zscore1 = (Mean1 - mean)/Stdev2
print("Z-Score for Sample1 is ", zscore1)