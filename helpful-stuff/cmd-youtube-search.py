search_query = input("What do you want to search on YouTube: ")

def main(query):
    if query != "":
        import webbrowser
        import time
        youtube_search = f"https://www.youtube.com/search?q={query}/"
        formatted_youtube_search = youtube_search.replace(" ", "+")
        print("\nYour search query has been saved and processed opening in YouTube")
        time.sleep(3)
        webbrowser.open(formatted_youtube_search)
    else:
        print("So can't search google for an empty string")


main(search_query)
