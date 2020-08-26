print("")
value_1 = int(input("What is the first cost price -> "))
print("")
value_2 = int(input("What is the first selling price -> "))

def main(cost_price, selling_price):
    print("")
    question = input("Did you get a profile or loss? |> ")
    if question == "profit":
        profit(value_1, value_2)
    elif question == "loss":
        loss(value_1, value_2)
    else:
        exit()

def profit(cost_price, selling_price):
    profit = selling_price - cost_price
    print("")
    print(f"Your profit is ->₦{profit}")

def loss(cost_price, selling_price):
    loss = cost_price - selling_price
    print("")
    print(f"Your loss is ->₦{loss}")

main(value_1, value_2)
