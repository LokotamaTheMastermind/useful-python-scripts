try:
    while 1:
        print("")
        search_query = input("What do you want to search on YouTube: ")
        def main(query):
            if query != "":
                import webbrowser, time, os, platform
                op = platform.system()
                youtube_search = f"https://www.youtube.com/search?q={query}"  # Constructed search query
                formatted_youtube_search = youtube_search.replace(" ", "+")  # Formatted search query
                print("\nYour search query has been saved and processed opening in YouTube")
                time.sleep(3)
                webbrowser.open(formatted_youtube_search)
                if op == "Windows":
                    os.system("cls")
                elif op == "Linux" or op == "Darwin":
                    os.system("clear")
            else:
                import os, platform
                op = platform.system()
                if op == "Windows":
                    os.system("cls")
                elif op == "Linux" or op == "Darwin":
                    os.system("clear")
                else:
                    print("Couldn't find system type")
                print("\nSo can't search youtube for an empty string, try again\n")

        main(search_query)
except KeyboardInterrupt:
    import time
    print("\n\nQuitting the console")
    time.sleep(2)
