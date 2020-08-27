def main():
    import pickle

    first_setup = True

    file_saved = pickle.dump(first_setup, open("settings/configurations.txt", mode="w", encoding="utf-8"))

    print("Welcome to the 1st ever Python automated Git Project Manager ...")

    if not first_setup:
        pass
    elif first_setup:
        print("Great")
    pass

main()
