def main():
    import os
    folder = input("Where do you want me to watch: ")
    settings_dir_exists = os.path.exists('{}'.format(f"{folder}/settings/"))

    if folder != "":
        if settings_dir_exists:
            print("Available settings in the location")
            print("Grabbing needed configuration")
            settings_conf = open(f'{folder}/settings/configurations.txt', 'r')
            lines = settings_conf.readlines()
            print(lines)
        elif not settings_dir_exists:
            print("No settings found")
            print("Going through quick-setup of the configurations, please endure ...")
        # var = lines[1].strip()


def watch():
    pass


main()
