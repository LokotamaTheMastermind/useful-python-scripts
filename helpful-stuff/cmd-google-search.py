try:
    while True:
        print("")
        search_query = input("What do you want to search on Google: ")  # Google Search Query

        def main(query):
            if query != "":
                """" Needed modules """
                import webbrowser
                import time
                import os
                import platform
                google_search = f"https://www.google.com/search?q={query}"  # Formation of google search uri
                op = platform.system()  # Grabs opearting system type
                print("\nYour search query has been saved and processed opening in Google")
                time.sleep(3)  # Remove this if you want webbrowser opening to be snappy
                webbrowser.open(google_search)  # Opens formed uri in webbrowser

                """ Available value => [Windows, Darwin (MAC), Linux] """
                if op == "Windows":
                    os.system("cls")
                elif op == "Linux" or op == "Darwin":
                    os.system("clear")
                else:
                    print("Couldn't find system type")
            else:
                import platform
                import os
                op = platform.system()  # Grabs opearting system type
                if op == "Windows":
                    os.system("cls")
                elif op == "Linux" or op == "Darwin":
                    os.system("clear")
                else:
                    print("Couldn't find system type")
                print("\nSo can't search google for an empty string, try again!")

        main(search_query)
except KeyboardInterrupt:
    import time
    print("\n\nQuitting program")
    time.sleep(3)
