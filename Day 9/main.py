#Dictionaries
p_dict = {
    "Bug": "Rocah",
    "Animal": "Snake",
    "Name": "Richard",
    1: "One"
}

print(p_dict[1])
p_dict[1] = 1
print(p_dict[1])

for x in p_dict:
    print(x)  #prints all keys