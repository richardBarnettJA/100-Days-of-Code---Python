# 1. Describe the problem
# 2. Reproduce the bug
# 3. Pretend to be the computer
# 4. Fixing Errors (Highlighted Lines)
# 5. Use print statements to squash bugs
# 6. Use a debugger
# 7. Take a Break
# 8. Ask a friend
# 9. Run your code often
# 10. Stackoverflow

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])