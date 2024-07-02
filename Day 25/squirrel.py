import pandas

# Fur Color, Count

data = pandas.read_csv("./Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

fur_color_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, Cinnamon_squirrels, Black_squirrels]
}


new_data = pandas.DataFrame(fur_color_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")