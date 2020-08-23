""" Comments

Formula -> (Simple Interest)
----------------------------

P * R * T
---------
   100

"""

print("")
value_1 = input("Please what is the principal ->₦")

confirm_1 = value_1.isdigit()

if confirm_1:
    int(value_1)

print("")
value_2 = input("Please what is the rate ->%")

confirm_2 = value_2.isdigit()

if confirm_2:
    int(value_2)

print("")
value_3 = input("Please what is the time ->yrs")

confirm_3 = value_3.isdigit()

if confirm_3:
    int(value_3)


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


def show_solving_template():
    import os
    solving_template = """
    Formula = P * R * T
              ---------
                  100

    Interest = P * R * T
               ---------
                   100
    """
    command_1 = f"cd results"
    os.system(command_1)


if value_1 == "skip" or value_2 == "skip" or value_3 == "skip":
    show_solving_template()

else:
    calculate(value_1, value_2, value_3)
