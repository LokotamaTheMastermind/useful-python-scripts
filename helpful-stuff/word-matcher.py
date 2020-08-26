import os
import time

value_1 = input("Enter the first value ># ")  # Comparison value 1
value_2 = input("Enter the second value ># ")  # Comparison value 2

"""

original -> params -> value_1
value -> params -> value_2

"""

def verify(original, other):
    if original == other:
        print("The two strings are the same!")
        time.sleep(5)  # Sets timer to sleep for 5 seconds
        os.system("cls")  # Clears the screen
    else:
        print("The two strings are not the same")

verify(value_1, value_2)  # Initializes the function
