search_query = input("What do you want to search on Google: ")

def main(query):
    if query != "":
        import webbrowser
        import time
        google_search = f"https://www.google.com/search?q={query}/"
        print("\nYour search query has been saved and processed opening in Google")
        time.sleep(3)
        webbrowser.open(google_search)
    else:
        print("So can't search google for an empty string")


main(search_query)
