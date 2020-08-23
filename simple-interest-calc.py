""" Comments

Formula -> (Simple Interest)
----------------------------

P * R * T
---------
   100

"""


def calculate(principal, rate, time):

    print("")

    interest = principal * rate * time / 100

    print(f"The simple interest is ->₦{interest}")

    question = input("Do you want to find the amount? |> ")

    if question == "y" or question == "yes":
        amount = principal + interest
        print("")
        print(f"The amount of the simple interest is ->₦{amount}")

    another_question = input("Do you want the solution |> ")

    if another_question == "yes" or another_question == "y":
        show_solving(principal, rate, time)


def show_solving(principal, rate, time):
    """
    Function for showing the solved equation in a ready to copy & paste solving-template in results/simple-interest-results.txt
    """
    name = """
    Formula = P * R * T
             -----------
                  100
    Interest = {} * {} * {}
               ------------
                   100
    I =
    """.format(principal, rate, time)
    print(name)


"""
Function for appending solving template to simple-interest-results.txt
"""


def show_solving_template():
    import time
    import os
    solving_template = """
    Formula = P * R * T
              ---------
                  100

    Interest = P * R * T
               ---------
                   100
    """

    filename_save = open(
        "results/simple-interest-results.txt", "w", encoding="utf-8")
    filename_save.write(f"{solving_template}")
    filename_save.close()

    print("Done appending the solving template to the path results/simple-interest-results.txt")
    time.sleep(3)
    print("Now opening file in Notepad ...")
    time.sleep(3)
    os.system("notepad results\\simple-interest-results.txt")
    time.sleep(2)


print("")
value_1 = input("Please what is the principal ->₦")

confirm_1 = value_1.isdigit()

if confirm_1:
    int(value_1)

if value_1 == " skip":
    show_solving_template()
    quit()


print("")
value_2 = input("Please what is the rate ->%")

confirm_2 = value_2.isdigit()

if confirm_2:
    int(value_2)

if value_2 == " skip":
    show_solving_template()
    quit()


print("")
value_3 = input("Please what is the time ->yrs")

confirm_3 = value_3.isdigit()

if confirm_3:
    int(value_3)

if value_3 == " skip":
    show_solving_template()
    quit()
else:
    calculate(confirm_1, confirm_2, confirm_3)
