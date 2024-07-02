# CSV

import csv
import pandas


with open("./weather_data.csv") as f:
    content = csv.reader(f)
    temperatures = []
    for c in content:
        print(c)
        if c[1] != "temp":
            temperatures.append(int(c[1]))
    print(temperatures)

data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(data["temp"])
# # OR
# print(data.temp)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# Create Dataframe from Scratch
data_dict = {
    "students": ["Amy", "Jill", "Fred"],
    "scores": [76, 56, 65]
}

data_2 = pandas.DataFrame(data_dict)
print(data_2)
data_2.to_csv("new_data.csv")