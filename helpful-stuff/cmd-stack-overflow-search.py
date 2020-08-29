def main(search_type):
    if search_type != "":
        if search_type == "multiple":
            print("")
            query = input("What do you want to search on StackOverflow |?> seperate with "" |> ")
            multiple(query)
        elif search_type == "single":
            print("")
            query = input("What do you want to search on StackOverflow: ")
            single(query)
    else:
        print("\nGoing for [default=single]\n")
        query = input("What do you want to search on StackOverflow: ")
        single(query)

def single(query):
    if query != "":
        """ Needed modules """
        import webbrowser, time, os, platform
        op = platform.system()

        stackoverflow_search = f"https://www.stackoverflow.com/search?q={query}"  # Constructed search query
        print("\nYour search query has been saved and processed opening in StackOverflow")
        time.sleep(3)
        webbrowser.open(stackoverflow_search)

        if op == "Windows":
            os.system("cls")
        elif op == "Linux" or op == "Darwin":
            os.system("clear")

    else:
        import os, platform, time
        op = platform.system()

        time.sleep(2)
        if op == "Windows":
            os.system("cls")
        elif op == "Linux" or op == "Darwin":
            os.system("clear")
        else:
            print("Couldn't find system type")

    print("\nSo can't search stackoverflow for an empty string, try again\n")

def multiple(query):
    if query != "":
        search_query = query.split("\"\"")
        print("")
        for search in search_query:
            print(search)

question = input("\nWant to do [multiple] or [single] search |> ")
main(question)
