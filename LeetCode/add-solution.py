import os
import sys


"""
Usage: python add-solution.py solution-number-1 solution-number-2 ...
Note: Solution number is a 4-digit number with leading 0s, e.g. 0001, 0002, etc
"""

if len(sys.argv) == 1:
    print('Please specify the solution number first!')
    exit(1)


"""
Get the legal solution number and path list
"""

# The LeetCode solution folder is under the current direcotry
leetcode_dir = 'LeetCode' 

def get_new_solution_path_list():
    solution_number_list = sorted(sys.argv[1:])
    new_solution_path_list = []
    for num in solution_number_list:
        if not num.isnumeric():
            print(f'The solution numebr {num} souble be integer.')
            exit(2)

    index = 0
    for dir_name in os.listdir(leetcode_dir):
        num = solution_number_list[index]
        if dir_name.startswith(num):
            check = input(f"Are you sure to add the solution '{dir_name}'? (Y/N)")
            if check.lower() == 'n':
                print(f"Skip the solution '{dir_name}'.\n")
                continue
            else:
                print(f"Add the solution '{dir_name}'.\n")
            solution_path = os.path.join(leetcode_dir, dir_name)
            new_solution_path_list.append((num, solution_path))
            index += 1

        if index >= len(solution_number_list):
            break

    if index < len(solution_number_list):
        check = input(f"Here is no solution numebr {solution_number_list[index:]}, continue or not? (Y/N)")
        if check.lower() == 'n':
            print("Terminal the program.")
            os.exit(0)
        print()

    return new_solution_path_list



"""
Add the solution list to remote
"""

soltuion_path_list = get_new_solution_path_list()

def upload_command(file_path, message):
    print("==>", message, '<==')
    os.system(f'git add "{file_path}"')
    os.system(f'git commit -m "{message}"')
    os.system('git push')
    print()

for num, solution_path in soltuion_path_list:
    for filename in os.listdir(solution_path):
        file_path = os.path.join(solution_path, filename)
        if filename.endswith("md"):
            upload_command(file_path, f":memo: upload #{num} README")
        elif filename.endswith("cpp"):
            upload_command(file_path, f":sparkles: upload #{num} cpp solution")
        elif filename.endswith("py"):
            upload_command(file_path, f":sparkles: upload #{num} python solution")
        elif filename.endswith("go"):
            upload_command(file_path, f":sparkles: upload #{num} golang solution")


"""
Update the LeetCode.md
"""

check = input("Update the 'LeetCode.md' or not? (Y/N)")

if check.lower() == 'n':
    print(f"The LeetCode soltion number {num} has been uploaded, but the 'LeetCode.md' has not been updated")
else:
    print("==>", "Update the LeetCode list", "<==")
    os.system("python LeetCode\generate_leetcode_list.py")
    os.system("git add LeetCode.md")
    os.system(f'git commit -m ":memo: add solution number {sys.argv[1:]}"')
    os.system('git push')
