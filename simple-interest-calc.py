""" Comments

Formula -> (Simple Interest)
----------------------------

P * R * T
---------
   100

"""

print("")
value_1 = int(input("Please what is the principal ->₦"))
print("")
value_2 = int(input("Please what is the rate ->%"))
print("")
value_3 = int(input("Please what is the time ->yrs"))


def calculate(principal, rate, time):
    print("")

    interest = principal * rate * time / 100

    print(f"The simple interest is ->₦{interest}")

    question = input("Do you want to find the amount? |> ")

    if question == "y" or "yes":
        amount = principal + interest
        print("")
        print(f"The amount of the simple interest is ->₦{amount}")
    else:
        print("")

calculate(value_1, value_2, value_3)
