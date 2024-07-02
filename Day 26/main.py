# List comprehension

numbers = [1,2,3,4,5]
new_list = [x+1 for x in numbers]
print(new_list)

# works with strings as well
letters = [x for x in "Richard"]
print(letters)


db_list = [i*2 for i in range(1,5)]
print(db_list)




# Conditional List Comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
names_list = [name.upper() for name in names if len(name) >= 60]
print(names_list)


import random
# Dictionary Comprehension
new_dict = {student:random.randint(1, 100) for student in names}
print(new_dict)

passed_students = {key:value for (key, value) in new_dict.items() if value>50}
print(passed_students)


import pandas
# Loop through pandas dataframe

data_dict = {
    "students": ["Amy", "Jill", "Fred"],
    "scores": [76, 56, 65]
}
df = pandas.DataFrame(data_dict)

for (index, row) in df.iterrows():
    print(row)
    print(index)
    print(row.students)