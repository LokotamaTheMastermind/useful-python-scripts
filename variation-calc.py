def main():
    question = input("Please what type of variation is it ... |> ")

    if question == "direct":

        question = input("Please what is the value of the initial 1st variable => ").isdigit()

        if question:
            int(question)

        another_question = input("Please what is the value of the initial 2nd variable => ").isdigit()

        if another_question:
            int(another_question)

        direct_variation(question, another_question)

    elif question == "inverse":
        pass
    elif question == "joint":
        pass
    elif question == "partial":
        pass
    else:
        print("Sorry can't find the type of variation mentioned ...")
        exit()


def direct_variation(initial_var, another_initial_var):

    def find_constant(value_1st_var, value_2nd_var):
        side = value_1st_var / value_2nd_var
        another_side = value_2nd_var / value_2nd_var
        k = side
        return k

    k = find_constant(initial_var, another_initial_var)

    print(k)

main()
