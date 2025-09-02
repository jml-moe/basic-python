import pandas as pd

with open("data.csv", "r") as file:
    # print(file.read()) -> tanpa pandas
    csv = pd.read_csv(file)
    print(csv)