# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# Self closing
with open("my_file.txt", "a") as f:
    # content = f.read()
    # print(content)
    f.write("\nSup")