import os
import time
import pandas

while True:
    if os.path.exists("Pandas/temps.csv"):
        data = pandas.read_csv("Pandas/temps.csv")
        print(data.mean())
        # To print mean of column: print(data.mean()["str1"])
    else:
        print("File not exist")
    time.sleep(10)

