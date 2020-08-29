"""

original -> params -> value_1
value -> params -> value_2

"""

try:
    while 1:
        def verify(original, other):
            import os, time
            if original == other:
                print("The two strings are the same!")
                time.sleep(5)  # Sets timer to sleep for 5 seconds
                os.system("cls")  # Clears the screen
            else:
                import time, os, platform
                time.sleep(2)
                op = platform.system()

                if op == "Windows":
                    os.system("cls")
                elif op == "Linux" or op == "Darwin":
                    os.system("clear")
                else:
                    print("Couldn't find system type")

                print("\nThe two strings are not the same")

        print("")
        value_1 = input("Enter the first value ># ")  # Comparison value 1
        print("")
        value_2 = input("Enter the second value ># ")  # Comparison value 2

        verify(value_1, value_2)  # Initializes the function
except KeyboardInterrupt:
    import time
    print("\n\nQuitting console ...")
    time.sleep(3)
