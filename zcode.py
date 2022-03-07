import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics 
import random

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)    
std = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print(mean)
print(std)

df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()

mean_sample2 = statistics.mean(data)
score = (mean - mean_sample2)/std

print(score)

