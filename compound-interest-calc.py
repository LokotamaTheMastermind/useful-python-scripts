value_1 = int(input("Please what is the intial principal ->₦"))
value_2 = int(input("Please what is the rate ->%"))
value_3 = int(input("How long do you want to watch the principal ->yrs"))

def calculate(principal, rate, time):
    interest_1 = principal * rate * time / 100
    how_long = time
    temp = list(how_long)
    print(temp)
    # for var in how_long:
    #     temp = principal * rate * time / 100
    #     print(f"Interest for the year {var} is {temp}")

calculate(value_1, value_2, value_3)
