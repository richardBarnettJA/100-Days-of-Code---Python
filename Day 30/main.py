# Error and Exceptions

try:
    file = open("a_file.txt")
    dict = {"key": "value"}
    print(dict["abc"])
except FileNotFoundError:
    open("a_file.txt", "w")
except KeyError as error_message:
    print(f"That key {error_message} does not exists")
else:
    print(dict["key"])
finally:
    print("prints no matter what")
    raise TypeError("This is an error I made up")