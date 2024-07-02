#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as f:
    content = f.readlines()
    for name in content:
        n = name.strip()
        names.append(n)

letter = []
with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.readlines()
    print(letter)

for name in names:
    head = letter[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(head)
        f.writelines(letter[1:])
