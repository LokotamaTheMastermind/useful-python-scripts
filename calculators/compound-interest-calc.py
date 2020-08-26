print("")
value_1 = int(input("Please what is the intial principal ->₦"))
print("")
value_2 = int(input("Please what is the rate ->%"))
print("")
value_3 = int(input("How long do you want to watch the principal ->yrs"))
print("")

def calculate(principal, rate, time):
    interest = principal * rate * time / 100

    how_long = time

    val = range(how_long + 1)[1:]

    for var in val:
        solution = interest + principal * rate * time / 100
        solution += solution
        print(f"\nInterest for the year {var} is {solution}")

calculate(value_1, value_2, value_3)
