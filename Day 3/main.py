num = 3
if num > 2:
    print("large")
else:
    print("small")



# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")



print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
cname = name1 + name2
lname = cname.lower()
T = int(lname.count("t"))
R = int(lname.count("r"))
U = int(lname.count("u"))
E = int(lname.count("e"))
l = int(lname.count("l"))
o = int(lname.count("o"))
v = int(lname.count("v"))
e = int(lname.count("e"))
total = ((T + R + U + E) * 10) + l + o + v + e

if (total < 10 or total > 90):
  print(f"Your score is {total}, you go together like coke and mentos.")
elif (total > 40 and total < 50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")