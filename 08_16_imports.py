# Method 1: Importing the whole module
import utilities

def main():
    result1 = utilities.square(4)
    print(f"Using import module_name: The square of 4 is {result1}")

# Method 2: Importing a specific function
from utilities import square

def main_specific():
    result2 = square(5)
    print(f"Using from module_name import function_name: The square of 5 is {result2}")

# Method 3: Importing with an alias
from utilities import square as sq

def main_alias():
    result3 = sq(6)
    print(f"Using from module_name import function_name as fn: The square of 6 is {result3}")

# Method 4: Importing the module with an alias
import utilities as util

def main_alias_module():
    result4 = util.square(7)
    print(f"Using import module_name as mn: The square of 7 is {result4}")

# Calling all methods
if __name__ == "__main__":
    main()
    main_specific()
    main_alias()
    main_alias_module()





