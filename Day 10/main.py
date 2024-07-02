#functions with outputs

# def my_function():
#     return 3*2

# num = my_function()
# print(num)



def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    full_name = f_name + " " + l_name
    return(full_name)

name = format_name("RiCHard", "barnetT")
print(name)


# Docstrings - must be the first line after the declaration of function. 
# Text shows up when we call the function
def new_function():
    """This is my new function"""
    return "New Function"

new_function()