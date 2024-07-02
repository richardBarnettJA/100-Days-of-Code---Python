import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")


nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}



is_num = True
while is_num:
    try:
        word = input("Enter a word: ").upper()
        word_dict = [nato_dict[x] for x in word]
    except KeyError:
        print("Sorry, only letters in the alpahabet please.")
    else:
        is_num = False
print(word_dict)